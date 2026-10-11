# Respiratory-medicine methodology inventory

Ticket: `.scratch/ro-respiratory-medicine/issues/04-respiratory-methodology-inventory.md` (primary working tree, untracked).
Branch: `research/respiratory-methodology-inventory` (throwaway; based on `main` @ e614b32).
Researched: 2026-10-10.

How claims were checked: repo pointers come from `rg` over this worktree (file:line as of e614b32). Bibliographic details (authors, journal, volume, pages, DOI) were checked against PubMed E-utilities records in this session. Web URLs were checked for HTTP 200 in this session unless marked otherwise. Where a numeric value (an MCID, say) is quoted, the note says whether it came from the PubMed abstract or is recalled from the full text and still needs confirming.

---

## Answer summary

1. **ARS already has a solid generic clinical-reporting core.** `deep-research/references/equator_reporting_guidelines.md` maps designs to PRISMA, CONSORT, STROBE, STARD 2015 (+ STARD-AI), TRIPOD+AI, CARE, COREQ/SRQR, SQUIRE, CHEERS, RIGHT/AGREE, ARRIVE, GRAMMS, and SPIRIT. It also includes a clinician-oriented design-routing sequence (§10). Systematic-review tooling covers PRISMA 2020 / PRISMA-P, RoB 2, ROBINS-I, GRADE and PROSPERO. Appraisal tools (QUADAS-3, PROBAST+AI) are named as companions.
2. **RECORD gets one sentence and no checklist.** It appears only as an optional add-on at `equator_reporting_guidelines.md:435`. Neither the §1 table nor `research_architect_agent` lists it. No other STROBE extension (RECORD-PE, STROME-ID, STROBE-MR) appears anywhere.
3. **Version drift in core:** core still says "CONSORT 2010" (`equator_reporting_guidelines.md:87`; `research_architect_agent.md:131` in both `agents/` and `deep-research/agents/`). CONSORT 2025 and SPIRIT 2025 were published in April 2025. This is a core/upstream fix, not an overlay item.
4. **There is no respiratory content at all.** A case-sensitive search finds zero hits for spirometry, FEV1, GOLD, GINA, COPD, asthma, tuberculosis, ATS/ERS, MCID, SGRQ, CAT, 6MWD, DLCO or FeNO, and none for ECDC, INSP or GBD. The only Eurostat mention is an education example. Everything in "Missing" below is net-new overlay content.
5. **Overlay surface:** `domain_evidence_profiles.md` reserves `clinical` but leaves it out of the enum. `shared/research_workflow_profiles/field_general.json` (schema `research-workflow-profile/1.0`) looks like the natural home for a `respiratory_medicine` profile. Whether an overlay can register a new profile without a core edit belongs to the extension-points ticket, not this one.

---

## Already covered in ARS (with pointers)

### Reporting guidelines

| Guideline | Where | Depth |
|---|---|---|
| Design → guideline map (PRISMA, CONSORT, NRSI/TREND, STROBE, COREQ/SRQR, SQUIRE, STARD 2015 + STARD-AI, TRIPOD+AI, RIGHT/AGREE, CARE, CHEERS, GRAMMS, ARRIVE, PRISMA-NMA, PRISMA-ScR) | `deep-research/references/equator_reporting_guidelines.md:8-28` | Table; bold rows have condensed checklists |
| PRISMA 2020 condensed + flow diagram | same file `:32-80` | Condensed |
| CONSORT ("2010 + extensions"), with CONSORT-SPI note | same file `:84-115` (version at `:87`) | Condensed; **outdated version label** |
| STROBE condensed (14 rows) | same file `:119-148` | Condensed; application notes are higher-education examples (`:143-148`) |
| COREQ, SQUIRE 2.0 | same file `:152-238` | Condensed |
| CARE 2013 (licensed adaptation, clinical notes) | same file `:242-276` | Full condensed + clinical notes |
| STARD 2015 (30 items) + STARD-AI, QUADAS-3 note | same file `:280-334` | Full condensed + clinical notes |
| TRIPOD+AI 2024 (27 items), PROBAST+AI note | same file `:338-396` | Full condensed + clinical notes |
| Clinician design-routing Q0–Q6a, ambiguity rule, ambiguous-phrase list | same file `:400-455` | Strong; designed for clinician authors |
| **RECORD** (routinely collected data) | same file `:435` only | One sentence; no checklist |
| SPIRIT (protocol, no results) | same file `:424` | Pointer only |
| Blueprint guideline picker (PRISMA 2020, CONSORT 2010, STROBE, COREQ, SQUIRE 2.0) | `deep-research/agents/research_architect_agent.md:124-138` (mirrored at `agents/research_architect_agent.md:126-133`) | Narrower than the reference file; no STARD/TRIPOD/CARE/RECORD |
| Reviewer check "CONSORT/STROBE/PRISMA followed?" | `academic-paper-reviewer/agents/domain_reviewer_agent.md:284` | One line |

