# Respiratory reviewer prompts

Ask the author:

- Which classification version and edition define the categories used? See `airways.gold-2026-group-e` and `thoracic_oncology.tnm9-uicc`.
- Which severity scheme was applied, and does its edition match the study period? See `airways.gold-2026-group-e` and `pulmonary_vascular.esc-pe-risk-classes`.
- What source supports the MCID, and is it appropriate to this population and instrument? See `airways.acq-mcid`, `ild.fvc-mcid`, and `methodology.daynes_6mwd_mid_2025`.
- Do included studies use different guideline editions or definitions? If so, make edition drift explicit rather than pooling silently.
- Were data obtained from routine records? If yes, ask whether RECORD is applicable (`methodology.record_2015`). For infectious-disease molecular epidemiology, check STROME-ID (`methodology.strome_id_2014`).
- Could CNAS reimbursement eligibility or renewal rules select the analysed patients? Treat this as a possible source of selection bias, not as a validated endpoint (`sleep.cnas-cpap-adherence`).
- What measurement standard and edition define the index test? For spirometry, check ATS/ERS and the equation used (`methodology.ats_ers_spirometry_2019`, `methodology.gli_race_neutral_2023`).

## Romanian manuscript-statement checks

Each missing item is **Conditional, never Critical**. Ask the author to confirm the statement:

- Does the ethics statement name the committee (CNBMDM or local) and give the approval number and date? (`ro.cnbmdm-ethics`, `ro.mdr-positive-opinion`)
- Is consent stated, or are anonymisation and the committee's decision described? Waiver wording is allowed only when the author declares that the committee said so. (`ro.patient-rights-research-consent`, `ro.patient-confidentiality`)
- For a CTR trial, is the EU CT number stated? (`ro.ctis-evaluation`)
- Are drug names INN-only? (`ro.cmr-publication-drug-name`)
- Is consent documented for every identifiable image? (`ro.patient-rights-images`)
- Is a conflict-of-interest disclosure present? (`ro.cmr-conflict-interest`)
