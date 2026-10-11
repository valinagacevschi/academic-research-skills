#!/usr/bin/env python3
"""Check scholar-declared venue extras against a manuscript."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
OVERLAY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import verify_submission_package as core  # noqa: E402

EXTRAS_SCHEMA = Path(__file__).with_name("venue_extras.schema.json")
ERS_ROW_ID = "venue.ers_congress.counting_rule"
PRIMARY_TAGS = {"primary-full-text", "primary-abstract"}
IMAGE_RE = re.compile(r"!\[[^]]*\]\([^)]*\)")


def load_data(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(raw)
    return yaml.safe_load(raw)


def check_ers_evidence() -> str | None:
    path = OVERLAY / "data/venues.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return f"ERS evidence unavailable: {exc}"
    row = next((r for r in payload.get("rows", []) if r.get("value_id") == ERS_ROW_ID), None)
    if row is None:
        return f"missing evidence row {ERS_ROW_ID}"
    if row.get("evidence_tag") not in PRIMARY_TAGS:
        return f"evidence row {ERS_ROW_ID} is non-primary ({row.get('evidence_tag')})"
    return None


def ers_char_count(abstract: str) -> int:
    """Count body + Markdown pipe-table cells + image allowances per ERS row."""
    lines = abstract.splitlines()
    table_cells = 0
    body_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped[1:-1].split("|")]
            # Markdown separator rows are syntax, not table content.
            if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                table_cells += sum(len(cell) + 1 for cell in cells)
        else:
            body_lines.append(line)
    body = "\n".join(body_lines)
    figures = len(IMAGE_RE.findall(body))
    body = IMAGE_RE.sub("", body)
    # ERS row venue.ers_congress.counting_rule: body + tables + figures,
    # each table cell adds one character; each figure consumes 277 characters of the allowance.
    return len(body.strip()) + table_cells + 277 * figures


def word_count(abstract: str) -> int:
    return core._word_count(abstract)


def abstract_headings(abstract: str) -> list[str]:
    """Collect textual labels such as `**Background:**` in reading order."""
    labels: list[str] = []
    for line in abstract.splitlines():
        line = re.sub(r"^\s*#{1,6}\s*", "", line)
        match = re.match(r"\s*(?:\*\*)?([^:*]+?)(?:\*\*)?\s*:\s*", line)
        if match:
            labels.append(match.group(1).strip())
    return labels


def emit(status: str, label: str, detail: str) -> None:
    print(f"{status} {label}: {detail}")


def run(extras: dict[str, Any], manuscript_path: Path) -> int:
    failures = 0
    try:
        manuscript = manuscript_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        emit("FAIL", "manuscript", f"cannot read: {exc}")
        return 1
    suffix = manuscript_path.suffix.lower()
    if suffix == ".docx":
        abstract = None
        docx_unsupported = True
    elif suffix in {".md", ".txt", ".tex"}:
        abstract = core._abstract_text(manuscript_path.name, manuscript)
        docx_unsupported = False
    else:
        emit("FAIL", "manuscript", f"unsupported extension {suffix or '(none)'}")
        return 1

    limit = extras.get("abstract_limit")
    if limit is None:
        emit("NOT-CHECKED(field not declared)", "abstract length", "abstract_limit is null")
    elif docx_unsupported:
        emit("NOT-CHECKED(core does not extract DOCX)", "abstract length", "")
    elif abstract is None:
        emit("NOT-CHECKED(abstract not found)", "abstract length", "")
    elif limit["counting_rule"] == "ers_congress":
        reason = check_ers_evidence()
        if reason:
            emit("NOT-CHECKED(ERS rule unavailable)", "abstract length", reason)
        else:
            count = ers_char_count(abstract) if limit["unit"] == "characters" else word_count(abstract)
            status = "PASS" if count <= limit["value"] else "FAIL"
            emit(status, "abstract length", f"{count} {limit['unit']} / {limit['value']} ({limit['counting_rule']})")
            failures += status == "FAIL"
    else:
        count = len(abstract.strip()) if limit["unit"] == "characters" else word_count(abstract)
        status = "PASS" if count <= limit["value"] else "FAIL"
        emit(status, "abstract length", f"{count} {limit['unit']} / {limit['value']}")
        failures += status == "FAIL"

    title_limit = extras.get("title_char_limit")
    if title_limit is None:
        emit("NOT-CHECKED(field not declared)", "title length", "title_char_limit is null")
    elif docx_unsupported:
        emit("NOT-CHECKED(core does not extract DOCX)", "title length", "")
    else:
        first = next((title for title, _, _ in core._md_sections(manuscript) if not core._is_abstract_title(title)), None)
        title = first or ""
        count = len(title)
        status = "PASS" if first is not None and count <= title_limit else "FAIL"
        emit(status, "title length", f"{count} characters / {title_limit}")
        failures += status == "FAIL"

    required = extras.get("required_abstract_headings")
    if required is None:
        emit("NOT-CHECKED(field not declared)", "abstract headings", "required_abstract_headings is null")
    elif docx_unsupported or abstract is None:
        emit("NOT-CHECKED(abstract unavailable)", "abstract headings", "")
    else:
        match_mode = extras.get("heading_match") or "exact"
        actual = abstract_headings(abstract)
        normalize = (lambda value: value.casefold()) if match_mode == "case_insensitive" else (lambda value: value)
        pos = 0
        missing: list[str] = []
        for heading in required:
            found = next((i for i in range(pos, len(actual)) if normalize(actual[i]) == normalize(heading)), None)
            if found is None:
                missing.append(heading)
            else:
                pos = found + 1
        status = "PASS" if not missing else "FAIL"
        emit(status, "abstract headings", "required headings present in order" if not missing else f"missing or out of order: {', '.join(missing)}")
        failures += status == "FAIL"

    required_extras = extras.get("extras_required")
    if required_extras is None:
        emit("NOT-CHECKED(field not declared)", "submission extras", "extras_required is null")
    elif docx_unsupported:
        emit("NOT-CHECKED(core does not extract DOCX)", "submission extras", "")
    else:
        headings = core._headings(manuscript_path.name, manuscript)
        missing = [name for name in required_extras if not any(name.replace("_", " ").casefold() in heading.casefold().replace("_", " ") for heading in headings)]
        status = "PASS" if not missing else "FAIL"
        emit(status, "submission extras", "all required section headings found" if not missing else f"missing headings: {', '.join(missing)}")
        failures += status == "FAIL"

    checklists = extras.get("checklists_required_with_submission")
    if checklists is None:
        emit("NOT-CHECKED(field not declared)", "checklists reminder", "checklists_required_with_submission is null")
    elif checklists:
        emit("NOT-CHECKED(reminder only)", "checklists required with submission", ", ".join(checklists))
    else:
        emit("NOT-CHECKED(reminder only)", "checklists required with submission", "none declared")
    return int(failures > 0)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extras", required=True, type=Path, help="venue extras YAML or JSON")
    parser.add_argument("--manuscript", required=True, type=Path, help="Markdown, text, TeX, or DOCX manuscript")
    args = parser.parse_args(argv)
    try:
        extras = load_data(args.extras)
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        emit("FAIL", "extras", f"cannot read: {exc}")
        return 1
    errors = list(Draft202012Validator(json.loads(EXTRAS_SCHEMA.read_text(encoding="utf-8"))).iter_errors(extras))
    if errors:
        for error in errors:
            emit("FAIL", "extras schema", error.message)
        return 1
    return run(extras, args.manuscript)


if __name__ == "__main__":
    raise SystemExit(main())
