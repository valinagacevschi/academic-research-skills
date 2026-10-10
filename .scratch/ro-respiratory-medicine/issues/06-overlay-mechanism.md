# Overlay mechanism decision

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 03
Map: ../map.md

## Question

Given what the upstream extension points allow today, how should the overlay be delivered now that output is English-only (no locale pack needed)? Covers: shipping full registry copies via `--registry` vs contributing entries upstream; how users activate the overlay (paths, a wrapper command, docs); and what to do about the `respiratory_medicine` profile while no stage consumes profiles (upstream #742).

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved).

- **Term.** It's an **overlay**, not a "locale pack" (see [GLOSSARY](../GLOSSARY.md)). It never uses `locales/`, which upstream reserves for the Phase-2 loader.
- **Location.** A top-level folder in this fork, `overlays/ro-respiratory-medicine/`. It only adds files, so upstream merges never conflict with it, and validators and tests run against the same checkout. Rejected: a sibling repo (splits CI and pinning) and `locales/ro/`.
- **Registries.** Each registry ships as a **delta** (rows added on top of upstream) plus a generator. The generator merges the delta into the current upstream `shared/human_subjects_authority_registry.json` and `shared/review_criteria_registry.json`, seals the result, and writes full copies that are passed via `--registry`. The delta is the source of truth, and the generated copies are pinned to upstream's `registry_version`. Generic, non-Romanian rows (e.g. an ERS/ATS `field_society_standard` row) are also listed as **upstream asks**, a separate track that doesn't block the overlay.
- **Activation.** An activation preamble (`ACTIVATE.md`) that the user adds to their project instructions (AGENTS.md/CLAUDE.md), plus a small install script that writes it there. It names the generated registry paths, the profile path, the venue/format profile templates, and the English-only output rule. Rejected: a wrapper skill (adds a `SKILL.md` right on the overlay boundary and competes for triggers) and docs only (too easy to get wrong).
- **Profile while #742 is open.** Ship `respiratory_medicine` sealed and validated (family `clinical_human_subjects`, `user_authored`, `declared_family_label`) but **dormant**. Activation produces a `select` receipt, and the preamble carries the behaviour the profile implies. Once #742 adds a consumer, the matching preamble text is removed. Offering the profile upstream as the first shipped clinical profile is an upstream ask.
- **Tracking upstream.** A manifest records `upstream_commit`, both `registry_version`s and the profile digest. A `check_overlay` script validates the profile, runs `--check-registry` on both generated copies, and checks for drift. It runs in fork CI and locally after every upstream merge, and a failure stops merges until the delta is regenerated. Upstream's locale-pack ownership policy (two owners, staleness checks) applies only if we ever seek "supported" listing, which we aren't.
- **Condition.** The human-subjects half depends on an untested probe, now [Probe a RO profile in an alternate human-subjects registry](15-probe-ro-human-subjects-alt-registry.md). If the probe fails, the fallback is to ship only the review-criteria copy and keep the Romanian ethics content in the preamble.

Supporting fact checked this session: both resolvers accept `--registry` (`scripts/resolve_review_target_context.py:656-661`, `scripts/resolve_human_subjects_authority.py:1113`). Only the lints hard-code the core path (`scripts/check_human_subjects_reference_migration.py:27`, `scripts/check_submission_packet_manifest_integration.py:15`, `scripts/check_669_review_pathway_rule_trace.py:19`).
