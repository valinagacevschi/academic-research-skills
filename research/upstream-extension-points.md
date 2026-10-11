# Upstream ARS extension points for a ro / respiratory-medicine overlay

Ticket: `.scratch/ro-respiratory-medicine/issues/03-upstream-extension-points.md` (primary tree, untracked).
Repo state examined: `main` @ `e614b32` (post v3.23.0). Upstream: `Imbad0202/academic-research-skills`, read via `gh` on 2026-10-10.
All `file:line` pointers are relative to the repo root at that commit. "Probe" = a throwaway local run against the shipped validators (outputs quoted; nothing committed except this note).

## Answer summary

- **There is no locale loader today.** `locales/` does not exist; the output-language-pair contract is Phase 1 only and says pack-supplied registry entries and regime rows "ship with the Phase-2 loader" (`shared/output_language_pair.md:3-5`, `:37-42`, `:98`). No upstream issue or PR for Phase 2 exists; the only plan of record is maintainer comments on #850 and #862 (Q5: "Pack-supplied registry entries are Phase 2 work, together with the loader that would read them").
- **So a `ro` locale pack cannot add a language pair without a core edit.** A `ro-en` (or `en-ro`) token is rejected as "unsupported" by the shipped registry (probe below). Adding the row to `shared/output_language_pair.md` parses fine, but that file is core. And there are no Schema-4 keys for a non-zh-TW L1: the legacy keys `abstract: {english, chinese}` / `keywords: {en, zh_tw}` are the only ones, and pairing them with a non-default L1 is a declared visible failure (`shared/output_language_pair.md:127-132`).
- **The field profile is the most overlay-friendly surface, with limits.** `scripts/research_workflow_profile.py select --profile <any path>` accepts an external `user_authored` profile. A `respiratory_medicine` profile under `research_family: clinical_human_subjects` with a `declared_family_label` validated and produced a selection receipt (probe). Limits:
  - `research_family` is a closed 8-value enum.
  - `display_name` is closed to `{en, zh_TW}`, so a `ro` name is rejected.
  - Only `user_authored` may carry a family label.
  - **No pipeline stage consumes the profile yet** ("This does not add a pipeline hook", design doc `:13`).
- **The two JSON registries (human-subjects authority, review criteria) take an explicit `--registry` path**, so an overlay can ship a *whole alternate registry file* without touching core. Agents and docs, however, name the core path (`shared/human_subjects_authority_registry.json`, `shared/review_criteria_registry.json`). The registries are single-file: there is no merge or layering, and the review-criteria authority classes are a closed enum. In practice the overlay ships a fork-copy of each registry plus run-time instructions to pass that path.
- **Config-only today, no core edit:**
  - per-run, scholar-declared venue profile (abstract limit, keyword range, and so on; it takes precedence over the regime table);
  - format profile;
  - Vancouver citation style (already the Medicine default);
  - user-authored workflow profile;
  - alternate registry files passed by path.
- **Needs core or an upstream loader:**
  - the language pair and its regime rows;
  - Schema-4 keys for non-zh-TW L1;
  - trigger phrases (they live in `SKILL.md` descriptions, which have a 1,024-code-point cap);
  - a `clinical` domain evidence profile (reserved, not shipped);
  - `ro` display names;
  - new research families or authority classes;
  - auto-discovery or merging of pack-supplied registry entries;
  - the formatter's abstract limit and its CJK/font logic.

## Extension points table

