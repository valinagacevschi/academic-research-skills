# Romanian respiratory-medicine overlay instructions

## Output

Write all generated output in English. The user may converse in Romanian.

## Registries

- Resolve human-subjects contexts, review-pathway traces, and packet manifests with `{OVERLAY_ROOT}/registries/generated/human_subjects_authority_registry.json`.
- Resolve review targets with `{OVERLAY_ROOT}/registries/generated/review_criteria_registry.json`.
- Pass the applicable overlay file as `--registry`; never pass a core registry path for these tasks.
- Contexts pin profile digests. Re-pin selected profiles and display precedence after overlay registries are regenerated. Regeneration also changes registry digests, so older resolved artifacts must be regenerated and replayed.

## Intake, before drafting

Build the Romanian context record before drafting. Ask the routing question first: CTR medicinal-product trial, MDR device investigation, or observational study. Then record the seven user-declared facts: `scope.ro_ctr_national`, `scope.ro_mdr_investigation`, `scope.ro_patient_rights`, `scope.ro_law_190`, `professional.ro_cmr_member`, `data.ro_cnp_processed`, and `activity.retrospective_records_only`. Then record `scope.eu_gdpr` and applicable GDPR facts: `processing.personal_data`, `data.special_category`, `data.collected_from_subject`, `purpose.scientific_research`, `gdpr.member_state_research_law_identified`, and `packet_v1.cross_border_material_transfer`. Unknown values remain unknown. Select applicable `ro.*` profiles and `eu.gdpr.research-core-bounded`; declare `overlay_selection_state.institutional` as `none_declared_by_author`.

Never infer applicability from locale, affiliation, or manuscript text. Never offer a consent waiver. Show the Law 46/2003 Article 22 disclosure risk and refer the question to the controller/DPO and local ethics committee.

## Venue

For a named target, show its matching section of `{OVERLAY_ROOT}/references/venue_notes.md` as “what the overlay found; check the current author instructions”. The scholar confirms values and declares only those confirmed in core's venue profile. Put character limits, required headings, and other extras in a scholar-declared venue-extras file, following `{OVERLAY_ROOT}/venue_extras/README.md`. Never fill either from notes without confirmation. At submission readiness, run the advisory venue-status check in SPEC §9, recording each URL and date. Never rank venues.

## Patient data

## Patient data

Apply these tiers before handling patient material:

- **Direct identifiers** (including a CNP): stop once; this is not a refusal. Never echo them or write them to workspace files. Ask the user to redact and re-paste, and note that the session transcript already holds anything previously pasted.
- **Line-level data**: warn once per session. Continue only after the user confirms their controller or DPO allows sending it to the model provider.
- **Aggregate data**: no action.

For code-to-data work, write analysis scripts for the user to run locally and ask only for aggregate results to come back. Choosing a local or EU-hosted model is the user's own choice.

Frame legal points as questions for the controller or DPO, never as rulings:

- Which GDPR Article 9(2) condition applies, and what supports it?
- Is an Article 28 processor agreement in place with the model provider?
- Does a Chapter V transfer apply, and what safeguards are in place?
- What safeguards are required by Law 190/2018 Article 4 for CNP processing?
- How do Law 46/2003 Articles 21–22 apply to confidentiality here?

For case reports, use relative dates, age in years, and generalise rare details. Never paste identifiable images; strip DICOM metadata before any permitted image use.
## Design and subdomain content

Core chooses the reporting guideline; never re-route it. Apply `{OVERLAY_ROOT}/references/design_addons.md` for first-class designs. For every design, apply the matching file under `{OVERLAY_ROOT}/references/subdomains/`. Reviewers apply `{OVERLAY_ROOT}/references/reviewer_prompts.md`; manuscript-statement gaps are Conditional, never Critical.

## Facts

Only values tagged `primary-full-text` or `primary-abstract` are facts. `secondary` values are advisory and must be shown with a “verify” caveat; stale rows are advisory. Never state a respiratory threshold, MCID, or legal provision from memory when the overlay has a row for it. If it has no row, say “not verified”.

## Citations

Follow `{OVERLAY_ROOT}/references/citations_ro.md`.

## Field profile

`{OVERLAY_ROOT}/profile/respiratory_medicine.json` is dormant until upstream #742. Carry its behaviour through these instructions: apply the design add-ons, subdomain references, reviewer prompts, and evidence-tag rule above.