### Systematic review, bias and certainty

- PRISMA-P 2015 protocol template: `deep-research/templates/prisma_protocol_template.md:1-17, 175-176, 222-240`
- PRISMA 2020 report template (RoB 2 / ROBINS-I, GRADE SoF, PROSPERO): `deep-research/templates/prisma_report_template.md:145, 192, 323, 367`
- Cochrane Handbook v6.4, RoB 2, ROBINS-I, GRADE, PROSPERO: `deep-research/references/systematic_review_toolkit.md:21-28, 151, 180, 228, 281, 330-349`
- `risk_of_bias_agent` (RoB 2 + cluster/crossover, ROBINS-I; "default to ROBINS-I" note for higher education): `deep-research/agents/risk_of_bias_agent.md:33, 56-128, 203`
- `meta_analysis_agent` GRADE: `deep-research/agents/meta_analysis_agent.md:225-264, 300`
- `sr-screener` defers RoB/GRADE to deep-research: `sr-screener/SKILL.md:106-108`

### Registration, authorship, venues

- Preregistration tree ("ICMJE requires RCTs to be pre-registered"): `deep-research/references/preregistration_guide.md:29-32`. Platforms: OSF, PROSPERO, ClinicalTrials.gov (`:62-72, 80`). **No EU CTIS / ISRCTN / WHO ICTRP.** Flag this for the regulation ticket.
- ICMJE authorship criteria: `academic-paper/references/credit_authorship_guide.md:141-143`
- Medical AI-disclosure venues (ICMJE, NEJM, Lancet, JAMA, BMJ …): `academic-paper/references/venue_disclosure_policies.md:4, 109-120`
- Medicine journal list (Lancet, BMJ, then medical education only; **no respiratory journals**): `academic-paper-reviewer/references/top_journals_by_field.md:108-117`

### Evidence/field profile hooks

- Evidence hierarchy row "Medicine/Health — Level I-II": `deep-research/references/source_quality_hierarchy.md:158`
- Domain evidence profiles. The ship-ready enum is `general_social_science`, `cs_ml`, `humanities_interpretive` and `unknown_user_defined`. **`clinical` is reserved and falls back to neutral**: `academic-paper/references/domain_evidence_profiles.md:7-18, 30-34`
- Research-workflow profile mechanism: `shared/research_workflow_profiles/field_general.json` (single shipped profile, all stages but `integrity_check` are `unresolved_fit`); schema `shared/contracts/research_workflow/research_workflow_profile.schema.json`; loader `scripts/research_workflow_profile.py`.

---

## Missing for respiratory work

All entries below are absent from the repo (zero `rg` hits). Bibliographic data comes from PubMed unless noted.

### A. Reporting-guideline gaps (EQUATOR family)

| Item | Primary source | Why it matters for respiratory work |
|---|---|---|
| **RECORD** checklist (13 items, extension of STROBE) | Benchimol EI et al. *PLoS Med* 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885 · EQUATOR page https://www.equator-network.org/reporting-guidelines/record/ | Romanian COPD/asthma/TB studies often use hospital discharge (DRG), CNAS claims or TB-register data. The abstract says RECORD has 13 items. |
| **RECORD-PE** (pharmacoepidemiology) | Langan SM et al. *BMJ* 2018;363:k3532. doi:10.1136/bmj.k3532 | Inhaler/biologic utilisation and safety studies in routinely collected data |
| **STROME-ID** (STROBE ext., molecular epidemiology of infectious disease) | Field N et al. *Lancet Infect Dis* 2014;14:341-52. doi:10.1016/S1473-3099(13)70324-4 | TB genotyping/WGS transmission and MDR-TB clusters |
| **STROBE-MR** | Skrivankova VW et al. *BMJ* 2021;375:n2233 / *JAMA* 2021;326:1614-21 | Mendelian-randomisation papers on COPD/asthma risk factors |
| **CONSORT 2025** (supersedes 2010) | Hopewell S et al. *BMJ* 2025;389:e081123. doi:10.1136/bmj-2024-081123 | Core label is stale (`equator_reporting_guidelines.md:87`, `research_architect_agent.md:131`) |
| **SPIRIT 2025** | Chan AW et al. *BMJ* 2025;389:e081477; *PLoS Med* 2025;22:e1004589 | Trial protocols |
| Base STROBE citation (core cites none) | von Elm E et al. *Lancet* 2007;370:1453-7. doi:10.1016/S0140-6736(07)61602-X | Provenance for any condensed checklist |
| TB diagnostic-accuracy guidance (complements STARD) | Nathavitharana RR et al. "Guidance for Studies Evaluating the Accuracy of Tuberculosis Triage Tests." *J Infect Dis* 2019;220(Suppl 3):S116-25. doi:10.1093/infdis/jiz243 | TB triage tests (CXR-CAD, CRP, symptom screens) |

