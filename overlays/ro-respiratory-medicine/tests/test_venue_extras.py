from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

import importlib.util

CHECKER_PATH = Path(__file__).resolve().parents[1] / "venue_extras/check_venue_extras.py"
spec = importlib.util.spec_from_file_location("check_venue_extras", CHECKER_PATH)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = json.loads((ROOT / "overlays/ro-respiratory-medicine/venue_extras/venue_extras.schema.json").read_text())
FIXTURES = ROOT / "overlays/ro-respiratory-medicine/tests/fixtures/venue_extras"


def extras(**updates):
    base = {
        "venue_name": "Example Respiratory Journal (fictional)",
        "abstract_limit": None,
        "title_char_limit": None,
        "required_abstract_headings": None,
        "heading_match": None,
        "extras_required": None,
        "checklists_required_with_submission": None,
        "notes": None,
        "declared_by": "scholar",
    }
    return base | updates


def run_check(tmp_path, monkeypatch, capsys, declaration, text):
    manuscript = tmp_path / "manuscript.md"
    manuscript.write_text(text)
    extras_file = tmp_path / "extras.yaml"
    extras_file.write_text(yaml.safe_dump(declaration))
    assert checker.main(["--extras", str(extras_file), "--manuscript", str(manuscript)]) in (0, 1)
    return capsys.readouterr().out


@pytest.mark.parametrize("unit", ["words", "characters"])
@pytest.mark.parametrize(("length", "expected"), [(4, "PASS"), (5, "PASS"), (6, "FAIL")])
def test_abstract_limit_boundaries(tmp_path, monkeypatch, capsys, unit, length, expected):
    content = "a b c d e f" if unit == "words" else "abcdef"
    text = f"# Title\n\n## Abstract\n\n{content[:length] if unit == 'characters' else ' '.join(content.split()[:length])}\n"
    limit = 5
    output = run_check(tmp_path, monkeypatch, capsys, extras(abstract_limit={"value": limit, "unit": unit, "counting_rule": "plain"}), text)
    assert f"{expected} abstract length" in output


def test_ers_rule_table_figure_exact_arithmetic(tmp_path, monkeypatch, capsys):
    # Body 3 chars + table cells (A=1 + overhead 1, BC=2 + overhead 1) + figure 277 = 285.
    text = "# Title\n\n## Abstract\n\nabc\n| A | BC |\n| --- | --- |\n![x](figure.png)\n"
    assert checker.ers_char_count("abc\n| A | BC |\n| --- | --- |\n![x](figure.png)\n") == 285
    output = run_check(tmp_path, monkeypatch, capsys, extras(abstract_limit={"value": 1, "unit": "characters", "counting_rule": "ers_congress"}), text)
    assert "FAIL abstract length: 285 characters / 1 (ers_congress)" in output


def test_ers_figure_consumes_allowance(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(checker, "check_ers_evidence", lambda: None)
    limit = {"value": 1810, "unit": "characters", "counting_rule": "ers_congress"}
    over = "# Title\n## Abstract\n" + "x" * 1600 + "\n![x](figure.png)\n"
    under = "# Title\n## Abstract\n" + "x" * 1500 + "\n![x](figure.png)\n"

    output = run_check(tmp_path, monkeypatch, capsys, extras(abstract_limit=limit), over)
    assert "FAIL abstract length: 1877 characters / 1810 (ers_congress)" in output

    output = run_check(tmp_path, monkeypatch, capsys, extras(abstract_limit=limit), under)
    assert "PASS abstract length: 1777 characters / 1810 (ers_congress)" in output


def test_title_limit(tmp_path, monkeypatch, capsys):
    text = "# Title\n\n## Abstract\n\nwords\n"
    output = run_check(tmp_path, monkeypatch, capsys, extras(title_char_limit=5), text)
    assert "PASS title length: 5 characters / 5" in output
    output = run_check(tmp_path, monkeypatch, capsys, extras(title_char_limit=4), text)
    assert "FAIL title length" in output


def test_required_heading_order(tmp_path, monkeypatch, capsys):
    declaration = extras(required_abstract_headings=["Background", "Methods"], heading_match="case_insensitive")
    good = run_check(tmp_path, monkeypatch, capsys, declaration, "# Title\n## Abstract\n**Background:** x\n**Methods:** y\n")
    assert "PASS abstract headings" in good
    bad = run_check(tmp_path, monkeypatch, capsys, declaration, "# Title\n## Abstract\n**Methods:** y\n**Background:** x\n")
    assert "FAIL abstract headings" in bad


def test_missing_extras(tmp_path, monkeypatch, capsys):
    output = run_check(tmp_path, monkeypatch, capsys, extras(extras_required=["highlights", "plain_language_summary"]), "# Title\n## Abstract\nwords\n")
    assert "FAIL submission extras: missing headings: highlights, plain_language_summary" in output


def test_undeclared_fields_are_not_checked(tmp_path, monkeypatch, capsys):
    output = run_check(tmp_path, monkeypatch, capsys, extras(), "# Title\n## Abstract\nwords\n")
    assert output.count("NOT-CHECKED(field not declared)") == 5


def test_declared_by_other_than_scholar_rejected():
    validator = Draft202012Validator(SCHEMA)
    assert list(validator.iter_errors(extras(declared_by="overlay")))


def test_missing_ers_row_is_not_checked(tmp_path, monkeypatch, capsys):
    evidence_dir = tmp_path / "data"
    evidence_dir.mkdir()
    (evidence_dir / "venues.json").write_text(json.dumps({"rows": []}))
    monkeypatch.setattr(checker, "OVERLAY", tmp_path)
    output = run_check(tmp_path, monkeypatch, capsys, extras(abstract_limit={"value": 1810, "unit": "characters", "counting_rule": "ers_congress"}), "# Title\n## Abstract\nabc\n")
    assert "NOT-CHECKED(ERS rule unavailable) abstract length: missing evidence row venue.ers_congress.counting_rule" in output
