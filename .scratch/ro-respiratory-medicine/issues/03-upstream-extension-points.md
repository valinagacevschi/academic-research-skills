# Upstream ARS extension points for an overlay

Type: research
Status: resolved
Map: ../map.md

## Question

Exactly what can a locale pack and field profile add to ARS without core edits, and what is missing today? Investigate this repo: `shared/output_language_pair.md` (registry, overlay boundary, Phase-2 loader status, issue #862), `shared/research_workflow_profiles/` (schema, how profiles are selected and consumed), `shared/human_subjects_authority_registry.json` (profiles/overlays), `shared/review_criteria_registry.json` (authority classes), `academic-paper/references/abstract_writing_guide.md` regime table, and `scripts/check_spec_consistency.py`. Also check upstream GitHub issues and PRs for locale-pack / Phase-2 plans. Output: a list of extension points with file:line pointers, which ones are config-only, and what would need core changes or an upstream loader.

## Answer

- **`ro-en` language pair is blocked on upstream.** There is no `locales/` folder and no loader (Phase 2 is unscheduled; only maintainer comments on #850/#862). The validator rejects `ro-en`, and Schema 4 has no abstract keys for a non-Chinese first language, so a core or schema change is needed.
- **Field profile:** a `respiratory_medicine` profile in family `clinical_human_subjects` validates today, but no pipeline stage consumes profiles yet (#742 open). A Romanian display name and a new family name are both rejected.
- **Human-subjects and review-criteria registries:** the overlay can ship a *full copy* passed via `--registry`; neither registry can be layered on the core file. Review-criteria authority classes are closed (adding a row works, adding a class doesn't).
- **Config-only today:** venue profile (abstract and keyword limits, overrides the regime table), format profile, Vancouver style.
- **Needs core changes:** Romanian trigger phrases (they live in `SKILL.md` descriptions), the `clinical` domain evidence profile, formatter abstract limits and fonts, the glossary hook.
- **Not yet tested:** a `ro.*` profile run through the human-subjects resolver from a separate registry file.

Findings: branch `research/upstream-extension-points` (commit `4840f6a`), file `research/upstream-extension-points.md` (worktree `/Users/val/dev/ars-research/upstream-extension-points`).
