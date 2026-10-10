# Respiratory subdomain standards: infection, occupational, rehab, critical care, interventional

Type: research
Status: resolved
Map: ../map.md

## Question

Which standards does the respiratory profile need for respiratory infections beyond TB basics (CAP/HAP/VAP ERS/ATS and ERS/ESICM guidelines, NTM ATS/ERS/ESCMID/IDSA 2020, COVID-19/post-COVID, influenza/RSV vaccination, AMR context in Romania), drug-resistant TB details (WHO 2022+ regimens, Romanian MDR-TB burden), occupational and environmental lung disease (silicosis, air pollution exposure reporting), smoking cessation/tobacco (Romanian prevalence, ENSP), pulmonary rehabilitation (ATS/ERS statement, outcomes), acute respiratory failure and ventilation (ERS/ATS NIV, Berlin/global ARDS definition), and interventional pulmonology (EBUS, ERS/ESGE guidance)? Same shape as the [Respiratory-medicine methodology inventory](04-respiratory-methodology-inventory.md) findings (branch `research/respiratory-methodology-inventory`): for each condition list the current guideline/statement with edition, disease definitions and severity classifications, standard outcome measures and MCIDs, condition-specific reporting or technical standards, key registries/data sources (Romania/EU where they exist), and Romania-specific facts (burden, national programmes, reimbursement-driven practice). Primary sources with checked DOIs. Don't repeat what ticket 04 already established; extend it.

## Answer

- **New 2025–26 documents:** ERS/ESGE/ESTS endosonography guideline 2026 (replaces Vilmann 2015), ERS 2026 core outcome set for pneumonia trials, WHO 2025 TB Module 4 (new 6-month DR-TB regimen), BEAT-Tuberculosis (NEJM 2026). New versions of the long-COVID guidance and the 2024 global ARDS definition.
- **Romania, from primary documents:**
  - **TB 2024:** 8,825 cases (46.3 per 100k); 200 RR/MDR (20 pre-XDR); 55.0% treatment success in the DR cohort.
  - **Antibiotic resistance:** CR-*Klebsiella* bloodstream infections rose from 7.12 to 20.31 per 100k (2019→2024). ECDC rates the data as low representativeness, so always caveat it.
  - **Other:** antibiotic use 24.2 DDD (EU 14.4); tobacco 30.7% (2018); flu vaccination among people 65+ 34.8%; air pollution about 7% of deaths (2019).
- **Walking-test MCIDs:** 6MWD 25 m and ISWT 48 m in respiratory patients (Daynes 2025 meta-analysis), confirming the 6MWD value the methodology inventory flagged.
- **Other standards covered:** CAP/HAP/VAP, NTM, COVID, vaccination, ILO 2022 radiograph classification, EU silica limit, smoking cessation, rehab, NIV/ARDS, interventional pulmonology.
- **Profile shape:** no new reporting-guideline routing needed; these areas need definition/outcome reference files, nine proposed reviewer prompts, and additions to the freshness list.
- **Evidence grades:** values are tagged *abstract-read*, *citation-only* or *unverified*; only abstract-read values should be encoded as facts.
- **Unverified:** Romanian silicosis counts (insp.gov.ro down), the ENSP edition, the Eurobarometer 2024 RO figure, the RSV vaccination policy, rehab reimbursement, CURB-65 items, Berlin severity bands, the NIV pH threshold.

Findings: branch `research/subdomain-infection-other` (commit `40169a8`), file `research/subdomain-infection-other.md` (worktree `/Users/val/dev/ars-research/subdomain-infection-other`).