### B. ATS/ERS technical standards (measurement and interpretation)

| Standard | Primary source |
|---|---|
| Spirometry 2019 | Graham BL et al. *Am J Respir Crit Care Med* 2019;200(8):e70-e88. doi:10.1164/rccm.201908-1590ST |
| DLCO 2017 | Graham BL et al. *Eur Respir J* 2017;49:1600016. doi:10.1183/13993003.00016-2016 |
| Interpretation 2022 | Stanojevic S et al. *Eur Respir J* 2022;60:2101499. doi:10.1183/13993003.01499-2021 |
| Lung volumes 2023 | Bhakta NR et al. ERS/ATS technical statement: standardisation of the measurement of lung volumes. *Eur Respir J* 2023;62(4):2201519. doi:10.1183/13993003.01519-2022 |
| Oscillometry 2020 | King GG et al. *Eur Respir J* 2020;55:1900753. doi:10.1183/13993003.00753-2019 |
| FeNO measurement 2005 | ATS/ERS. *Am J Respir Crit Care Med* 2005;171:912-30. doi:10.1164/rccm.200406-710ST |
| FeNO interpretation 2011 (ATS CPG) | Dweik RA et al. *Am J Respir Crit Care Med* 2011;184:602-15. doi:10.1164/rccm.9120-11ST |
| Field walking tests (6MWT/ISWT/ESWT) 2014 | Holland AE et al. *Eur Respir J* 2014;44:1428-46. doi:10.1183/09031936.00150314; companion systematic review: Singh SJ et al. *Eur Respir J* 2014;44:1447-78. doi:10.1183/09031936.00150414 |
| Reference equations | GLI-2012: Quanjer PH et al. *Eur Respir J* 2012;40:1324-43. doi:10.1183/09031936.00080312. Race-neutral GLI Global: Bowerman C et al. *Am J Respir Crit Care Med* 2023;207:768-74. doi:10.1164/rccm.202205-0963OC |
| Race/ethnicity in PFT interpretation (ATS statement) | Bhakta NR et al. *Am J Respir Crit Care Med* 2023;207:978-95. doi:10.1164/rccm.202302-0310ST |

Reviewer-relevant consequences (checks a respiratory profile should prompt): acceptability/repeatability grading per 2019 spirometry; reference-equation set named (GLI-2012 vs GLI Global); LLN/z-score rather than fixed %predicted where the 2022 standard applies. The z-score/LLN recommendation is my reading of the 2022 standard and should be confirmed against its full text before it is encoded. Note also the post-bronchodilator definition of airflow obstruction (GOLD).

### C. Disease-definition documents (annual, version-pinned)

| Document | Current edition (verified 2026-10-10) |
|---|---|
| GOLD Global Strategy for COPD | **2026 GOLD Report**: https://goldcopd.org/2026-gold-report/ (HTTP 200) |
| GINA Global Strategy for Asthma | **GINA 2026**: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf (HTTP 200). Executive summary: Reddel HK et al. *Am J Respir Crit Care Med* 2026 (epub 8 Oct 2026). doi:10.1093/ajrccm/aamag542, PMID 42847657 |
| ATS/ERS asthma control & exacerbation definitions for trials | Reddel HK et al. *Am J Respir Crit Care Med* 2009;180:59-99. doi:10.1164/rccm.200801-060ST |
| COPD trial outcomes (ATS/ERS task force) | Cazzola M et al. *Eur Respir J* 2008;31:416-69. doi:10.1183/09031936.00099306 |

GOLD and GINA call themselves *strategy reports*, not guidelines. Both revise every year, so the profile must store edition and year, not "current".

### D. MCIDs / MIDs (cite the source, not just the number)

