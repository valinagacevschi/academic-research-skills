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


def check_verified_row_coverage(root: Path, today: date) -> list[str]:
    """Require each effective fact-check evidence row to be anchored or explicitly gapped."""
    try:
        legal_payload = load_json(root / "data/legal_ro.json")
        rows = legal_payload["rows"]
        schema_errors = [
            error.message
            for row in rows
            for error in Draft202012Validator(
                load_json(root / "schemas/evidence_row.schema.json"),
                format_checker=FormatChecker(),
            ).iter_errors(row)
        ]
        if schema_errors:
            return ["legal_ro rows invalid: " + "; ".join(schema_errors)]
        delta = load_json(root / "registries/human_subjects.delta.json")
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        return [f"legal-row coverage: {exc}"]
    anchors = {
        (req["authority_anchor"]["authority_url"], req["authority_anchor"]["provision"])
        for profile in delta["profiles"] for req in profile["requirements"]
    }
    gaps = "\n".join(delta.get("known_gaps", []))
    return [
        f"{row['value_id']}: effective fact_check row is not anchored or named in delta known_gaps"
        for row in rows
        if effective_use(row, today) == "fact_check"
        and (row["source"]["url"], row["source"]["locator"]) not in anchors
        and row["value_id"] not in gaps
    ]


def check_later_artifacts(root: Path) -> list[tuple[str, bool, str]]:
    artifacts = [
        "profile/respiratory_medicine.json",
        "registries/generated/human_subjects_authority_registry.json",
        "registries/generated/review_criteria_registry.json",
    ]
    return [(path, (root / path).exists(), f"artifact not present: {path}") for path in artifacts]


def check_profile(root: Path, repo_root: Path) -> list[str]:
    """Validate the sealed profile and its manifest binding using core contracts."""
    sys.path.insert(0, str(repo_root))
    try:
        from scripts.research_workflow_profile import load_profile

        profile = load_profile(root / "profile/respiratory_medicine.json")
        manifest = load_json(root / "MANIFEST.json")
    except Exception as exc:
        return [f"profile: {exc}"]
    expected = manifest.get("profile_content_sha256")
    if profile["content_sha256"] != expected:
        return [
            "profile: content_sha256 does not match MANIFEST.json "
            f"({profile['content_sha256']} != {expected})"
        ]
    return []


def check_human_subjects_registry(root: Path, repo_root: Path) -> list[str]:
    generated = root / "registries/generated/human_subjects_authority_registry.json"
    if not generated.exists():
        return []
    try:
        sys.path.insert(0, str(repo_root))
        sys.path.insert(0, str(root / "registries"))
        from scripts.resolve_human_subjects_authority import validate_registry
        from build_registries import build_human_subjects, rendered
        payload = load_json(generated)
        if generated.read_text(encoding="utf-8") != rendered(build_human_subjects(core_path=repo_root / "shared/human_subjects_authority_registry.json", delta_path=root / "registries/human_subjects.delta.json")):
            return ["generated human-subjects registry is stale; rebuild registries"]
        validate_registry(payload)
        core = load_json(repo_root / "shared/human_subjects_authority_registry.json")
        prefix = core["registry_version"] + "-ro."
        if not payload.get("registry_version", "").startswith(prefix):
            return ["generated human-subjects registry version does not match current core registry"]
        delta = load_json(root / "registries/human_subjects.delta.json")
        rows, row_errors = load_rows(root)
        if row_errors:
            return ["legal_ro rows invalid: " + "; ".join(row_errors)]
        verified = {(r["source"]["url"], r["source"]["locator"]): r for r in rows}
        for profile in delta["profiles"]:
            for req in profile["requirements"]:
                anchor = req["authority_anchor"]
                row = verified.get((anchor["authority_url"], anchor["provision"]))
                if row is None:
                    return [f"delta requirement {req['requirement_id']} has no legal_ro.json anchor row"]
                if effective_use(row, date.today()) != "fact_check":
                    return [f"delta requirement {req['requirement_id']} anchor is not effective fact_check"]
    except Exception as exc:
        return [f"human-subjects registry: {exc}"]
    return []

