# Probe: a RO profile in an alternate human-subjects registry

Ticket: `.scratch/ro-respiratory-medicine/issues/15-probe-ro-human-subjects-alt-registry.md`. Base: `main` @ `e614b32`. No core file changed.

## Result: PASS, with no core edits needed

`research/probe/build_alt.py` creates the alternate registry. It copies `shared/human_subjects_authority_registry.json` and adds:
- `registry_id` `human-subjects-authority-ro-respiratory-overlay`, version `2026-08-09.1-ro.1`;
- fact `scope.ro_research_ethics`;
- three placeholder `ro.placeholder.ethics.*` sources (`source_language: ro`);
- profile `ro.placeholder.research-ethics` (`review_ethics`), cloned structurally from the TW profile, with the digest recomputed via `resolve_human_subjects_authority.digest`.

`eu.gdpr.research-core-bounded` stays unchanged on `data_protection`. The context is the `tw-gdpr-two-axis` fixture re-pointed to the RO profile.

| Step | Command | Result |
|---|---|---|
| Registry lint | `resolve_human_subjects_authority.py --registry alt --check-registry` | passed (#666) |
| Resolve | `... --context ro_context.json --output resolved.json` | `resolution_state: resolved`, all four downstream gates true, 8 requirement results |
| Replay | `... --check-resolved resolved.json` | passed |
| Negative | RO context against the core registry | rejected: `scope.ro_research_ethics` not in the fact catalog (as expected) |
| Pathway trace (#669) | `build_review_pathway_rule_trace.py build/validate` with alt registry | built, and replay passed |
| Packet manifest (#667) | `build_submission_packet_manifest.py build/validate` with alt registry | built, and validation passed |
| Core lints with the file placed at `overlays/ro-respiratory-medicine/registries/` | `check_spec_consistency`, `check_human_subjects_reference_migration`, `check_submission_packet_manifest_integration`, `check_669_review_pathway_rule_trace` | all exit 0, same as baseline |

The downstream artifacts bind by `registry_pointer` (id, version, digest), never by file path. The pathway trace and the packet manifest both carry the overlay pointer.

## Constraints found (they shape the generator)

1. Every `requirements[].authority_anchor.source_id` must be listed in its profile's `source_ids`. The anchor's `source_language` must match the source row, and anchor provisions must be within the source's `allowed_provisions`.
2. `profile_digest` = sha256 of the canonical JSON of the profile with the digest removed. A context pins the digest in `selected_profiles` and `display_precedence`, so every profile edit means re-pinning the user's context.
3. Any fact a context declares must exist in the registry's fact catalog. A RO context therefore cannot be resolved against the core registry. Activation must pass the overlay registry everywhere (resolve, trace, manifest).
4. The registry digest changes with every regeneration. Contexts and resolved artifacts made against an older generated copy will fail replay after an upstream registry bump. That's expected, but the activation docs must say so.

## Caveats

- Run with `/usr/bin/python3` 3.9.6, which is too old for `check_spec_consistency.py` (`ast.MatchAs`). The lints were run with `uv run --python 3.12 --with pyyaml --with jsonschema`.
- The RO content is a structural placeholder only. Its requirements are the TW requirements renamed, so no Romanian legal content was tested. The real profile content belongs to the ethics-gate decision.
- pytest suites were not run (core is unchanged).
