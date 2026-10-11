"""Mutation tests for check_workflow_classification.py (#755)."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from check_workflow_classification import (
    DOC_RELPATH,
    WORKFLOWS_DIR,
    run_all_checks,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    """Real doc + real workflow inventory, copied so mutations are isolated."""
    dst_doc = tmp_path / DOC_RELPATH
    dst_doc.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(REPO_ROOT / DOC_RELPATH, dst_doc)
    (tmp_path / WORKFLOWS_DIR).mkdir(parents=True, exist_ok=True)
    for pattern in ("*.yml", "*.yaml"):
        for wf in sorted((REPO_ROOT / WORKFLOWS_DIR).glob(pattern)):
            shutil.copyfile(wf, tmp_path / WORKFLOWS_DIR / wf.name)
    return tmp_path


def _mutate_doc(root: Path, old: str, new: str) -> None:
    doc = root / DOC_RELPATH
    text = doc.read_text(encoding="utf-8")
    assert old in text, f"mutation anchor not found: {old!r}"
    doc.write_text(text.replace(old, new), encoding="utf-8")


def test_real_tree_passes() -> None:
    assert run_all_checks(REPO_ROOT) == []


def test_fixture_baseline_passes(repo: Path) -> None:
    assert run_all_checks(repo) == []


def test_missing_doc_is_single_fatal_error(repo: Path) -> None:
    (repo / DOC_RELPATH).unlink()
    errors = run_all_checks(repo)
    assert len(errors) == 1
    assert "missing" in errors[0]


def test_missing_section_fires(repo: Path) -> None:
    _mutate_doc(
        repo,
        "### 7.1 CI workflow enforcement classes",
        "### 7.1 CI workflow something else",
    )
    errors = run_all_checks(repo)
    assert any("WC-1" in e and "not found" in e for e in errors)


def test_new_workflow_without_row_fires(repo: Path) -> None:
    (repo / WORKFLOWS_DIR / "brand-new-check.yml").write_text(
        "name: Brand New\non:\n  push:\n", encoding="utf-8"
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-1" in e and "brand-new-check.yml" in e and "no row" in e
        for e in errors
    )


def test_row_for_removed_workflow_fires(repo: Path) -> None:
    (repo / WORKFLOWS_DIR / "pytest.yml").unlink()
    errors = run_all_checks(repo)
    assert any(
        "WC-1" in e and "pytest.yml" in e and "names no file" in e
        for e in errors
    )


def test_duplicate_row_fires(repo: Path) -> None:
    doc = repo / DOC_RELPATH
    lines = doc.read_text(encoding="utf-8").split("\n")
    idx = next(
        i for i, line in enumerate(lines) if line.startswith("| `pytest.yml`")
    )
    lines.insert(idx, lines[idx])
    doc.write_text("\n".join(lines), encoding="utf-8")
    errors = run_all_checks(repo)
    assert any(
        "pytest.yml" in e and "more than one table row" in e for e in errors
    )


def test_off_vocabulary_class_fires(repo: Path) -> None:
    _mutate_doc(repo, "| Blocking |", "| Mandatory |")
    errors = run_all_checks(repo)
    assert any(
        "WC-2" in e and "Mandatory" in e for e in errors
    )
    # Reclassifying the only blocking row also changes the category tally.
    assert any("WC-3" in e for e in errors)


def test_typo_suffix_class_fires(repo: Path) -> None:
    # `Blockingg` must not pass on a prefix match — the vocabulary term is
    # matched as a whole word (codex R1 finding).
    _mutate_doc(repo, "| Blocking |", "| Blockingg |")
    errors = run_all_checks(repo)
    assert any("WC-2" in e and "Blockingg" in e for e in errors)


def test_class_with_qualifier_still_passes(repo: Path) -> None:
    # Qualifiers after a boundary are in-vocabulary; the count is unchanged,
    # so WC-3 stays quiet too.
    _mutate_doc(
        repo,
        "| Blocking |",
        "| Blocking (runs required checks) |",
    )
    assert run_all_checks(repo) == []


def test_yaml_extension_workflow_fires(repo: Path) -> None:
    # GitHub Actions also reads *.yaml — a completeness lint bypassable by a
    # file extension fails open in the exact direction it exists to prevent.
    (repo / WORKFLOWS_DIR / "alt-ext.yaml").write_text(
        "name: Alt\non:\n  push:\n", encoding="utf-8"
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-1" in e and "alt-ext.yaml" in e and "no row" in e for e in errors
    )


def test_count_line_drift_fires(repo: Path) -> None:
    _mutate_doc(repo, "5 blocking", "6 blocking")
    errors = run_all_checks(repo)
    assert any("WC-3" in e and "count line" in e for e in errors)


def test_renamed_bypass_token_fires(repo: Path) -> None:
    # The table's eval bypass must exist verbatim in the workflow —
    # renaming it there cannot leave the table stale with CI green.
    wf = repo / WORKFLOWS_DIR / "eval-harness.yml"
    wf.write_text(
        wf.read_text(encoding="utf-8").replace(
            "[eval-regression-acknowledged]", "[eval-override]"
        ),
        encoding="utf-8",
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-4" in e and "[eval-regression-acknowledged]" in e for e in errors
    )


def test_token_surviving_only_in_comment_fires(repo: Path) -> None:
    # Renaming the executable token while an old comment still mentions it
    # must not satisfy WC-4 (codex R2 finding).
    wf = repo / WORKFLOWS_DIR / "eval-harness.yml"
    text = wf.read_text(encoding="utf-8")
    text = text.replace("[eval-regression-acknowledged]", "[eval-override]")
    wf.write_text(
        text + "\n# legacy note: the old token was [eval-regression-acknowledged]\n",
        encoding="utf-8",
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-4" in e and "[eval-regression-acknowledged]" in e for e in errors
    )


def test_malformed_token_spelling_fires(repo: Path) -> None:
    # `[eval_regression_acknowledged]` (underscore typo) must fail loudly, not silently
    # fall out of the token grammar (codex R4 finding).
    _mutate_doc(repo, "[eval-regression-acknowledged]", "[eval_regression_acknowledged]")
    errors = run_all_checks(repo)
    assert any(
        "WC-4" in e and "eval_regression_acknowledged" in e and "not a well-formed" in e
        for e in errors
    )


def test_whitespace_token_spelling_fires(repo: Path) -> None:
    # `[eval regression acknowledged]` (space typo) must also fail loudly (codex R5).
    _mutate_doc(repo, "[eval-regression-acknowledged]", "[eval regression acknowledged]")
    errors = run_all_checks(repo)
    assert any(
        "WC-4" in e and "eval regression acknowledged" in e and "not a well-formed" in e
        for e in errors
    )


def test_bogus_unbackticked_row_fires(repo: Path) -> None:
    # A data row whose first cell is not a backticked workflow filename
    # must fail WC-1, not silently drop out of the inventory and count
    # (codex R6 finding).
    _mutate_doc(
        repo,
        "| `pytest.yml` |",
        "| not-a-workflow | bogus | bogus | Advisory | none |\n"
        "| `pytest.yml` |",
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-1" in e and "not-a-workflow" in e and "malformed" in e
        for e in errors
    )


def test_malformed_row_arity_fires(repo: Path) -> None:
    _mutate_doc(
        repo,
        "| `pytest.yml` | PR + push to main, both path-filtered (scripts/tests/contracts/config, adapter references, `bibliography_agent`) | adapter + script test suite | Blocking | none |",
        "| `pytest.yml` | PR + push | Blocking | none |",
    )
    errors = run_all_checks(repo)
    assert any(
        "WC-1" in e and "pytest.yml" in e and "expected 5" in e
        for e in errors
    )
