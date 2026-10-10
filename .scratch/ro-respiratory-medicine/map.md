# Map: Romanian respiratory-medicine adaptation of ARS

Label: wayfinder:map

## Destination

A hand-off-ready **spec** for adapting ARS to respiratory-medicine research and paper publishing in Romania, delivered as an **overlay** (a `respiratory_medicine` field profile, registry entries, and venue/format profiles) with no core edits, so the fork keeps tracking upstream `Imbad0202/academic-research-skills`. All ARS output is English.

**Reached 2026-10-10:** [SPEC.md](../../overlays/ro-respiratory-medicine/docs/SPEC.md) (untracked; not committed).

## Notes

- Domain: academic medical publishing, clinical respiratory research in Romania across the whole of pulmonology: airways disease (COPD, asthma, bronchiectasis, CF, AATD, cough), ILD, pulmonary vascular disease, sleep, thoracic oncology, infection incl. TB/MDR-TB, occupational, rehab, critical care, interventional.
- Primary users: Romanian pulmonologists and residents writing journal papers. Secondary users: PhD candidates. Theses themselves are out of scope.
- Targets: international English-language respiratory journals (ERJ, Chest, AJRCCM, Thorax…), Romanian venues that publish in English (*Pneumologia* etc.), and conference abstracts (ERS; SRP congress, English half only).
- "Romania" covers: citations with Romanian author names and diacritics (no Romanian output), regulation (ethics/ANMDMR/CTR/GDPR), data and evidence (INSP, national TB programme), and academic-career pressure (thin: venue choice only).
- Plan only. The map ends at the spec, and implementation is delegated afterwards (Codex). Don't build the pack inside the map.
- Respect upstream's overlay boundary (`shared/output_language_pair.md` § Overlay boundary): packs never overlay SKILL.md, agents, IRON RULEs, integrity protocols, schemas, modes, or oversight rules.
- Skills to consult per session: grilling + domain-modeling (HITL tickets); research (research tickets).
- Vocabulary: [GLOSSARY](GLOSSARY.md). Upstream asks (core changes we offer upstream, never make in the fork) are gathered in the spec, not built.
- Tracker: local markdown (this directory). Research findings live on throwaway `research/<name>` branches, with pointers in the tickets.

## Decisions so far

<!-- one line per closed ticket: [title](link): gist -->

