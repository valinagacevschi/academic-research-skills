import json
import shutil
import subprocess
from datetime import date
from pathlib import Path

import pytest
import yaml

import check_overlay as check

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]


def test_workflow_runs_for_overlay_and_core_registry_changes():
    workflow = yaml.safe_load((REPO_ROOT / ".github/workflows/ro-overlay.yml").read_text())
    triggers = workflow[True]
    expected = {
        "overlays/ro-respiratory-medicine/**",
        "shared/human_subjects_authority_registry.json",
        "shared/review_criteria_registry.json",
    }
    for event in ("pull_request", "push"):
        assert expected <= set(triggers[event]["paths"])


def valid_row(**changes):
    row = json.loads((ROOT / "tests/fixtures/evidence_row.json").read_text())
    row.update(changes)
    return row


def write_data(root, name, rows):
    data = root / "data"
    data.mkdir(exist_ok=True)
    (data / name).write_text(json.dumps({"schema_version": "ro-overlay-evidence-rows/1.0", "rows": rows}))


def test_manifest_schema_passes():
    assert check.check_manifest(ROOT) == []


def test_manifest_schema_fails(tmp_path):
    shutil.copytree(ROOT / "schemas", tmp_path / "schemas")
    (tmp_path / "MANIFEST.json").write_text('{"overlay_id":"wrong"}')
    assert check.check_manifest(tmp_path)


def test_upstream_drift_matches(tmp_path):
    for name in ("human_subjects_authority_registry.json", "review_criteria_registry.json"):
        (tmp_path / "shared").mkdir(exist_ok=True)
        shutil.copy(ROOT.parents[1] / "shared" / name, tmp_path / "shared" / name)
    assert check.check_upstream_drift(ROOT, tmp_path) == []


def test_upstream_drift_mismatch_requests_rebuild(tmp_path):
    (tmp_path / "shared").mkdir()
    (tmp_path / "shared/human_subjects_authority_registry.json").write_text('{"registry_version":"old"}')
    (tmp_path / "shared/review_criteria_registry.json").write_text('{"registry_version":"2026.08.24"}')
    errors = check.check_upstream_drift(ROOT, tmp_path)
    assert errors and "re-run build_registries.py" in errors[0]


def test_evidence_row_schema_passes(tmp_path):
    write_data(tmp_path, "one.json", [valid_row()])
    (tmp_path / "schemas").mkdir()
    shutil.copy(ROOT / "schemas/evidence_row.schema.json", tmp_path / "schemas/evidence_row.schema.json")
    rows, errors = check.load_rows(tmp_path)
    assert [row["value_id"] for row in rows] == ["fixture.value"]
    assert errors == []


@pytest.mark.parametrize("changes,expected", [
    ({"value_id": "Invalid ID"}, "does not match"),
    ({"source": {"url": "", "title": "t", "locator": "l"}}, "'' should be non-empty"),
    ({"area": ""}, "should be non-empty"),
    ({"area": "   "}, "does not match"),
    ({"statement": ""}, "should be non-empty"),
    ({"statement": "   "}, "does not match"),
    ({"source": {"url": "   ", "title": "t", "locator": "l"}}, "does not match"),
    ({"source": {"url": "u", "title": "   ", "locator": "l"}}, "does not match"),
    ({"source": {"url": "u", "title": "t", "locator": "   "}}, "does not match"),
    ({"evidence_tag": "other"}, "not one of"),
])
def test_evidence_row_schema_fails(tmp_path, changes, expected):
    write_data(tmp_path, "one.json", [valid_row(**changes)])
    (tmp_path / "schemas").mkdir()
    shutil.copy(ROOT / "schemas/evidence_row.schema.json", tmp_path / "schemas/evidence_row.schema.json")
    _, errors = check.load_rows(tmp_path)
    assert errors and expected in " ".join(errors)


def test_duplicate_ids_across_two_files_fail(tmp_path):
    (tmp_path / "schemas").mkdir()
    shutil.copy(ROOT / "schemas/evidence_row.schema.json", tmp_path / "schemas/evidence_row.schema.json")
    write_data(tmp_path, "a.json", [valid_row()])
    write_data(tmp_path, "b.json", [valid_row(area="sleep")])
    errors, _ = check.check_evidence(tmp_path, date(2026, 1, 1))
    assert any("duplicate value_id fixture.value" in item for item in errors)


