# Respiratory subdomain standards: airways disease

Type: research
Status: resolved
Map: ../map.md

## Question

Which standards does the respiratory profile need for airways disease: COPD (GOLD 2026, exacerbation definitions incl. Rome proposal, ERS/ATS), asthma (GINA 2026, ERS/ATS severe asthma, biologics/T2 phenotyping, FeNO/eosinophils), bronchiectasis (ERS guidelines, EMBARC, BSI/FACED), cystic fibrosis (ECFS standards, registry), alpha-1 antitrypsin deficiency, and chronic cough (ERS 2020)? Same shape as the [Respiratory-medicine methodology inventory](04-respiratory-methodology-inventory.md) findings (branch `research/respiratory-methodology-inventory`): for each condition list the current guideline/statement with edition, disease definitions and severity classifications, standard outcome measures and MCIDs, condition-specific reporting or technical standards, key registries/data sources (Romania/EU where they exist), and Romania-specific facts (burden, national programmes, reimbursement-driven practice). Primary sources with checked DOIs. Don't repeat what ticket 04 already established; extend it.

## Answer

- **COPD (GOLD 2026):** Group E now starts at one moderate exacerbation, so every "GOLD E" cohort needs an edition year. GOLD adopts the Rome severity grading and renames CAT to CAAT (scores interchangeable). There is an ERS 2022 core outcome set for exacerbation trials.
- **Asthma (GINA 2026):** severe asthma is defined via optimised high-dose ICS-LABA. T2 cut-offs: eosinophils ≥150/µL, FeNO ≥20 ppb, sputum eosinophils ≥2%. The ACQ MCID of 0.5 is now confirmed, closing the open item from the methodology inventory. Registries: ISAR, SHARP (Romania participates).
- **Bronchiectasis:** ERS 2025 replaces ERS 2017. Hill 2017 exacerbation definition; BSI/FACED severity scores; QOL-B MCID 8.0. Romania is in EMBARC.
- **Cystic fibrosis:** ECFS standards 2023–24 series; CFQ-R MCID 4.0 stable / 8.5 in exacerbation. In Romania: national programme P6.4, CFTR modulators reimbursed, newborn screening since 2022, data sent to the ECFS registry.
- **AATD and chronic cough:** AATD references are ERS 2017 and the EARCO 2024 Delphi. Chronic cough: ERS 2020 (>8 weeks adults, >4 weeks children), LCQ MCID 1.3.
- **Romanian reimbursement:** CNAS protocols (e.g. dupilumab for COPD, tezepelumab with ACT +3 / ACQ −0.5 response rules) turn GOLD/GINA criteria into eligibility rules. Treat them as a selection-bias source, not as validated endpoints.
- **Unverified:** the GOLD FEV1 grade cut-offs (in a figure), the full list of CNAS protocols in force, Romanian prevalence (no peer-reviewed national estimate), the AQLQ MID, sweat-chloride thresholds and the Fuchs criteria.

Findings: branch `research/subdomain-airways` (commit `0f55175`), file `research/subdomain-airways.md` (worktree `/Users/val/dev/ars-research/subdomain-airways`).
