#!/usr/bin/env python3
"""Render evidence-backed overlay references from data rows."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from check_overlay import effective_use, load_rows  # noqa: E402

SUBDOMAINS = {
    "airways": "Airways", "ild": "Interstitial lung disease", "pulmonary_vascular": "Pulmonary vascular",
    "sleep": "Sleep", "thoracic_oncology": "Thoracic oncology", "infection_and_other": "Infection and other",
}
VENUES = {
    "venue.rjme": "Romanian Journal of Morphology and Embryology", "venue.ers_congress": "ERS International Congress",
    "venue.srp_congress": "SRP Congress", "venue.medicina": "Medicina", "venue.maedica": "Maedica",
    "venue.ijtld": "International Journal of Tuberculosis and Lung Disease", "venue.pneumologia": "Pneumologia",
    "venue.ers_journals": "ERS journals", "venue.ajrccm": "AJRCCM", "venue.chest": "CHEST",
    "venue.thorax": "Thorax", "venue.respiratory_medicine": "Respiratory Medicine",
}
MISSING_VENUES: list[str] = []


def esc(value: object) -> str:
    return str(value if value is not None else "—").replace("|", "\\|").replace("\n", " ")


def table(rows: list[dict], today: date) -> str:
    out = ["| Value | Edition | Tag | Verified | Source |", "|---|---|---|---|---|"]
    for row in rows:
        use = effective_use(row, today)
        value = row["statement"]
        if use == "advisory":
            value += " **Verify:** advisory; confirm before use."
        source = f"[{row['source']['title']}]({row['source']['url']}) ({row['source']['locator']}) · `{row['value_id']}`"
        out.append("| " + " | ".join(map(esc, [value, row["edition"], row["evidence_tag"], row["verified_at"], source])) + " |")
    return "\n".join(out)


def render(today: date | None = None) -> dict[Path, str]:
    today = today or date.today()
    rows, errors = load_rows(ROOT)
    if errors:
        raise ValueError("Invalid data rows: " + "; ".join(errors))
    files: dict[Path, str] = {}
    for key, title in SUBDOMAINS.items():
        grouped: dict[str, list[dict]] = {}
        for row in rows:
            area_root = row["area"].split(".")[0]
            if area_root == key or (key == "infection_and_other" and area_root == "infection"):
                grouped.setdefault(row["area"], []).append(row)
        body = [f"# {title} subdomain reference", "", "Applies to every study design. Core ARS selects the reporting guideline; this reference adds subdomain content after that choice.", ""]
        for topic, items in grouped.items():
            body.extend([f"## {topic}", "", table(items, today), ""])
        files[Path("references/subdomains") / f"{key}.md"] = "\n".join(body).rstrip() + "\n"
    for data_name, output, header in [
        ("data_sources.json", "references/data_sources_ro_eu.md", "# Romanian and European data sources"),
        ("citations.json", "references/citations_ro.md", "# Romanian citation notes"),
    ]:
        selected = [r for r in rows if ("data." in r["value_id"] if data_name == "data_sources.json" else r["value_id"].startswith("citation."))]
        groups: dict[str, list[dict]] = {}
        for row in selected: groups.setdefault(row["area"], []).append(row)
        body = [header, ""]
        for topic, items in groups.items(): body.extend([f"## {topic}", "", table(items, today), ""])
        if data_name == "citations.json":
            body += ["## Fixed style decisions", "", "- Generated text uses comma-below ș/ț (U+0218–U+021B); quoted reference data keeps the publisher's characters, including cedilla where present.", "- Use English MeSH keywords.", "- Use the Vancouver variant stated in the confirmed venue notes.", ""]
        files[Path(output)] = "\n".join(body).rstrip() + "\n"
    venues = [r for r in rows if r["value_id"].startswith("venue.")]
    grouped = {}
    for row in venues: grouped.setdefault(row["area"], []).append(row)
    body = ["# Venue notes", ""]
    for area, name in VENUES.items():
        items = grouped.get(area, [])
        body += [f"## {name}", "", "What the overlay found; check the current author instructions. Declare only the values you confirm.", ""]
        if items: body += [table(items, today), ""]
        else: body += ["not verified (publisher site blocked automated access); check the author instructions", ""]
        if area == "venue.medicina": body += ["AI-disclosure placement is advisory text for the author; verify current instructions before declaring it.", ""]
        if area == "venue.maedica": body += ["The stated ≤30% AI rule has no defined metric. Never claim compliance.", ""]
    files[Path("references/venue_notes.md")] = "\n".join(body).rstrip() + "\n"
    # methodology rows are the generated evidence appendix inside the hand-written add-ons file.
    method = [r for r in rows if r["area"].startswith("methodology")]
    files[Path("references/design_methodology_evidence.md")] = "# Measurement and reporting standards evidence\n\n" + table(method, today) + "\n"
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--today", help="Override date for deterministic freshness checks")
    args = parser.parse_args()
    try: rendered = render(date.fromisoformat(args.today) if args.today else None)
    except (ValueError, KeyError) as exc:
        print(f"render error: {exc}", file=sys.stderr); return 1
    failures = []
    for rel, content in rendered.items():
        path = ROOT / rel
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content: failures.append(str(rel))
        else:
            path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content, encoding="utf-8")
    if failures:
        print("Rendered references differ: " + ", ".join(failures), file=sys.stderr); return 1
    print("Reference render is current." if args.check else f"Rendered {len(rendered)} files.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