| # | Extension point | Where | What an overlay can add | Config-only today? | What's missing / needs |
|---|---|---|---|---|---|
| 1 | Output-language-pair registry | `shared/output_language_pair.md:20-24` (marked block), lint `scripts/check_spec_consistency.py:1339-1400`, `:1761-1905` | A pair entry such as `ro-en` (token grammar `^[a-z]{2,3}(?:-[a-z0-9]{2,4}){1,3}$`, `:1299`) | **No.** The only registry is the core file. Pack entries need the Phase-2 `locales/<locale>/` loader (`:37-42`, `:98`) | Upstream Phase-2 loader. Today: a fork edit of the core file, which breaks the overlay rule |
| 2 | Abstract length/keyword regime rows | `academic-paper/references/abstract_writing_guide.md:19-26`; lint requires the 4 rows and columns (`check_spec_consistency.py:1306-1312`) and forbids a copy in the contract (`:1810`) | Per-pair rows for Romanian | **No.** "a pack-supplied entry ships its own regime rows with the Phase-2 registry loader" (`abstract_writing_guide.md:57-62`) | Phase-2 loader. **Workaround that is config-only:** the venue profile, which takes precedence (`:32-33`) |
| 3 | Schema-4 abstract/keyword keys for non-default L1 | `shared/handoff_schemas.md:237`; conflict rule `shared/output_language_pair.md:127-132` | n/a | **No** | A core schema change (packs may not overlay schemas: `CONTRIBUTING.md:72`) |
| 4 | Intake abstract cardinality (Bilingual / EN only / zh-TW only) | `academic-paper/agents/intake_agent.md:207-213` | "EN only" is usable as-is | Partially: EN-only works. A ro-only or ro+en abstract has no option | Core intake change (agent definition) |
| 5 | Research workflow (field) profile | schema `shared/contracts/research_workflow/research_workflow_profile.schema.json`; runtime `scripts/research_workflow_profile.py`; shipped fallback `shared/research_workflow_profiles/field_general.json` | A `respiratory_medicine` profile JSON (canonical bytes + `content_sha256`), passed with `--profile <path>` | **Yes** for authoring, validation and selection (probe PASS) | Closed `research_family` enum (`schema:141-152`; `.py:57-66`). `display_name` closed to en/zh_TW (`schema:30-38`). No profile directory or discovery: only `field_general` is a known path (`.py:24-26`). **No pipeline consumer** (design doc `dev/design/2026-08-17-742-...md:10-14`). #742 still OPEN |
| 6 | Human-subjects authority registry: profiles, overlays, facts | `shared/human_subjects_authority_registry.json` (facts `:8+`, profiles `:252+`, `overlays: []` at `:1277`); schema `shared/contracts/human_subjects/authority_profile_registry.schema.json`; resolver `scripts/resolve_human_subjects_authority.py:1113` (`--registry` required) | A RO `review_ethics` profile, institutional overlays (`overlay_kind: institutional|funder`, schema `:475`), new `fact_definitions` (e.g. `scope.ro_*`), `ro` sources (`source_language` pattern allows `ro`, schema `:224`) | **Yes, as a separate full registry file** passed by `--registry` | Single-file registry, no merge. Agents name the core path (`deep-research/SKILL.md:600`, `deep-research/agents/ethics_review_agent.md:166`, `deep-research/agents/research_architect_agent.md:108`). The axis enum is closed to `review_ethics`/`data_protection` (schema `:62`). The resolver needs base profiles on both axes in the same file (`shared/references/human_subjects_authority_protocol.md:163`), so the alt file must also carry `eu.gdpr.research-core-bounded`. Untested probe (see uncertainties) |
| 7 | Review-criteria registry | `shared/review_criteria_registry.json:6-24`; resolver `scripts/resolve_review_target_context.py:20-26`, `:656-661` (`--registry`, defaults to core) | Rows in the 4 existing classes, e.g. a `reporting_design_overlay` for STROBE/CONSORT, a `field_society_standard` row (ERS/ATS), or an `official_venue_type` row for a Romanian journal | **Yes, as a separate full registry file** (probe: copy + added row validates) | `authority_classes` closed to 4 (`resolve_review_target_context.py:20-25`; probe rejects a 5th). `dimension` closed to 3 (`:26`). The consumer protocol examples pin the core path (`shared/references/review_criteria_consumer_protocol.md:32-33`). Sources need verification receipts like `shared/review_criteria_sources/*` (convention per `shared/contracts/README.md:902-915`) |
| 8 | Venue profile (#394) | `academic-paper/agents/intake_agent.md:170-177`; `shared/contracts/submission/venue_profile.schema.json` | Per-run abstract word limit, keyword range, required sections, reference limit | **Yes (per run)** | `declared_by` is const `scholar` (schema `:109-112`) and intake must never prefill from a journal name (`intake_agent.md:174`). A pack may ship *templates/examples* but not pre-declared values. Treat that as policy-sensitive |
| 9 | Format profile (#439) | `intake_agent.md:197-203`; `shared/contracts/submission/format_profile.schema.json` | Fonts, spacing, margins | **Yes (per run)** | Same "declared values only" rule (`:201`) |
| 10 | Citation style | `intake_agent.md:180-188` | Vancouver is already the Medicine default | **Yes** (no change needed) | The citation-guide *mapping* per locale is a Phase-2 pack asset (`CONTRIBUTING.md:72`; #850 answer 2) |
| 11 | Domain evidence profile (#259) | `academic-paper/references/domain_evidence_profiles.md:7-18`; lint `scripts/check_domain_evidence_profile.py:22-23` | n/a | **No.** The enum has 4 values. `clinical` is *reserved*, and selecting it falls back to `unknown_user_defined` (`:16-18`, `:30-34`) | A core change to ship `clinical` (upstream) |
| 12 | Trigger phrases (ro activation) | SKILL.md frontmatter `description`; rules in `CONTRIBUTING.md:64`, `:73` | Conservative ro phrases | **No.** They live in core `SKILL.md`. The maintainer says Phase 2 needs "a per-language trigger budget or a routing layer that does not live in the description" (#850 comment 5650299654) | Upstream routing layer, or a core edit under the #509 rules |
| 13 | L1 terminology glossary | `academic-paper/agents/abstract_bilingual_agent.md:102` (`references/hei_domain_glossary.md`, default zh) | A ro respiratory glossary | **No wiring.** The agent names the zh glossary only | Phase-2 pack asset or loader |
| 14 | Formatter abstract limit / fonts | `academic-paper/agents/formatter_agent.md:790` (recorded exception, `shared/output_language_pair.md:61-64`) | n/a | **No** | Deferred upstream ("keep the formatter untouched", #862 comment 5658585469) |

## Findings with pointers

### F1. Output-language pair: Phase 1 only, overlay boundary is explicit
- Status line: "Phase 2 adds the registry loader, locale packs (`locales/<locale>/`), and pack-supplied regime rows" (`shared/output_language_pair.md:3-5`).
- Registry has one row, `zh-tw-en`, status `default` (`:20-24`). Two-language entries only; unary tokens fail visibly (`:26-28`).
- Overlay boundary (`:35-42`): packs contribute registry entries "as configuration — nothing else", and MUST NOT overlay `SKILL.md`, agents, IRON RULEs, integrity protocols, schemas, modes, or oversight rules. This matches `CONTRIBUTING.md:72`.
- Any value not in the registry aborts and names the registry; there is no fallback (`:79-80`). The lint enforces this: `check_spec_consistency.py:1407-1437`, default must be exactly `zh-tw-en` (`:1245`, `:1836-1840`), and 11 consumer surfaces are scanned for unregistered backticked tokens (`:1844-1886`). Overlay docs that sit *outside* those 11 surfaces are not scanned (inferred from the surface list; not exhaustively verified).
- **Probe:** with a `ro-en` row added in memory, the core parser accepts it (`['ro-en','zh-tw-en']`). Against the shipped file, `validate_output_language_pair("ro-en")` returns `unsupported token 'ro-en' (registry holds: zh-tw-en)`.
- Conflict rule: a non-zh-TW L1 cannot use the legacy keys (`:127-132`). No alternative keys exist in Schema 4 (`shared/handoff_schemas.md:237`), so even a loader would need a schema change for ro-L1 output.

### F2. Regime table: single source, default pair only
- Marked block `abstract_writing_guide.md:19-26`. Required rows: standard, conference, extended_abstract, dissertation. Required columns: paper_type, l1_abstract, l2_abstract, keywords_per_language (`check_spec_consistency.py:1306-1312`).
- "Phase 1 carries the regime rows for the default entry only; a pack-supplied entry ships its own regime rows with the Phase-2 registry loader" (`:57-62`).
- A venue-declared limit (#394) "takes precedence over the table" (`:32-33`; repeated in `abstract_bilingual_agent.md:45`, `:78`). This is the only config-only way to get journal-specific abstract figures today.

### F3. Research workflow profiles: validated, selectable, not consumed
- Schema is closed (`additionalProperties:false`, `research_workflow_profile.schema.json:7`). The required fields are at `:8-23`. Family enum `:141-152`. `display_name` `{en, zh_TW}` only (`:30-38`). Optional `evidence_overlays` holds pointers only (`:79-91`). A non-`field_general` family requires ≥1 authority point (`:116-121`). `declared_family_label` ⇒ `user_authored` (`:122-132`).
- Runtime: `load_profile` requires canonical JSON bytes plus a matching digest (`scripts/research_workflow_profile.py:536-541`). `select --profile` takes any path (`:987-991`, `:968-973`). `fallback_automatic` binds only the shipped `field_general` (`:747-754`). `validate_profile_catalog` refuses two contents under one id@version (`:566-579`).
- **Probe:** a sealed `respiratory_medicine` profile (`clinical_human_subjects`, `user_authored`, label "Respiratory medicine (RO)", 1 authority point) gave `PASS: valid research-workflow-profile/1.0 profile`, and `select ... --selected-by user_explicit` emitted a receipt. The negative probes were rejected:
  - `display_name.ro`: "undeclared field(s): ro";
  - `research_family: respiratory_medicine`: "must be one of: …";
  - `shipped_default` with a label: "lawful only when provenance.source is user_authored".
- Consumption: the design doc says the implementation "does not add a pipeline hook or change a default" (`dev/design/2026-08-17-742-research-family-profile-contract-design.md:10-14`). The only code importer is `scripts/inquiry_branch_ledger.py:66-80` (#743, opt-in). No `SKILL.md` or agent references the profile (grep). The enum widens "by ordinary contract versioning when a family earns its own shipped profile" (`:103-108`). #742 is OPEN, and its default-on change is gated on usability evidence.

### F4. Human-subjects authority registry: data-driven, single-file, explicit path
- Two axes only: `review_ethics`, `data_protection`. Funder and institutional requirements are overlays, never axes (`shared/references/human_subjects_authority_protocol.md:21-23`; schema `:62`).
- Never infer selection "from locale, language, affiliation…" (`:49-50`). Profiles and overlays are pinned by id/version/digest, and there is no "latest" (`:52-54`).
- Overlays: `add|supplement|conflict`, `requirements_removed` const false, target profiles pinned exactly; they cannot fill an unresolved axis (`:131-140`; schema `:475-487`). The shipped `overlays` array is empty (`registry.json:1277`).
- The resolver reads only the explicitly supplied files (`:158`, `resolve_human_subjects_authority.py:1113`). That makes an alternate registry file possible, but agent prose names the core path (pointers in the table). Profiles carry `profile_digest`, which is recomputed (`resolve_human_subjects_authority.py:648-652`).
- Lints and tests key on the core file: `check_human_subjects_reference_migration.py:27`, `:38`, `check_submission_packet_manifest_integration.py:15`, `test_resolve_human_subjects_authority.py:34`. The requirement-id doc scanner only recognises `us.45cfr46.|tw.hsra.|eu.gdpr.article-` (`check_human_subjects_reference_migration.py:102-107`), so a `ro.*` requirement id would not be cross-checked in docs. Inferred; effect not tested.
- For Romania, the existing `eu.gdpr.research-core-bounded` covers `data_protection`. A RO national `review_ethics` profile would be new data.

### F5. Review-criteria registry: closed classes, path-parameterised
- Classes: `official_venue_type`, `field_society_standard`, `reporting_design_overlay`, `broad_field_fallback` (`shared/review_criteria_registry.json:6-24`; enforced at `resolve_review_target_context.py:20-25`, `:279-291`, `:368-376`). Dimensions: `scientific_validity`, `venue_fit`, `submission_readiness` (`:26`).
- `--registry` defaults to the core file (`:656-661`). The consumer protocol binds "the exact criteria registry named by that context" (`review_criteria_consumer_protocol.md:23`), so a context resolved against an overlay registry carries that registry's pointer and digest.
- **Probe:** a deep copy of the live registry plus one `reporting_design_overlay` row (Respiratory Medicine / STROBE) passes `validate_registry`. Adding a `national_regulator` class is rejected ("undeclared field(s)").
- The live test asserts broad rows point at `repository://academic-paper-reviewer/references/review_criteria_framework.md` (`test_resolve_review_target_context.py:99-118`). An overlay copy should keep those four rows verbatim.
- Epic #575 is OPEN. Its invariants say stale, inferred, or model-recalled criteria are advisory-only, and that venue, discipline and overlay are independent axes.

### F6. Other per-run declared inputs (config-only)
- Venue profile: `intake_agent.md:170-177`; scholar-only provenance (`venue_profile.schema.json:109-112`). Format profile: `:197-203`. Both are "write nothing when declined" (Invariant 7).
- Citation: Vancouver is the default for Medicine (`intake_agent.md:186`).

### F7. Domain evidence profiles: `clinical` reserved
- Ship enum `general_social_science | cs_ml | humanities_interpretive | unknown_user_defined`. `clinical` is reserved and falls back to `unknown_user_defined` (`domain_evidence_profiles.md:7-18`). Medicine/Health hierarchy notes are preserved but non-normative (`:30-34`). Pinned by `check_domain_evidence_profile.py:22-23`.

### F8. Upstream plan of record (gh, read-only)
- **#850** (CLOSED 2026-09-13), maintainer answer (comment 5650299654):
  - per-run field first; install-time default later;
  - `locales/<locale>/` overlay accepted for "configuration and presentation assets only (trigger phrases, the language pair, citation-guide mapping, example sets, fonts)";
  - generated per-locale SKILL.md variants rejected;
  - description caps mean "Phase 2 needs a per-language trigger budget or a routing layer that does not live in the description";
  - citation mapping, examples and fonts deferred.
- **#862** (OPEN), the Phase-1 design home. Maintainer comment 5658585469:
  - Q5: "the core contract owns validation and the default entry. Pack-supplied registry entries are Phase 2 work, together with the loader that would read them";
  - the formatter stays untouched;
  - "Part B stays here for Phase 2".
- **PR #869** merged 2026-09-16 (`774d6c5a41`), shipped in v3.22.0.
- Comment 5970303879 (2026-10-03) opens the es-ES backup-owner window 2026-10-03 to 2026-10-17. Only es-ES has an ownership record.
- **PRs #861 and #863** (merged): locale-pack policy in `CONTRIBUTING.md:60-75`. It requires:
  - two named owners in the pack manifest;
  - recorded currency;
  - CI-visible staleness;
  - config/presentation only;
  - #509 trigger discipline.
- Searches for "Phase 2 loader", "locales/", "locale pack", "research_workflow_profile", "clinical profile", "authority overlay", "Romanian" and "respiratory" returned no Phase-2 loader issue or PR and nothing ro- or respiratory-specific (searched both issues and PRs).
- **#742** and **#575** remain OPEN epics; #666 and #683 are closed.

## Open uncertainties

- **Phase-2 shape is undesigned upstream.** Several things are only named, not specified: the manifest format, how a loader merges pack entries with the core registry, and whether the lint scans `locales/`. Any overlay layout we pick may not match what upstream builds.
- **Human-subjects alt-registry probe not run.** I did not build a RO profile and resolve a context against an alternate registry. Field shapes are confirmed only from the schema and protocol. Before relying on it, test that an alt file carrying the EU GDPR profile plus a RO profile passes `--check-registry`.
- **Effect of a non-core registry on bound consumers is unverified.** The submission-packet manifest and review-pathway trace may record or require the core registry pointer (`check_submission_packet_manifest_integration.py:15` hard-codes it, but that is a lint, not a runtime gate). I have not checked whether runtime binders reject a non-core path.
- **No consumer hook for the field profile.** Even a valid `respiratory_medicine` profile currently changes no agent behaviour. Any "respiratory_medicine field profile" effect in the overlay would have to come from user-facing instructions, not ARS runtime. That is a fact about today; upstream may add consumers under #743/#744/#745.
- **Venue-profile templates.** Whether shipping example venue profiles for Romanian journals fits the "scholar-declared only" rule is a policy judgement. The schema permits any file with `declared_by: scholar`, but intake forbids inferring from a journal name.
- **Ownership policy fit.** A `ro` pack under the upstream policy needs two owners. If the overlay stays in a fork or sibling repo, the policy applies only if we seek "supported" listing.

## Implications for the overlay

1. **Ship without core edits now:**
   - `locales/ro/` (or a sibling dir) holding a `user_authored` `respiratory_medicine` workflow profile (family `clinical_human_subjects`, `declared_family_label`, real authority points, en/zh_TW display names with the `ro` name only in pack docs), sealed with `seal_profile`;
   - an alternate review-criteria registry: a full copy of the core file plus respiratory reporting/venue rows with source receipts;
   - an alternate human-subjects registry: a copy plus a RO `review_ethics` profile and any institutional overlays;
   - venue- and format-profile *examples* and instructions;
   - a manifest recording the upstream commit (`e614b32`) and validation commands.
2. **Treat the language pair as blocked on upstream.** Use abstract cardinality "EN only" plus venue profiles for limits. Do not add `ro-en` to `shared/output_language_pair.md` in the fork: it violates the no-core-edit rule and would conflict with the Phase-2 loader. File or join upstream Phase-2 discussion on #862 instead.
3. **Copy-registries drift.** Pin the copied registries to the upstream `registry_version` and add a sync check, because there is no merge layer and upstream rotates digests on each registry release (`shared/contracts/README.md:914-915`).
4. **Record as upstream asks (not overlay work):**
   - Phase-2 loader for pair and regime rows, plus Schema-4 keys for non-zh-TW L1;
   - `ro` (or open-locale) `display_name` in the workflow-profile schema;
   - shipping the reserved `clinical` domain evidence profile;
   - registry layering (core plus pack files) for both JSON registries;
   - a trigger routing layer outside `description`.
