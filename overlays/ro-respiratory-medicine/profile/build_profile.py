#!/usr/bin/env python3
"""Build and seal the Romanian respiratory-medicine research profile."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
OVERLAY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.research_workflow_profile import canonical_bytes, seal_profile


def build() -> dict[str, object]:
    stages = (
        "rq_formation", "retrieval", "methodology", "synthesis", "drafting",
        "integrity_check", "review", "revision", "finalization",
    )
    profile: dict[str, object] = {
        "schema_version": "research-workflow-profile/1.0",
        "profile_id": "respiratory_medicine",
        "profile_version": "1.0.0",
        "research_family": "clinical_human_subjects",
        "declared_family_label": "Respiratory medicine (RO)",
        "display_name": {
            "en": "Respiratory medicine (Romania)",
            "zh_TW": "呼吸醫學（羅馬尼亞）",
        },
        "stage_map": {stage: {"state": "applicable"} for stage in stages},
        "alternative_categories": {
            "state": "declared",
            "categories": ["alternative_design", "alternative_measurement"],
        },
        "branch_budget": 3,
        "overflow_behavior": "ask_merge_park_archive",
        "evidence_overlays": [
            {"name": "Design add-ons", "pointer": "references/design_addons.md"},
            {"name": "Respiratory subdomains", "pointer": "references/subdomains/"},
            {"name": "RO/EU data sources", "pointer": "references/data_sources_ro_eu.md"},
            {"name": "Respiratory reviewer prompts", "pointer": "references/reviewer_prompts.md"},
        ],
        "authority_points": [
            {
                "task_family": "methodology",
                "authority": "EQUATOR reporting guideline routing (core) with overlay design add-ons",
                "requirement": "Core chooses the reporting guideline; for first-class designs apply the overlay design add-ons; never re-route.",
            },
            {
                "task_family": "retrieval",
                "authority": "RO/EU respiratory data-source list",
                "requirement": "Prefer the listed primary data sources and state their known limitations.",
            },
            {
                "task_family": "drafting",
                "authority": "Overlay subdomain references (edition-stamped)",
                "requirement": "Every guideline-defined definition, threshold or MCID cites its edition and source.",
            },
            {
                "task_family": "review",
                "authority": "Overlay respiratory reviewer prompts",
                "requirement": "Apply the respiratory reviewer prompts and Romanian manuscript-statement checks.",
            },
            {
                "task_family": "integrity_check",
                "authority": "Overlay evidence-tag rule",
                "requirement": "Only primary-tagged values are facts; secondary values are advisory and flagged for verification.",
            },
        ],
        "known_exclusions": ["doctoral theses", "Romanian-language output"],
        "unresolved_fit_note": "This profile is dormant until upstream #742 adds a consumer; the activation preamble carries its behaviour in the meantime.",
        "provenance": {
            "source": "user_authored",
            "source_pointer": "overlays/ro-respiratory-medicine/profile/respiratory_medicine.json",
            "freshness_state": "current",
            "last_reviewed_at": "2026-10-10",
        },
    }
    return seal_profile(profile)


def main() -> None:
    sealed = build()
    profile_path = OVERLAY_ROOT / "profile/respiratory_medicine.json"
    profile_path.write_bytes(canonical_bytes(sealed))
    manifest_path = OVERLAY_ROOT / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["profile_content_sha256"] = sealed["content_sha256"]
    manifest_path.write_bytes(canonical_bytes(manifest) + b"\n")


if __name__ == "__main__":
    main()
