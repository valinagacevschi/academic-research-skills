# First-class study designs for the respiratory_medicine profile

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 04, 11, 13, 14
Map: ../map.md

## Question

Which study designs and reporting guidelines does the `respiratory_medicine` field profile treat as first-class (with stage-map states and authority points), and which fall back to the general path?

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved).

- **Meaning of first-class.** The profile schema has no notion of a study design. Core ARS chooses the reporting guideline (`deep-research/references/equator_reporting_guidelines.md` §10, questions Q0–Q6), and the overlay never re-routes. A **first-class design** gets respiratory add-ons on top of its core route. A **fallback design** gets the core route plus only the design-independent respiratory content (see [GLOSSARY](../GLOSSARY.md)).
- **First-class designs:** cohort, case-control and cross-sectional (STROBE); case report and case series (CARE); diagnostic accuracy (STARD); systematic review and meta-analysis (PRISMA).
- **Fallback designs:** RCTs and protocols (CONSORT/SPIRIT), prediction models (TRIPOD+AI), qualitative, economic, quality-improvement and Mendelian-randomisation studies, and non-randomised intervention studies.
- **Two separate dimensions: design × subdomain.** Subdomain content applies to every design, fallback included. A COPD-exacerbation RCT still gets the ERS 2022 core outcome set, the MCIDs and edition stamps.
- **Subdomain references.** One file per subdomain, every definition edition-stamped and every MCID evidence-tagged. There are six: airways; ILD; pulmonary vascular; sleep; thoracic oncology; infection, occupational, rehab, critical care and interventional. This replaces the "four subdomain packs" proposed in [Respiratory subdomain standards: ILD, pulmonary vascular, sleep, thoracic oncology](13-respiratory-subdomain-parenchymal-vascular-sleep-oncology.md). The final file slicing is left to the spec.
- **Design add-ons:**
  - **Cohort, case-control, cross-sectional:**
    - add RECORD whenever the data come from routine records (always ask);
    - add STROME-ID for infection or TB studies;
    - a Romanian data-source note: hospital records, the national TB registry (PNPSCT/Marius Nasta), and CNAS reimbursement protocols as a selection-bias source;
    - a prompt to put the edition year on any guideline-defined cohort label.
  - **Diagnostic accuracy:** measurement standards for the index or reference test: ATS/ERS spirometry 2019 with race-neutral GLI equations; DLCO 2017; AASM v3 for sleep tests; Lung-RADS v2022; a TB-diagnostics prompt; ERS/ESGE/ESTS EBUS 2026.
  - **Case report and case series:** CARE plus edition-stamped definitions, and a prompt to check it is a true series with no comparison group, not an unadmitted cohort.
  - **Systematic review and meta-analysis:** PRISMA, MCID anchors for GRADE imprecision judgements, and a check for guideline edition drift across included studies.
- **Profile contents (dormant until #742):**
  - **Stage map:** all nine stages `applicable`.
  - **Authority points:**
    - `methodology`: EQUATOR routing + design add-ons;
    - `retrieval`: the RO/EU data-source list;
    - `drafting`: the subdomain references;
    - `review`: the respiratory reviewer prompts;
    - `integrity_check`: the evidence-tag rule.

    Ethics and CTR authority points are deferred to [Romanian ethics-gate behaviour](09-romanian-ethics-gate.md).
  - **`alternative_categories`:** `declared` with `alternative_design` and `alternative_measurement`.
- **Reviewer prompts.** One reviewer-prompt file in the overlay, referenced from the activation preamble. The standards are also added as rows in the review-criteria registry delta: a `field_society_standard` row for ERS/ATS, and `reporting_design_overlay` rows for RECORD and STROME-ID.
