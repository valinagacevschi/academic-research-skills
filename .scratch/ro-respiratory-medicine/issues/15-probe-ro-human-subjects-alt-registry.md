# Probe a RO profile in an alternate human-subjects registry

Type: task (AFK)
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 06
Map: ../map.md

## Question

Does an alternate human-subjects authority registry work end to end without core edits? The registry should be a full copy of `shared/human_subjects_authority_registry.json` with `eu.gdpr.research-core-bounded` kept on the `data_protection` axis and a new placeholder RO `review_ethics` profile added. Check that it passes `scripts/resolve_human_subjects_authority.py --check-registry`, resolves a context for a Romanian observational study, and isn't rejected by any runtime binder (submission-packet manifest, review-pathway trace) for not being the core path. Work on a throwaway `research/ro-hs-alt-registry` branch or worktree, and don't change core. Record: pass or fail, the exact commands and outputs, and any binder or lint that hard-codes the core path in a way that matters at runtime. If it fails, the fallback from [Overlay mechanism decision](06-overlay-mechanism.md) applies: ship only the review-criteria copy and keep the ethics content in the preamble.

## Answer

**Pass. The fallback isn't needed, and the human-subjects half of [Overlay mechanism decision](06-overlay-mechanism.md) stands.**

- A full-copy registry with its own `registry_id`, a new `scope.ro_research_ethics` fact, `ro`-language sources and a placeholder RO `review_ethics` profile passes `--check-registry`. A Romanian context (RO ethics + EU GDPR) resolves with every downstream gate true and replays cleanly.
- The review-pathway trace (#669) and submission-packet manifest (#667) both build and validate against the overlay registry. Downstream artifacts bind by `registry_pointer` (id, version, digest), never by file path.
- The lints that hard-code the core path only check the core file. With the overlay registry placed under `overlays/ro-respiratory-medicine/registries/`, all four core lints still pass, the same as baseline.
- Constraints the generator must respect:
  - each requirement's anchor source must be one of the profile's `source_ids`, with matching `source_language` and permitted provisions;
  - `profile_digest` is recomputed on every edit, and contexts pin it;
  - a RO context can't be resolved against the core registry, so activation must pass the overlay registry to resolve, trace and manifest;
  - every upstream bump changes the registry digest, so older contexts and resolved artifacts fail replay.
- Not tested: real Romanian legal content (the placeholder reuses TW requirements). That content belongs to [Romanian ethics-gate behaviour](09-romanian-ethics-gate.md).
- Environment: `/usr/bin/python3` is 3.9.6, which is too old for `check_spec_consistency.py`; use `uv run --python 3.12 --with pyyaml --with jsonschema`.

Findings: branch `research/ro-hs-alt-registry` (commit `8bcc048`), file `research/ro-hs-alt-registry.md`, probe scripts in `research/probe/` (worktree `/Users/val/dev/ars-research/ro-hs-alt-registry`).