- [Romanian regulatory landscape for respiratory research](issues/01-romanian-regulatory-landscape.md): Trials run through CTR/CTIS with ANMDMR and CNBMDM; observational studies rely on a local ethics committee; no explicit research basis for health data under GDPR Art. 9(2)(j) or a Law 46/2003 waiver, so practice relies on anonymisation
- [Venue landscape for Romanian respiratory publishing](issues/02-venue-landscape.md): Three venue tiers (international respiratory journals, MDPI, Romanian journals); a Romanian abstract is required only by Farmacia and the SRP congress; formats and AI-disclosure rules vary; delisting risk means checking indexing at submission time
- [Upstream ARS extension points for an overlay](issues/03-upstream-extension-points.md): `ro-en` needs a core and schema change (no loader yet); the field profile validates but nothing consumes it (#742); the registries can be shipped as full copies via `--registry`; venue and format profiles work as config only
- [Respiratory-medicine methodology inventory](issues/04-respiratory-methodology-inventory.md): Generic EQUATOR coverage exists but no respiratory content; ATS/ERS, GOLD/GINA, TB, RECORD and MCID sources need adding; sleep, ILD and lung cancer not yet covered
- [Romanian scientific-language resources](issues/05-romanian-scientific-language.md): No Romanian MeSH; ICD-10-AM in use; comma-below ș/ț required in generated text, publisher characters kept in quoted data; Vancouver variants differ; `ro-en` is a Latin-Latin pair
- [Extent of Romanian-language output](issues/07-romanian-output-extent.md): English-only output; no `ro-en` pair and no Romanian abstracts (the author writes the SRP congress Romanian half); Romanian conversation allowed but no Romanian triggers; *Farmacia* dropped
- [Respiratory subdomain standards: airways disease](issues/11-respiratory-subdomain-standards.md): GOLD 2026 changed Group E and adopted Rome grading (record edition year on cohorts); GINA 2026 T2 cut-offs, ERS 2025 bronchiectasis, ECFS 2023–24; CNAS reimbursement protocols are a selection-bias source
- [Respiratory subdomain standards: ILD, pulmonary vascular, sleep, thoracic oncology](issues/13-respiratory-subdomain-parenchymal-vascular-sleep-oncology.md): IPF/PPF 2022, ESC/ERS 2022 + WSPH 2024, AASM v3, TNM 9th edition; Romanian OSA driving vs CPAP reimbursement bands differ; national lung-cancer screening 2025–29; four subdomain packs, each definition edition-stamped
- [Respiratory subdomain standards: infection, occupational, rehab, critical care, interventional](issues/14-respiratory-subdomain-infection-and-other.md): New 2025–26 TB, EBUS and pneumonia outcome-set documents; Romania TB, AMR and tobacco figures from primary sources; walking-test MCIDs settled; no new reporting routing, only definitions and outcomes
- [Overlay mechanism decision](issues/06-overlay-mechanism.md): Overlay (not a locale pack) in `overlays/ro-respiratory-medicine/`; registry deltas merged by a generator into pinned full copies; activation preamble plus installer; profile shipped sealed but dormant until #742; manifest plus `check_overlay` in CI; human-subjects half depends on a probe
- [Probe a RO profile in an alternate human-subjects registry](issues/15-probe-ro-human-subjects-alt-registry.md): Pass with no core edits; resolve, pathway trace and packet manifest all work against the overlay registry (they bind by registry id, version and digest, not by path); core lints are unaffected; the generator must re-pin digests and keep anchor sources consistent
- [First-class study designs for the respiratory_medicine profile](issues/08-first-class-study-designs.md): Core keeps choosing the reporting guideline; cohort, case-control, cross-sectional, case report/series, diagnostic accuracy and systematic reviews get respiratory add-ons, other designs fall back; six subdomain references apply to every design; profile has all stages applicable and five authority points
- [Romanian ethics-gate behaviour](issues/09-romanian-ethics-gate.md): Never refuse, ask and record; RO context record built at intake, checked at Phase 5 review; five `ro.*` profiles (CTR, MDR, Law 46, Law 190, CMR code); no consent waiver offered for chart reviews; manuscript ethics, consent, EU CT, INN and image statements graded Conditional
- [Patient data in prompts](issues/10-patient-data-in-prompts.md): Three tiers; stop once on direct identifiers, warn once on line-level data, nothing on aggregates; line-level analysis runs locally in scripts ARS writes; optional checksum-based CNP-blocking hook; legal points raised as questions for the controller/DPO, no registry change
- [Target-venue support and indexing checks](issues/12-target-venue-support.md): Six international journals, four OA/Romanian venues and two congresses get sourced venue notes that the scholar confirms (no pre-filled profiles); venue extras plus a check script for character limits and headings; AI-disclosure rows and character limits are upstream asks; advisory, dated venue-status check, never ranking
- [Fact-verification policy for overlay content](issues/16-fact-verification-policy.md): Five evidence tags mapped onto core's freshness values; only primary-sourced values become facts, secondary ones advisory, recalled ones never encoded; the verification pass is the first implementation slice; values are demoted to advisory after 12 months (6 for venue notes), plus an edition-watch list
- [Romanian eval cases for the overlay](issues/17-romanian-eval-cases.md) (auto-approved): Deterministic pytest suite for the CNP hook, venue extras, lint, registry generators and profile; six fictional-data plugin evals under `overlays/ro-respiratory-medicine/plugin-evals/`; v1 is done when CI is green and all six pass once
- [Spec shape and slicing into implementation tickets](issues/18-spec-shape-and-slicing.md) (auto-approved): Self-contained spec at `overlays/ro-respiratory-medicine/docs/SPEC.md`; 11 slices with the lint skeleton first and the verification pass second; upstream asks drafted but not filed

## Not yet specified

_(none: the frontier has reached the destination)_

## Out of scope

- Romanian-language output (a `ro-en` language pair, Romanian abstracts, a `ro` locale pack, Romanian trigger phrases): papers are always in English. See [Extent of Romanian-language output](issues/07-romanian-output-extent.md).
- Fixes to shared core references (CONSORT 2010 → 2025, SPIRIT 2025, CTIS/ISRCTN/ICTRP in the pre-registration guide, RECORD checklist depth): core edits violate the overlay destination; contribute them upstream separately. Surfaced by [Respiratory-medicine methodology inventory](issues/04-respiratory-methodology-inventory.md).
- Doctoral thesis production and CNATDCU/UMF career-criteria planning: beyond the destination (journal papers and abstracts).
- Building the overlay pack itself: happens after the spec is handed off.
- Pilot clinician validation (a prototype draft abstract or ethics-gate dialogue reviewed by a real Romanian pulmonologist, and any institutional ethics-committee overlay): no clinician confirmed, so it is beyond this destination; auto-approved, flagged for Val. See [Spec shape and slicing into implementation tickets](issues/18-spec-shape-and-slicing.md).