| Outcome | Value | Source | Verification status |
|---|---|---|---|
| SGRQ (COPD) | ~4 units | Jones PW. *COPD* 2005;2:75-9. doi:10.1081/copd-200050513 | Stated in PubMed abstract |
| CAT | 2 points (ROC); anchor range −1.2 to −2.8 | Kon SS et al. *Lancet Respir Med* 2014;2:195-203. doi:10.1016/S2213-2600(14)70001-3 | Stated in abstract |
| Trough FEV1 (COPD) | ~100 mL | Donohue JF. *COPD* 2005;2:111-24. doi:10.1081/copd-200053377. Also Cazzola 2008 (above) | Abstract says "about 100 mL" and that "a precise MCID … has not been established" |
| 6MWD (chronic respiratory disease) | Commonly cited 25–33 m (COPD) | Singh SJ et al. *Eur Respir J* 2014;44:1447-78 | **Not in abstract. Recalled from full text; confirm before encoding.** Abstract confirms a 26 m learning effect between first and second tests |
| ACT (asthma) | 3 points | Schatz M et al. *J Allergy Clin Immunol* 2009;124:719-23. doi:10.1016/j.jaci.2009.06.053 | Stated in abstract |
| ACQ / AQLQ (asthma) | Commonly cited 0.5 | Juniper EF et al. (ACQ development, PMID 10573240) | **Not verified this session** |

### E. TB-specific standards

| Item | Primary source |
|---|---|
| WHO *Definitions and reporting framework for tuberculosis – 2013 revision (updated Dec 2014 and Jan 2020)* | https://www.who.int/publications/i/item/9789241505345 (HTTP 200) |
| WHO updated treatment-outcome definitions (2021 onwards), now in the operational handbook | WHO operational handbook on TB, Module 4: treatment: https://www.who.int/publications/i/item/9789240050761. Secondary summary: Stadler JAM. *Afr J Thorac Crit Care Med* 2022;28(2). doi:10.7196/AJTCCM.2022.v28i2.224 |
| WHO consolidated guidelines on TB, Module 4: treatment and care (2025 edition) | https://www.who.int/publications/i/item/9789240107243 |
| IJTLD "clinical standards" series (Union/GTN/ERS/ALAT consensus) | e.g. Migliori GB et al. Clinical standards for the assessment, management and rehabilitation of post-TB lung disease. *Int J Tuberc Lung Dis* 2021;25:797-813. doi:10.5588/ijtld.21.0425 |
| Romanian national TB methodology | *Ghid metodologic de implementare a PNPSCT*. A 2015 edition is hosted at old.ms.ro, and a newer edition (title adds "și altor micobacterioze") appears via ResearchGate. **Current official edition not verified.** |

"IJTLD guidance", as the ticket uses it, does not map to one reporting guideline I could find. IJTLD publishes clinical-standards consensus papers, and its author instructions may name EQUATOR checklists, but I did not verify those instructions this session.

---

## Data sources

| Source | What it gives | URL / identifier | Check |
|---|---|---|---|
| **INSP / CNSCBT** (Centrul Național de Supraveghere și Control al Bolilor Transmisibile) | Communicable-disease surveillance (TB analyses, influenza/SARI, other notifiable respiratory infections) | https://insp.gov.ro/downloads/tuberculoza/ (search-indexed) | **HTTP 503 from this host. May be bot-blocking; recheck from a browser** |
| **INSP / CNSISP** | Causes-of-death bulletins for Romania | e.g. `insp.gov.ro/download/cnsisp/.../Buletin-Informativ-CAUZE-DECES-2018_2019.pdf` (search-indexed) | Not fetched |
| **PNPSCT** (Programul Național de Prevenire, Supraveghere și Control al Tuberculozei), coordinated from Institutul de Pneumoftiziologie „Marius Nasta” | National TB programme pages, including "Actualizarea endemiei TB" updates | https://marius-nasta.ro/programul-national-de-prevenire-supraveghere-si-control-al-tuberculozei-pnpsct/ | HTTP 200; page content confirmed |
| **ECDC / WHO Europe** joint TB report | *Tuberculosis surveillance and monitoring in Europe 2025 – 2023 data* | https://www.who.int/europe/publications/i/item/9789289061834 | HTTP 200 |
| **ECDC Surveillance Atlas** | EU/EEA notifiable-disease series incl. TB, influenza, legionellosis, pertussis | https://atlas.ecdc.europa.eu/public/index.aspx | HTTP 200 |
| **ERVISS** (ECDC + WHO Europe) | Weekly respiratory-virus surveillance (influenza, RSV, SARS-CoV-2); data on GitHub `EU-ECDC/Respiratory_viruses_weekly_data` | https://erviss.org/ | HTTP 200 |
| **Eurostat** | Causes of death `hlth_cd_aro` (updated 2026-09-24); NUTS-2 standardised death rates `hlth_cd_asdr2`; hospital discharges `hlth_co_disch1` (**labelled "historical data 1995-2021"**; successor dataset not identified) | Eurostat dissemination API | API returned data for `geo=RO` |
| **WHO Europe** European Health Information Gateway / HFA-DB | Harmonised country indicators | https://gateway.euro.who.int/en/datasets/european-health-for-all-database/ | HTTP 200 |
| **GBD** (IHME) | Modelled burden (incidence, prevalence, DALYs) for COPD, asthma, TB, LRI, lung cancer; GBD 2023 round | https://vizhub.healthdata.org/gbd-results/ | HTTP 200 |
| INS TEMPO-Online (supplementary) | Romanian national statistics (population denominators, some health tables) | http://statistici.insse.ro:8077/tempo-online/ | HTTP 200 |
| National DRG portal (supplementary) | Hospital-activity / DRG data (access conditions unknown) | https://www.drg.ro/ | HTTP 200; content not reviewed |