def check_review_criteria_registry(root: Path, repo_root: Path) -> list[str]:
    generated = root / "registries/generated/review_criteria_registry.json"
    if not generated.exists():
        return []
    try:
        sys.path.insert(0, str(repo_root))
        sys.path.insert(0, str(root / "registries"))
        from scripts.resolve_review_target_context import validate_registry
        from build_registries import build_review_criteria, rendered
        payload = load_json(generated)
        core = load_json(repo_root / "shared/review_criteria_registry.json")
        prefix = core["registry_version"] + "-ro."
        if not payload.get("registry_version", "").startswith(prefix):
            return ["generated review-criteria registry version does not match current core registry"]
        fresh = rendered(build_review_criteria(core_path=repo_root / "shared/review_criteria_registry.json", delta_path=root / "registries/review_criteria.delta.json"))
        if generated.read_text(encoding="utf-8") != fresh:
            return ["generated review-criteria registry is stale; rebuild registries"]
        validate_registry(payload)
        if payload["criteria"][:len(core["criteria"])] != core["criteria"]:
            return ["generated review-criteria registry changed core criteria rows"]
        delta = load_json(root / "registries/review_criteria.delta.json")
        delta_errors = validate_json(delta, root / "schemas/review_criteria_delta.schema.json")
        if delta_errors:
            return ["review-criteria delta invalid: " + "; ".join(delta_errors)]
        rows, row_errors = load_rows(root)
        if row_errors:
            return ["data rows invalid: " + "; ".join(row_errors)]
        verified = {row["source"]["url"] for row in rows}
        for criterion in delta["criteria"]:
            if criterion["source"]["uri"] not in verified:
                return [f"criterion {criterion['criterion_id']} source is not backed by a data/ row"]
        manuscript_rows = [c for c in delta["criteria"] if c["criterion_id"].startswith("ro.manuscript-statements.")]
        if any(c["blocking_policy"] != "advisory_only" for c in manuscript_rows):
            return ["manuscript-statement criteria must use advisory_only blocking policy"]
        receipt_schema = load_json(repo_root / "shared/contracts/review_target/review_criteria_source_receipt.schema.json")
        receipt_validator = Draft202012Validator(receipt_schema, format_checker=FormatChecker())
        receipts = sorted((root / "registries/review_criteria_sources").glob("*.json"))
        if not receipts:
            return ["review-criteria source receipts are missing"]
        receipt_criterion_ids: set[str] = set()
        for receipt_path in receipts:
            receipt = load_json(receipt_path)
            receipt_errors = list(receipt_validator.iter_errors(receipt))
            if receipt_errors:
                return [f"source receipt {receipt_path.name} invalid: {receipt_errors[0].message}"]
            for locator in receipt.get("criterion_locators", []):
                receipt_criterion_ids.add(locator["criterion_id"])
                if not any(row["source"]["url"] == receipt["source_uri"] and row["source"]["locator"] == locator["locator"] and row["notes"] == locator["fragment"] for row in rows):
                    return [f"source receipt {receipt_path.name} has locator not backed by a data/ row"]
        missing_receipts = {criterion["criterion_id"] for criterion in delta["criteria"]} - receipt_criterion_ids
        if missing_receipts:
            return ["criteria missing source receipts: " + ", ".join(sorted(missing_receipts))]
    except Exception as exc:
        return [f"review-criteria registry: {exc}"]
    return []


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

    coverage_errors = check_verified_row_coverage(args.overlay_root, today)
    if coverage_errors:
        for error in coverage_errors:
            report("verified-row coverage", "FAIL", error)
        failures += 1
    else:
        report("verified-row coverage", "PASS", "all effective fact_check rows accounted for")

    hs_errors = check_human_subjects_registry(args.overlay_root, args.repo_root)
    if hs_errors:
        for error in hs_errors:
            report("human-subjects registry", "FAIL", error)
        failures += 1
    elif (args.overlay_root / "registries/generated/human_subjects_authority_registry.json").exists():
        report("human-subjects registry", "PASS", "valid, current and legally anchored")

    review_errors = check_review_criteria_registry(args.overlay_root, args.repo_root)
    if review_errors:
        for error in review_errors:
            report("review-criteria registry", "FAIL", error)
        failures += 1
    elif (args.overlay_root / "registries/generated/review_criteria_registry.json").exists():
        report("review-criteria registry", "PASS", "valid, current and backed by data rows")

    for label, present, reason in check_later_artifacts(args.overlay_root):
        if label == "profile/respiratory_medicine.json" and present:
            errors = check_profile(args.overlay_root, args.repo_root)
            if errors:
                for error in errors:
                    report(label, "FAIL", error)
                failures += 1
            else:
                report(label, "PASS", "valid and manifest digest matches")
        elif label in {"registries/generated/human_subjects_authority_registry.json", "registries/generated/review_criteria_registry.json"}:
            continue
        else:
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
