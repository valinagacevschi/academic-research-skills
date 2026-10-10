# Romanian ethics-gate behaviour

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 01, 15
Map: ../map.md

## Question

What should the pipeline check, ask, or refuse before drafting a Romanian respiratory paper (ethics approval number, consent or waiver basis, trial registration, CTR/ANMDMR status), and at which stage gate?

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved). Constraint from core: the ethics review agent never vetoes, and human-subjects results come only from an author-declared, replay-validated context (`deep-research/agents/ethics_review_agent.md`; `shared/references/human_subjects_authority_protocol.md`). The overlay's gate is therefore registry content, plus what the activation preamble tells the agents, plus the reviewer prompts.

- **Posture: never refuse; ask and record.** Missing items appear as `submission_readiness=gaps_located` and as external-actor dependencies. In the manuscript checks they are graded Conditional, never Critical. Drafting continues.
- **Two touchpoints, no new gate:**
  - **Intake.** The activation preamble has the author build the Romanian context record before drafting. The routing question comes first (CTR drug trial / MDR device investigation / observational), then the RO facts.
  - **Phase 5 review.** The ethics agent reads the resolved context, and the reviewer prompts check the manuscript statements.
- **Profiles shipped in the human-subjects registry delta (five):**
  - `ro.ms.ctr-national-implementation`, `ro.ms.mdr-clinical-investigation` and `ro.parliament.law-46-2003.patient-rights-research` (review_ethics);
  - `ro.parliament.law-190-2018.research-bounded`: a separate `data_protection` profile selected alongside `eu.gdpr.research-core-bounded` (several profiles per axis are allowed; registry overlays are only institutional/funder);
  - `ro.cmr.deontology-code-2025`: `authority_level: national`, with a `known_gaps` note that it is a professional-body code, so no schema change.

  Non-interventional PASS is in `known_exclusions`. The requirement drafts are in §4 of the regulatory findings (branch `research/romanian-regulatory-landscape`).
- **Retrospective consent.** Law 46/2003 Arts. 19 and 22 are encoded as `external_authority_required`, with the local ethics committee + controller/DPO deciding. A waiver is never offered as available. The Art. 22 legal risk is always shown, as a `known_gaps` item. "Consent waived by committee X" wording is allowed only when the author declares that the committee said so.
- **Registry facts (routing booleans):** `scope.ro_ctr_national`, `scope.ro_mdr_investigation`, `scope.ro_patient_rights`, `scope.ro_law_190`, `professional.ro_cmr_member`, `data.ro_cnp_processed`, `activity.retrospective_records_only`. Committee name, approval number and date, EU CT number and the consent statement are manuscript fields, not facts.
- **Manuscript-statement checks** (reviewer-prompt file + review-criteria registry rows):
  - an ethics statement naming the committee (CNBMDM or local), with approval number and date;
  - a consent statement, or an anonymisation statement plus the committee's decision;
  - the EU CT number (CTIS) for CTR trials, plus any registry the venue requires;
  - INN-only drug names (CMR Art. 46);
  - consent for identifiable images (Law 46 Art. 20);
  - a COI disclosure.

  Each one missing is Conditional.
- **Sources.** Anchors are `authoritative_unofficial`, `source_language: ro`, until verified on the official portal under [Fact-verification policy for overlay content](16-fact-verification-policy.md).
- **Institutional overlays (hospital or UMF ethics committees):** none shipped. The preamble tells the author to declare `none_declared_by_author`. The possibility is folded into the pilot-clinician item in the map's Not yet specified.
- **Builds on:** [Probe a RO profile in an alternate human-subjects registry](15-probe-ro-human-subjects-alt-registry.md) (mechanism proven), [Romanian regulatory landscape for respiratory research](01-romanian-regulatory-landscape.md) (content).
