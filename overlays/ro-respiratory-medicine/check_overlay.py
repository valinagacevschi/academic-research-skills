#!/usr/bin/env python3
"""Lint the Romanian respiratory-medicine overlay without changing core ARS."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from calendar import monthrange
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def validate_json(instance: Any, schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in validator.iter_errors(instance)]


def add_months(value: date, months: int) -> date:
    month_index = value.month - 1 + months
    year = value.year + month_index // 12
    month = month_index % 12 + 1
    return date(year, month, min(value.day, monthrange(year, month)[1]))


def effective_use(row: dict[str, Any], today: date | str) -> str:
    """Return advisory when a row has passed its review window."""
    current = date.fromisoformat(today) if isinstance(today, str) else today
    verified = date.fromisoformat(row["verified_at"])
    if current > add_months(verified, row["review_window_months"]):
        return "advisory"
    return row["use"]


def load_rows(overlay_root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    schema_path = overlay_root / "schemas/evidence_row.schema.json"
    for path in sorted((overlay_root / "data").glob("*.json")):
        try:
            payload = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if not isinstance(payload, dict) or payload.get("schema_version") != "ro-overlay-evidence-rows/1.0" or not isinstance(payload.get("rows"), list) or set(payload) != {"schema_version", "rows"}:
            errors.append(f"{path.name}: expected schema_version ro-overlay-evidence-rows/1.0 and rows array")
            continue
        for index, row in enumerate(payload["rows"], 1):
            label = f"{path.name} row {index}"
            problems = validate_json(row, schema_path)
            errors.extend(f"{label}: {problem}" for problem in problems)
            if not problems:
                rows.append(row)
    return rows, errors


def check_manifest(root: Path) -> list[str]:
    path = root / "MANIFEST.json"
    try:
        manifest = load_json(path)
        errors = validate_json(manifest, root / "schemas/manifest.schema.json")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [f"manifest: {exc}"]
    return [f"manifest: {error}" for error in errors]


def check_upstream_drift(root: Path, repo_root: Path) -> list[str]:
    try:
        expected = load_json(root / "MANIFEST.json")["upstream_registry_versions"]
        actual = {
            "human_subjects": load_json(repo_root / "shared/human_subjects_authority_registry.json")["registry_version"],
            "review_criteria": load_json(repo_root / "shared/review_criteria_registry.json")["registry_version"],
        }
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        return [f"upstream drift: unable to read registry versions ({exc})"]
    if expected != actual:
        return [f"upstream drift: manifest {expected} != registries {actual}; re-run build_registries.py"]
    return []


def check_evidence(root: Path, today: date) -> tuple[list[str], list[str]]:
    rows, errors = load_rows(root)
    seen: set[str] = set()
    warnings: list[str] = []
    for row in rows:
        value_id = row["value_id"]
        if value_id in seen:
            errors.append(f"evidence rows: duplicate value_id {value_id}")
        seen.add(value_id)
        tag, use = row["evidence_tag"], row["use"]
        if tag in {"recalled", "unreachable"}:
            errors.append(f"evidence rows: {value_id} has forbidden evidence_tag {tag}")
        if row["numeric"] and use == "fact_check" and tag not in {"primary-full-text", "primary-abstract"}:
            errors.append(f"evidence rows: {value_id} numeric fact_check requires a primary evidence tag")
        if use == "fact_check" and tag == "secondary":
            errors.append(f"evidence rows: {value_id} secondary evidence cannot drive a fact_check")
        if effective_use(row, today) == "advisory" and use == "fact_check":
            warnings.append(f"{value_id}: demoted: will be treated as advisory")
        elif effective_use(row, today) == "advisory" and use != "advisory":
            warnings.append(f"{value_id}: demoted to advisory")
    return errors, warnings


def check_later_artifacts(root: Path) -> list[tuple[str, bool, str]]:
    artifacts = [
        "profile/respiratory_medicine.json",
        "registries/generated/human_subjects_authority_registry.json",
        "registries/generated/review_criteria_registry.json",
    ]
    return [(path, (root / path).exists(), f"artifact not present: {path}") for path in artifacts]


def changed_paths(repo_root: Path, base: str) -> tuple[set[str], str | None]:
    paths: set[str] = set()
    commands = [
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        ["git", "diff", "--name-only"],
        ["git", "diff", "--cached", "--name-only"],
        ["git", "ls-files", "--others", "--exclude-standard"],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=repo_root, text=True, capture_output=True)
        if result.returncode:
            return paths, result.stderr.strip() or f"command failed: {' '.join(command)}"
        paths.update(line for line in result.stdout.splitlines() if line)
    return paths, None


def check_boundary(repo_root: Path, base: str | None) -> list[str] | None:
    if not base:
        return None
    paths, failure = changed_paths(repo_root, base)
    if failure:
        return [f"boundary: {failure}"]
    allowed_overlay = "overlays/ro-respiratory-medicine/"
    allowed_workflow = ".github/workflows/ro-overlay.yml"
    outside = sorted(path for path in paths if not path.startswith(".scratch/") and not path.startswith(allowed_overlay) and path != allowed_workflow)
    return [f"boundary: disallowed changed paths: {', '.join(outside)}"] if outside else []


def report(label: str, status: str, reason: str) -> None:
    print(f"{status} {label}: {reason}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overlay-root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--today", help="current date in YYYY-MM-DD format")
    parser.add_argument("--base", help="git ref for the boundary check")
    args = parser.parse_args(argv)
    try:
        today = date.fromisoformat(args.today) if args.today else date.today()
    except ValueError:
        report("date", "FAIL", "--today must be YYYY-MM-DD")
        return 1

    failures = 0
    for label, errors in (("manifest", check_manifest(args.overlay_root)), ("upstream drift", check_upstream_drift(args.overlay_root, args.repo_root))):
        if errors:
            for error in errors:
                report(label, "FAIL", error)
            failures += 1
        else:
            report(label, "PASS", "valid")

    errors, warnings = check_evidence(args.overlay_root, today)
    if errors:
        for error in errors:
            report("evidence rows", "FAIL", error)
        failures += 1
    else:
        report("evidence rows", "PASS", "all data rows valid")
    if warnings:
        report("demoted to advisory", "WARN", "; ".join(warnings))
    else:
        report("demoted to advisory", "PASS", "none")

    for label, present, reason in check_later_artifacts(args.overlay_root):
        report(label, "PASS" if present else "SKIPPED", "present" if present else reason)
    boundary_errors = check_boundary(args.repo_root, args.base)
    if boundary_errors is None:
        report("boundary", "SKIPPED", "--base not supplied")
    elif boundary_errors:
        for error in boundary_errors:
            report("boundary", "FAIL", error)
        failures += 1
    else:
        report("boundary", "PASS", "changed paths are within the allowed boundary")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