Any study built on INSP, PNPSCT, DRG or CNAS data is "routinely collected", so RECORD applies. That links section A to this table.

---

## Open uncertainties

1. **INSP site reachability.** insp.gov.ro returned 503 to scripted requests. I could not check whether CNSCBT TB and SARI reports are current or how they are formatted.
2. **6MWD and ACQ MCIDs** are recalled, not read from source (see table D). Confirm both against the full texts before encoding.
3. **Eurostat hospital-discharge successor.** `hlth_co_disch1` stops at 2021. I did not identify the current dataset code.
4. **Current PNPSCT methodological guide.** I did not find which edition is in force or its official URL.
5. **IJTLD author instructions.** I did not verify whether they mandate particular EQUATOR checklists.
6. **Interpretation of the 2022 standard and the race-neutral equations.** I did not confirm against full text that the 2022 standard recommends LLN/z-scores, or how ERS (as opposed to ATS) positions GLI Global. Don't encode either as a hard rule until checked.
7. **Overlay mechanics.** Whether an overlay can add a `respiratory_medicine` research-workflow profile, or un-reserve `clinical`, without a core edit is outside this ticket. See the upstream-extension-points research.
8. **Sleep, ILD and lung cancer** were not inventoried (e.g. AASM scoring manual, ATS/ERS/JRS/ALAT IPF guideline, IASLC staging/TNM). The map lists them as in-domain, so they likely need a follow-up ticket if the profile is meant to cover them.

---

## Implications for the profile

- **Overlay reference file (`respiratory_medicine` methodology pack).** Ship a single reference listing sections B–E above with full citations and an `edition`/`last_verified` field per entry. GOLD and GINA editions need a freshness check like the existing PRISMA-trAIce freshness pattern (`scripts/check_prisma_trAIce_freshness.py`).
- **Routing add-ons, not new routes.** Reuse the core §10 routing (`equator_reporting_guidelines.md:400-455`) unchanged. The overlay should only add *secondary-component prompts*: RECORD/RECORD-PE when data are routinely collected (Romanian registers, DRG, CNAS), STROME-ID for TB molecular epidemiology, and TB-triage guidance alongside STARD. This matches the extension clause at `:435` and needs no core edit.
- **Reviewer prompts.** Add a respiratory checklist for `domain_reviewer_agent`. It should cover the measurement standard cited and met (2019 spirometry, 2017 DLCO, 2005/2011 FeNO, 2014 field walking tests), the reference-equation set named, GOLD or GINA definitions with their edition stated, WHO TB definitions with the outcome-definition version stated, and MCIDs cited with their source rather than as bare numbers.
- **Data-source registry.** Add a Romania/EU respiratory data-source list (table above) to the `ro` locale pack or the profile, with access notes. Mark INSP pages as "verify reachability".
- **Upstream/core issues to file (not overlay):** (a) CONSORT 2010 → CONSORT 2025 and SPIRIT 2025 in `equator_reporting_guidelines.md:87` and both `research_architect_agent.md:131`; (b) RECORD missing from the §1 table and from the architect picker; (c) preregistration platforms lack EU CTIS/ISRCTN/WHO ICTRP (`preregistration_guide.md:62-72`). This also matters to the regulation ticket.
- **Scope signal for the map.** Cover COPD, asthma and TB (well-sourced above) first. Sleep, ILD and lung cancer need their own inventory before the profile claims them.