@pytest.mark.parametrize("tag,numeric,use,should_fail", [
    ("recalled", False, "reference", True),
    ("unreachable", False, "reference", True),
    ("secondary", True, "fact_check", True),
    ("secondary", False, "fact_check", True),
    ("primary-abstract", True, "fact_check", False),
    ("secondary", False, "advisory", False),
])
def test_evidence_tag_rules(tmp_path, tag, numeric, use, should_fail):
    (tmp_path / "schemas").mkdir()
    shutil.copy(ROOT / "schemas/evidence_row.schema.json", tmp_path / "schemas/evidence_row.schema.json")
    write_data(tmp_path, "rows.json", [valid_row(evidence_tag=tag, numeric=numeric, use=use)])
    errors, _ = check.check_evidence(tmp_path, date(2026, 1, 1))
    assert bool(errors) is should_fail


@pytest.mark.parametrize("window,verified,today,expected", [
    (6, "2026-01-31", "2026-07-31", "fact_check"),
    (6, "2026-01-31", "2026-08-01", "advisory"),
    (12, "2025-02-28", "2026-02-28", "fact_check"),
    (12, "2025-02-28", "2026-03-01", "advisory"),
])
def test_staleness_boundaries(window, verified, today, expected):
    row = valid_row(use="fact_check", verified_at=verified, review_window_months=window)
    assert check.effective_use(row, today) == expected


def test_stale_fact_check_warns_and_is_demoted(tmp_path):
    (tmp_path / "schemas").mkdir()
    shutil.copy(ROOT / "schemas/evidence_row.schema.json", tmp_path / "schemas/evidence_row.schema.json")
    write_data(tmp_path, "rows.json", [valid_row(use="fact_check", verified_at="2025-01-01")])
    errors, warnings = check.check_evidence(tmp_path, date(2026, 1, 2))
    assert errors == []
    assert warnings == ["fixture.value: demoted: will be treated as advisory"]


def test_later_artifacts_are_skipped_when_absent(tmp_path):
    results = check.check_later_artifacts(tmp_path)
    assert len(results) == 3
    assert all(not present and reason.startswith("artifact not present:") for _, present, reason in results)


def git(repo, *args):
    return subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)


def test_boundary_passes_inside_allowed_paths(tmp_path):
    git(tmp_path, "init", "-b", "main")
    git(tmp_path, "config", "user.email", "test@example.org")
    git(tmp_path, "config", "user.name", "Test")
    (tmp_path / "README").write_text("base")
    git(tmp_path, "add", "README")
    git(tmp_path, "commit", "-m", "base")
    git(tmp_path, "checkout", "-b", "work")
    (tmp_path / "overlays/ro-respiratory-medicine").mkdir(parents=True)
    (tmp_path / "overlays/ro-respiratory-medicine/file").write_text("allowed")
    assert check.check_boundary(tmp_path, "main") == []


def test_boundary_fails_outside_allowed_paths_and_ignores_scratch(tmp_path):
    git(tmp_path, "init", "-b", "main")
    git(tmp_path, "config", "user.email", "test@example.org")
    git(tmp_path, "config", "user.name", "Test")
    (tmp_path / "README").write_text("base")
    git(tmp_path, "add", "README")
    git(tmp_path, "commit", "-m", "base")
    git(tmp_path, "checkout", "-b", "work")
    (tmp_path / ".scratch").mkdir()
    (tmp_path / ".scratch/map.md").write_text("ignored")
    (tmp_path / "core.txt").write_text("outside")
    errors = check.check_boundary(tmp_path, "main")
    assert errors and "core.txt" in errors[0]
    assert ".scratch/map.md" not in errors[0]


def test_cli_reports_later_slice_skips(capsys):
    code = check.main(["--overlay-root", str(ROOT), "--repo-root", str(ROOT.parents[1]), "--today", "2026-10-10"])
    output = capsys.readouterr().out
    assert code == 0
    assert output.count("SKIPPED ") == 3
    assert output.count("artifact not present:") == 2
