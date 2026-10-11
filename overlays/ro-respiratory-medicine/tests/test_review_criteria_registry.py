import json
import shutil
from pathlib import Path

import check_overlay
from registries import build_registries
from scripts.resolve_review_target_context import resolve

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
REG = ROOT / "registries/generated/review_criteria_registry.json"
def test_build_is_deterministic_validates_and_preserves_core_broad_rows():
    first = build_registries.rendered(build_registries.build_review_criteria())
    assert first == build_registries.rendered(build_registries.build_review_criteria())
    registry = json.loads(first)
    core = json.loads((REPO / "shared/review_criteria_registry.json").read_text())
    assert registry["criteria"][:len(core["criteria"])] == core["criteria"]
    assert registry["authority_classes"]["broad_field_fallback"] == core["authority_classes"]["broad_field_fallback"]
    from scripts.resolve_review_target_context import validate_registry
    validate_registry(registry)
    assert build_registries.main(["--check"]) == 0


def test_ro_respiratory_cohort_resolves_record_ers_ats_and_advisory_statements():
    declaration = json.loads((ROOT / "tests/fixtures/review_target_context/ro-respiratory-cohort.json").read_text())
    result = resolve(declaration, json.loads(REG.read_text()))
    selected = set(result["selected_criterion_ids"])
    assert "overlay.record.routine-data" in selected
    assert "field.ers-ats.respiratory-measurement" in selected
    pointers = {item["criterion_id"]: item for item in result["selected_criteria"]}
    for criterion_id in selected:
        if criterion_id.startswith("ro.manuscript-statements."):
            assert pointers[criterion_id]["blocking_eligible"] is False


def test_unbacked_source_and_stale_generated_registry_fail(tmp_path):
    overlay = tmp_path / "overlay"
    shutil.copytree(ROOT, overlay, ignore=shutil.ignore_patterns("__pycache__"))
    delta_path = overlay / "registries/review_criteria.delta.json"
    delta = json.loads(delta_path.read_text())
    delta["criteria"][0]["source"]["uri"] = "https://example.invalid/unbacked"
    delta_path.write_text(json.dumps(delta))
    errors = check_overlay.check_review_criteria_registry(overlay, REPO)
    assert errors and "stale" in errors[0]

    # Rebuild the copied artifact so the semantic source-backing check is reached.
    fresh = build_registries.rendered(build_registries.build_review_criteria(
        core_path=REPO / "shared/review_criteria_registry.json", delta_path=delta_path
    ))
    generated = overlay / "registries/generated/review_criteria_registry.json"
    generated.write_text(fresh)
    errors = check_overlay.check_review_criteria_registry(overlay, REPO)
    assert errors and "not backed by a data/ row" in errors[0]

    delta = json.loads(delta_path.read_text())
    delta["criteria"][0]["source"]["uri"] = "https://europepmc.org/article/MED/31613151"
    delta_path.write_text(json.dumps(delta))
    errors = check_overlay.check_review_criteria_registry(overlay, REPO)
    assert errors and "stale" in errors[0]

    registry = json.loads(generated.read_text())
    registry["registry_version"] = "wrong-prefix-ro.1"
    generated.write_text(json.dumps(registry))
    errors = check_overlay.check_review_criteria_registry(overlay, REPO)
    assert errors and "version does not match" in errors[0]


def test_noncurrent_sources_resolve_as_advisory():
    registry = json.loads(REG.read_text())
    row = next(row for row in registry["criteria"] if row["criterion_id"] == "overlay.record.routine-data")
    row["source"]["freshness"] = "stale"
    declaration = {
        "schema_version": "review-target-declaration/1.0", "confirmed_by": "author",
        "confirmed_at": "2026-10-10T12:00:00Z", "criteria_as_of": "2026-10-10",
        "discipline": {"primary": "Medicine", "subfield": "Respiratory medicine", "additional_disciplines": []},
        "target": {"venue": None, "track": None, "contribution_type": "Original Article"},
        "reporting_design_overlays": ["RECORD"], "criterion_selection": {"mode": "all_applicable", "ids": []},
        "precedence": [
            {"rank": 1, "authority_class": "official_venue_type"}, {"rank": 2, "authority_class": "field_society_standard"},
            {"rank": 3, "authority_class": "reporting_design_overlay"}, {"rank": 4, "authority_class": "broad_field_fallback"},
        ],
    }
    result = resolve(declaration, registry)
    pointer = next(item for item in result["selected_criteria"] if item["criterion_id"] == "overlay.record.routine-data")
    assert pointer["blocking_eligible"] is False
    assert "source_stale" in pointer["advisory_reasons"]
