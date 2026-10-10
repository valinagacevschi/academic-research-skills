# Upstream asks from the Romanian respiratory-medicine overlay

Status: **drafts only. Do not file without Val's approval.** Target repo: `Imbad0202/academic-research-skills`. Baseline: `main` @ `e614b32` (v3.23.0).

These are changes that would help the overlay but belong in core ARS (see **Upstream ask** in [GLOSSARY.md](GLOSSARY.md)). The overlay works without any of them. Each one, if accepted, lets the overlay delete a workaround. Each draft below has a title, the problem, the proposal and the overlay workaround it would retire. Before filing, link related open threads: #742 (research-family profiles), #862 (locale Phase 1/2), #575 (review-target criteria).

---

## 1. Registry layering for the human-subjects and review-criteria registries

**Problem.** Both registries are single files. `scripts/resolve_human_subjects_authority.py` and `scripts/resolve_review_target_context.py` accept `--registry`, but an addition can only be shipped as a full copy of the core file. A downstream overlay has to regenerate that copy, and re-pin user contexts, on every upstream registry release.

**Proposal.** Allow a resolver to take the core registry plus one or more addition files, with these rules:
- additions only;
- no overriding a core row;
- a combined `registry_pointer` whose digest covers every input.

This matches the "pack-supplied registry entries" path that #862 defers to Phase 2.

**Retires.** `registries/build_registries.py` and the full-copy `generated/` files.

## 2. A consumer for research-workflow profiles, and open locales in `display_name`

**Problem.**
- A sealed `user_authored` profile validates and selects, but no pipeline stage reads it (#742 is still open).
- `display_name` is closed to `en`/`zh_TW`, so a profile can't carry a name in its users' language.

**Proposal.**
- Land a first consumer (#743/#744/#745) so that `stage_map` and `authority_points` change behaviour.
- Open `display_name` to BCP-47 keys.
- Offer `respiratory_medicine` (family `clinical_human_subjects`) as a candidate first shipped clinical profile.

**Retires.** The profile-equivalent instructions duplicated in the overlay's `ACTIVATE.md`.

## 3. Ship the reserved `clinical` domain evidence profile

**Problem.** `academic-paper/references/domain_evidence_profiles.md` reserves `clinical`, but selecting it falls back to `unknown_user_defined`. The Medicine/Health evidence hierarchy (lines 30–34) is preserved there but has no effect.

**Proposal.** Ship `clinical` with the preserved hierarchy, under the existing lint (`scripts/check_domain_evidence_profile.py`).

**Retires.** Nothing in the overlay directly. It removes a silent downgrade for every clinical user.

## 4. Character-limit abstracts in the venue profile

**Problem.** `shared/contracts/submission/venue_profile.schema.json` has `abstract_word_limit` only. Some venues count characters:
- ERS Congress: 1810 characters including spaces, plus a fixed cost per table cell and per figure;
- *Farmacia*: 1500 characters.

Word-based checks can't verify these.

**Proposal.** Add `abstract_limit: {value, unit: words|characters, counting_rule}`, scholar-declared like every other field, and teach `scripts/verify_submission_package.py` the character unit.

**Retires.** The character-limit part of the overlay's venue extras and `check_venue_extras.py`.

## 5. AI-disclosure rows for respiratory and medical publishers

**Problem.** `academic-paper/references/venue_disclosure_policies.md` covers BMJ, JAMA, Lancet and NEJM, but not ERS (ERJ, ERJ Open Research, ERS Congress), ATS/OUP (AJRCCM), Elsevier (CHEST, Respiratory Medicine), The Union (IJTLD, which asks for the *proportion* of AI-written text) or MDPI.

**Proposal.** Add these rows under the database's evidence-layer contract, using the dated sources gathered in the overlay's venue notes.

**Retires.** The advisory AI-disclosure placement column in the overlay's venue notes.

## 6. Core reporting-guideline reference updates

**Problem.** `deep-research/references/equator_reporting_guidelines.md` still anchors CONSORT at "CONSORT 2010 + extensions" (line 87). CONSORT 2025 and SPIRIT 2025 are published. The pre-registration guide lacks CTIS (EU CT numbers), ISRCTN and ICTRP. RECORD is mentioned only as a STROBE add-on, with no item depth.

**Proposal.** Update the anchors to CONSORT 2025 / SPIRIT 2025, add the EU and international trial registries, and expand RECORD.

**Retires.** Overlay reviewer prompts that today must say "core cites CONSORT 2010; check the 2025 items".

## 7. Respiratory rows in the core review-criteria registry

**Problem.** There is no `field_society_standard` row for respiratory medicine, and no `reporting_design_overlay` rows for RECORD or STROME-ID.

**Proposal.** Add three source-backed rows with receipts under `shared/review_criteria_sources/`:
- ERS/ATS technical standards;
- RECORD;
- STROME-ID.

They are field-generic, not Romanian.

**Retires.** The same rows in the overlay's review-criteria delta.

## 8. A professional-body `authority_level`

**Problem.** `authority_level` in `shared/contracts/human_subjects/authority_profile_registry.schema.json` is `supranational | national | subnational | tribal | institutional`. A national medical chamber's deontology code (e.g. the Romanian CMR Code 2025) is neither the state nor an institution. The overlay records it as `national` with a `known_gaps` note.

**Proposal.** Add `professional_body`.

**Retires.** The `known_gaps` workaround on `ro.cmr.deontology-code-2025`.

## 9. Registry-driven requirement-id prefixes in the reference-migration lint

**Problem.** `scripts/check_human_subjects_reference_migration.py` (the `REQUIREMENT_ID` regex, lines 101–106) recognises only the `us.45cfr46.`, `tw.hsra.` and `eu.gdpr.article-` prefixes. Requirement ids from any other registry (e.g. `ro.l46.*`) are never cross-checked in docs.

**Proposal.** Derive the prefix list from the registry or registries being linted.

**Retires.** Nothing in the overlay. It closes a silent coverage gap for any non-US/TW/EU profile.
