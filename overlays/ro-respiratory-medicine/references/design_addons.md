# Design add-ons

Core ARS routes reporting using EQUATOR Q0–Q6 (§10). The overlay never re-routes that choice; it adds design × subdomain content only after core's choice. First-class designs receive the checks below. Fallback designs receive only the design-independent subdomain references.

## Cohort, case-control, and cross-sectional (STROBE)

- Were the data collected from routine records? If yes, add RECORD (`methodology.record_2015`). For pharmacoepidemiology, also check RECORD-PE (`methodology.record_pe_2018`).
- Is the study about infection or TB molecular epidemiology? If yes, ask whether STROME-ID is applicable (`methodology.strome_id_2014`).
- Are Romanian hospital records or PNPSCT/Marius Nasta sources used? Identify their provenance and coverage; the PNPSCT source is `data.pnpsct`.
- Could CNAS reimbursement protocols create selection bias? Treat them as a possible selection mechanism, not validated endpoints; the adherence rule is `sleep.cnas-cpap-adherence`.
- Does a guideline-defined cohort label appear (for example, a GOLD group)? Ask the author to state its classification edition (`airways.gold-2026-group-e`).

## Diagnostic accuracy (STARD)

Ask which measurement standards apply and have the author identify the method and edition: spirometry and race-neutral GLI equations (`methodology.ats_ers_spirometry_2019`, `methodology.gli_race_neutral_2023`); DLCO (`methodology.ats_ers_dlco_2017`); lung volumes (`methodology.ats_ers_lung_volumes_2023`); FeNO (`methodology.ats_ers_feno_2005`); sleep tests (`sleep.aasm-v3-2023`); Lung-RADS (`thoracic_oncology.lung-rads-v2022`); endosonography (`infection_and_other.endosonography_2026`). For field walking, check the standard and relevant MID (`methodology.ers_ats_field_walking_2014`, `methodology.daynes_6mwd_mid_2025`, `methodology.daynes_iswt_mid_2025`).

Ask whether the index test is a TB diagnostic test and, if yes, whether the manuscript reports the applicable TB-specific context (`infection_and_other.ro_tb_2024`).

## Case report / case series (CARE)

Ask the author to edition-stamp each disease definition and severity classification using the relevant subdomain reference. Is this a true series without a comparison group? If not, ask whether it is an unadmitted cohort and clarify the design before drafting.

## Systematic review / meta-analysis (PRISMA)

Ask which MCID source anchors GRADE imprecision judgements and whether it is appropriate to the population and instrument. Check for guideline edition drift across included studies; preserve each study's edition rather than silently harmonising definitions. Relevant examples include `airways.acq-mcid`, `ild.fvc-mcid`, and `methodology.daynes_6mwd_mid_2025`.

## Fallback designs

RCTs and protocols (CONSORT/SPIRIT), prediction models (TRIPOD+AI), qualitative, economic, quality-improvement, Mendelian randomisation, and non-randomised intervention studies keep core's reporting route. Add only the design-independent subdomain content. For Mendelian randomisation reporting, see `methodology.strobe_mr_2021`.

## Measurement and reporting standards evidence

The evidence rows cited above are rendered with source, edition, evidence tag, verification date, and freshness caveat in [the evidence appendix](design_methodology_evidence.md).
