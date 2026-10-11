# Respiratory subdomain standards: ILD, pulmonary vascular, sleep, thoracic oncology

Type: research
Status: resolved
Map: ../map.md

## Question

Which standards does the respiratory profile need for interstitial lung disease (ATS/ERS/JRS/ALAT IPF and PPF 2022, sarcoidosis ERS 2021, FVC-decline MCID), pulmonary vascular disease (ESC/ERS 2022 PH guidelines, ESC 2019 PE), sleep-disordered breathing (AASM scoring manual, OSA definitions/AHI, ERS sleep statements; Romanian driving-licence OSA rules if any), and thoracic oncology (TNM 9th ed., IASLC, RECIST 1.1, ESMO NSCLC/SCLC, lung-cancer screening incl. EU/Romanian pilots, Lung-RADS)? Same shape as the [Respiratory-medicine methodology inventory](04-respiratory-methodology-inventory.md) findings (branch `research/respiratory-methodology-inventory`): for each condition list the current guideline/statement with edition, disease definitions and severity classifications, standard outcome measures and MCIDs, condition-specific reporting or technical standards, key registries/data sources (Romania/EU where they exist), and Romania-specific facts (burden, national programmes, reimbursement-driven practice). Primary sources with checked DOIs. Don't repeat what ticket 04 already established; extend it.

## Answer

- **ILD:** the IPF/PPF 2022 guideline is still current. ERS/ATS 2025 updates the IIP classification; there's ERS/EULAR 2026 for CTD-ILD and ATS 2025 for interstitial lung abnormalities. Sarcoidosis: ERS 2021 (treatment) and ATS 2020 (diagnosis).
- **Pulmonary vascular:** ESC/ERS 2022 plus WSPH 2024 (mPAP >20 mmHg, PVR >2 WU). For PE, ESC 2019 still applies in Europe (new edition expected 2027); AHA/ACC 2026 uses its own severity categories.
- **Sleep:** the AASM scoring manual is at v3 (2023).
- **Thoracic oncology:** TNM 9th edition (UICC book July 2025); ESMO 2025 for early-stage NSCLC; Lung-RADS v2022.
- **MCIDs read in abstracts:** FVC in IPF 2–6%; K-BILD 3.9; 6MWD in PAH about 33 m; QLQ-C30 bands 5–10 / 10–20 / >20. The Epworth MCID is unverified.
- **Romania:**
  - OSA driving rules copy the EU rule (AHI 15–29 moderate / ≥30 severe, plus sleepiness). CNAS CPAP reimbursement uses different bands and requires adherence ≥4 h on ≥70% of nights.
  - Antifibrotics are reimbursed for IPF only, not PPF; PAH drugs have their own national programme.
  - A national lung-cancer screening project led by Marius Nasta runs 2025–2029 (27,118 people targeted, own register). Romania is not a SOLACE pilot country.
  - ESADA is co-chaired from Timișoara.
- **Profile shape:** four subdomain packs, each definition with an edition stamp; reviewer prompts check the classification version, the severity scheme and the MCID source.
- **Unverified:** the PPF decline thresholds, the AASM hypopnoea rule, the ESC PE risk classes, the major pathologic response cut-off, the IPF 6MWD MCID, the official texts of the OSA driving order and the IPF protocol, and the screening eligibility rules.

Findings: branch `research/subdomain-ild-vascular-sleep-oncology` (commit `ed278ab`), file `research/subdomain-ild-vascular-sleep-oncology.md` (worktree `/Users/val/dev/ars-research/subdomain-ild-vascular-sleep-oncology`).
