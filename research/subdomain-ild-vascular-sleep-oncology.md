# Respiratory subdomain standards: ILD, pulmonary vascular, sleep, thoracic oncology

Ticket: `.scratch/ro-respiratory-medicine/issues/13-respiratory-subdomain-parenchymal-vascular-sleep-oncology.md` (primary working tree, untracked).
Branch: `research/subdomain-ild-vascular-sleep-oncology` (throwaway; based on `main` @ e614b32).
Extends: `research/respiratory-methodology-inventory` (ticket 04). Nothing from ticket 04 is repeated here. Its spirometry/DLCO/lung-volume/field-walking-test standards, RECORD family, Romania/EU data sources and 6MWD-in-COPD MCID still apply to these four subdomains.
Researched: 2026-10-10.

**Verification tags used below**

- **[PM]**: bibliographic record (authors, journal, year, volume, pages, DOI) checked against PubMed E-utilities in this session. The DOI resolved to that PMID.
- **[PM-abs]**: the quoted number or definition was also read in the PubMed abstract.
- **[web]**: the primary web page or PDF was fetched in this session and the quoted text read there.
- **[snippet]**: seen only in a search-engine snippet of a primary page that I could not fetch (403/503). Treat this as a lead to confirm, not as verified.
- **[UNVERIFIED]**: recalled from memory or from the full text without reading it this session. Confirm before encoding.

---

## Answer summary

1. **Every subdomain has a current, citable anchor set, and several changed recently.** Treat the following as live: the 2022 ATS/ERS/JRS/ALAT IPF + PPF guideline; the 2025 ERS/ATS update of the interstitial pneumonia classification; the 2026 ERS/EULAR CTD-ILD guideline; the 2022 ESC/ERS PH guideline plus the 2024 7th World Symposium (WSPH) definitions; the 2019 ESC PE guideline (the ESC lists a new PE guideline as *planned for 2027*), with the 2026 AHA/ACC PE guideline now a competing US reference; AASM Scoring Manual **v3 (Feb 2023)**; **TNM 9th edition** (IASLC proposals 2024; UICC book July 2025); RECIST 1.1/iRECIST; ESMO NSCLC 2023 (metastatic) and 2025 (early-stage); and **Lung-RADS v2022**.
2. **These subdomains are where definition drift does the most damage.** PH thresholds changed in 2022 (mPAP >20 mmHg, PVR >2 WU). PPF was defined only in 2022. IIP names changed in 2025 (e.g. AIP → idiopathic diffuse alveolar damage; DIP → alveolar macrophage pneumonia). TNM stage groups moved between the 8th and 9th editions. The AASM hypopnoea rule differs between manuals and payers. The profile must therefore demand an **edition/version stamp** on every definition, as ticket 04 already concluded for GOLD/GINA.
3. **MCIDs exist and are source-checkable for most core endpoints:** FVC in IPF 2–6% [PM-abs]; K-BILD total 3.9 [PM-abs]; 6MWD in PAH ≈33 m [PM-abs]; EORTC QLQ-C30 10-point "moderate" band [PM-abs]. The Epworth MCID (Patel 2018) is a letter with no abstract, so its −2 value is **[UNVERIFIED]**.
4. **Romanian facts that make a difference for a paper:**
   - **OSA and driving.** Romania transposed Directive 2014/85/EU into Ordin MS 1162/2010, pt. 6¹ (inserted by OMS 1255/2015, in force 20 Oct 2015) with identical AHI thresholds and review intervals [web].
   - **CPAP reimbursement.** CNAS reimburses CPAP/BPAP under its own severity bands (moderate AHI 15–30, severe >30; mild <15 only if Epworth ≥10). Renewal is compliance-gated at ≥4 h/night on ≥70% of nights [web]. This is a different cut-point from AASM/EU (severe ≥30).
   - **Antifibrotics and PAH drugs.** Antifibrotics are reimbursed for **IPF only** (protocol L014AE, programme C2-P6.20). PAH drugs are reimbursed under CI01I-HTP (programme C2-P6.3) [web].
   - **Lung-cancer screening.** Romania now has an FSE+-funded **national lung-cancer screening project** (SMIS 346295, led by Institutul „Marius Nasta”, 26 Aug 2025 – 25 Oct 2029, 27,118-person target group, with its own screening register) [web]. Romania is **not** among the 12 SOLACE pilot countries [web].
5. **Profile implication:** add four subdomain packs (definitions + outcome/MCID table + reporting/technical standard + data sources + Romania notes). Add reviewer prompts that check the edition stamp, the classification system and the MCID source. All of this is overlay content and needs no core edit beyond what ticket 04 already flagged.

---

## Per-condition tables

### 1. Interstitial lung disease and sarcoidosis

| Element | Current anchor | Verification |
|---|---|---|
| IPF diagnosis + PPF definition/treatment | Raghu G et al. Idiopathic Pulmonary Fibrosis (an Update) and Progressive Pulmonary Fibrosis in Adults: An Official ATS/ERS/JRS/ALAT Clinical Practice Guideline. *Am J Respir Crit Care Med* 2022;205(9):e18-e47. doi:10.1164/rccm.202202-0399ST (PMID 35486072) | [PM-abs] |
| Prior IPF diagnosis guideline (UIP/HRCT pattern categories, still cited) | Raghu G et al. *Am J Respir Crit Care Med* 2018;198(5):e44-e68. doi:10.1164/rccm.201807-1255ST | [PM] |
| Fleischner IPF diagnostic criteria | Lynch DA et al. *Lancet Respir Med* 2018;6(2):138-153. doi:10.1016/S2213-2600(17)30433-2 | [PM] |
| IIP classification (**supersedes 2013**) | Ryerson CJ et al. Update of the international multidisciplinary classification of the interstitial pneumonias: an ERS/ATS statement. *Eur Respir J* 2025;66(6):2500158. doi:10.1183/13993003.00158-2025 (PMID 40774805). Predecessor: Travis WD et al. *AJRCCM* 2013;188:733-48. doi:10.1164/rccm.201308-1483ST | [PM-abs] |
| PPF expert consensus (non-ATS) | Rajan SK et al. *Eur Respir J* 2023;61(3):2103187. doi:10.1183/13993003.03187-2021 | [PM-abs] |
| Hypersensitivity pneumonitis | Raghu G et al. ATS/JRS/ALAT CPG. *AJRCCM* 2020;202(3):e36-e69. doi:10.1164/rccm.202005-2032ST | [PM] |
| CTD-ILD (Europe) | Antoniou KM et al. ERS/EULAR clinical practice guidelines for CTD-ILD. *Eur Respir J* 2026;67(1):2402533. doi:10.1183/13993003.02533-2024 (co-published *Ann Rheum Dis* 2026;85:22-60. doi:10.1016/j.ard.2025.08.021). 25 PICO + 28 narrative questions across SSc, RA, IIM, Sjögren, SLE, MCTD. One author is from Bucharest (Gheorghiu AM) | [PM-abs] |
| SARD-ILD (US) | Johnson SR et al. 2023 ACR/CHEST screening & monitoring guideline. *Arthritis Rheumatol* 2024;76:1201-13. doi:10.1002/art.42860; treatment: *Arthritis Rheumatol* 2024;76:1182-1200. doi:10.1002/art.42861. SSc-ILD treatment: Raghu G et al. ATS CPG. *AJRCCM* 2024;209:137-52. doi:10.1164/rccm.202306-1113ST | [PM] |
| Interstitial lung abnormalities (ILA) | Hatabu H et al. Fleischner position paper. *Lancet Respir Med* 2020;8:726-737. doi:10.1016/S2213-2600(20)30168-5. **Updated by** Podolanczuk AJ et al. ATS Clinical Statement. *AJRCCM* 2025;211(7):1132-55. doi:10.1164/rccm.202505-1054ST | [PM-abs] |
| Sarcoidosis treatment | Baughman RP et al. ERS clinical practice guidelines on treatment of sarcoidosis. *Eur Respir J* 2021;58(6):2004079. doi:10.1183/13993003.04079-2020 (12 recommendations, 7 PICOs) | [PM-abs] |
| Sarcoidosis diagnosis | Crouser ED et al. ATS CPG. *AJRCCM* 2020;201(8):e26-e51. doi:10.1164/rccm.202002-0251ST | [PM] |
| Sarcoidosis trial end-points | Baughman RP et al. Delphi study. *Eur Respir J* 2025;66(4):2500943. doi:10.1183/13993003.00943-2025. Consensus end-points: prednisone reduction ≥50% or discontinuation; ≥10% predicted improvement in FVC%, FEV1% or DLCO%; KSQ Lung and General Health domains | [PM-abs] |
| Staging/prognosis (IPF) | GAP index: Ley B et al. *Ann Intern Med* 2012;156:684-91. doi:10.7326/0003-4819-156-10-201205150-00004 | [PM] |

**Definitions and severity**

- **PPF** (2022): in a patient with an ILD other than IPF, ≥2 of 3 criteria (worsening symptoms, radiological progression, physiological progression) within the past year, with no alternative explanation [PM-abs]. Physiological thresholds: absolute FVC decline ≥5% predicted or DLCO decline ≥10% predicted within 1 year **[UNVERIFIED: full text]**.
- **IPF HRCT patterns** (UIP / probable UIP / indeterminate / alternative) per the 2018 and 2022 guidelines **[UNVERIFIED: category names recalled]**.
- **2025 IIP classification:** adds secondary causes; adds bronchiolocentric interstitial pneumonia as a major pattern; renames AIP → idiopathic diffuse alveolar damage and DIP → alveolar macrophage pneumonia; splits fibrotic from non-fibrotic; makes diagnostic confidence explicit [PM-abs].
- **ILA vs ILD** (ATS 2025): ILA means non-dependent bilateral abnormalities involving ≥5% of a lung zone. ILD requires attributable symptoms, abnormal or declining function, fibrotic change in ≥5% of total lung volume, progression, or a specific fibrotic pattern [PM-abs].

**Outcomes and MCIDs**

| Outcome | Value | Source | Status |
|---|---|---|---|
| FVC % predicted (IPF), MCID | 2–6%; a 24-week decline of 5–10% carries >2× 1-year mortality | du Bois RM et al. *AJRCCM* 2011;184:1382-9. doi:10.1164/rccm.201105-0840OC | [PM-abs] |
| "Marginal" vs "significant" FVC decline | 5–10% vs >10% (DLCO 7.5–15% vs >15%) at 6 months | Zappala CJ et al. *Eur Respir J* 2010;35:830-6. doi:10.1183/09031936.00155108 | [PM-abs] |
| K-BILD total (ILD) | 3.9 points (anchor); domains 4.4–9.8 | Nolan CM et al. *Eur Respir J* 2019;54:1900281. doi:10.1183/13993003.00281-2019 | [PM-abs] |
| K-BILD (alternative estimates) | see source | Sinha A et al. *BMJ Open Respir Res* 2019;6:e000363. doi:10.1136/bmjresp-2018-000363; Prior TS et al. *Respir Res* 2020;21:91. doi:10.1186/s12931-020-01359-3 | [PM] (values not read) |
| 6MWD (IPF) | commonly cited 24–45 m | du Bois RM et al. *AJRCCM* 2011;183:1231-7 | **[UNVERIFIED]**: DOI 10.1164/rccm.201007-0980OC did not resolve in PubMed this session |
| Sarcoidosis lung function | ≥10% predicted improvement (consensus trial end-point, not an MCID) | Baughman 2025 Delphi (above) | [PM-abs] |

**Registries:** European IPF Registry (eurIPFreg): Guenther A et al. *Respir Res* 2018;19:141. doi:10.1186/s12931-018-0845-5 [PM]. No Romanian centre was listed among its affiliations in the abstract I checked. Romanian national ILD/IPF registry: **none found**.

### 2. Pulmonary vascular disease (PH and PE)

| Element | Current anchor | Verification |
|---|---|---|
| PH guideline | Humbert M et al. 2022 ESC/ERS Guidelines for the diagnosis and treatment of pulmonary hypertension. *Eur Heart J* 2022;43(38):3618-3731. doi:10.1093/eurheartj/ehac237; *Eur Respir J* 2023;61(1):2200879. doi:10.1183/13993003.00879-2022 | [PM] |
| PH definitions/classification (latest) | Kovacs G et al. Definition, classification and diagnosis of pulmonary hypertension (7th WSPH). *Eur Respir J* 2024;64(4):2401324. doi:10.1183/13993003.01324-2024 | [PM-abs] |
| PAH risk stratification (follow-up) | COMPERA 2.0 four-stratum model: Hoeper MM et al. *Eur Respir J* 2022;60(1):2102311. doi:10.1183/13993003.02311-2021 (WHO-FC, 6MWD, BNP/NT-proBNP) | [PM-abs] |
| CTEPH | Delcroix M et al. ERS statement on CTEPH. *Eur Respir J* 2021;57(6):2002828. doi:10.1183/13993003.02828-2020 | [PM] |
| Acute PE (Europe) | Konstantinides SV et al. 2019 ESC Guidelines… acute pulmonary embolism (with ERS). *Eur Heart J* 2020;41(4):543-603. doi:10.1093/eurheartj/ehz405. ESC publication schedule lists a new **PE guideline planned for 2027** (chairs Becattini, Klok) | [PM]; schedule [web] |
| Acute PE (US, newest) | 2026 AHA/ACC/ACCP/ACEP/CHEST/SCAI/SHM/SIR/SVM/SVN Guideline for… Acute Pulmonary Embolism in Adults. *Circulation* 2026;153(12):e977-e1051. doi:10.1161/CIR.0000000000001415 (erratum doi:10.1161/CIR.0000000000001462). Introduces "AHA/ACC Acute PE Clinical Categories" | [PM-abs] |
| PE prognosis scores | PESI: Aujesky D et al. *AJRCCM* 2005;172:1041-6. doi:10.1164/rccm.200506-862OC. sPESI: Jiménez D et al. *Arch Intern Med* 2010;170:1383-9. doi:10.1001/archinternmed.2010.199 | [PM] |
| Bleeding outcome definition (trials) | ISTH major bleeding: Schulman S, Kearon C. *J Thromb Haemost* 2005;3:692-4. doi:10.1111/j.1538-7836.2005.01204.x | [PM] |

**Definitions:** PH means mPAP >20 mmHg at RHC. Pre-capillary PH: PAWP ≤15 and PVR >2 WU. Isolated post-capillary: PAWP >15, PVR ≤2. Combined: PAWP >15, PVR >2. Exercise PH: mPAP/CO slope >3 mmHg/L/min. Five clinical groups are retained [PM-abs, Kovacs 2024]. ESC 2019 PE severity runs high / intermediate-high / intermediate-low / low **[UNVERIFIED: recalled]**. The 2026 AHA/ACC categories are a different scheme, so a paper must say which one it uses.

**Outcomes/MCIDs:** 6MWD in PAH MID ≈33 m (distributional 25.1–38.5 m; anchor 38.6 m): Mathai SC et al. *AJRCCM* 2012;186:428-33. doi:10.1164/rccm.201203-0480OC [PM-abs]. Time to clinical worsening, risk-stratum change (COMPERA 2.0), and emPHasis-10 PRO **[UNVERIFIED: no MCID source checked]**.

**Registries:** COMPERA (e.g. Vizza CD et al. *Chest* 2021;160:678-89. doi:10.1016/j.chest.2021.02.012) [PM]. Romania: national PAH treatment programme. Marius Nasta's programme page quotes ~15 patients/million prevalence and 2.4/million/yr incidence [web] (these are literature figures, not Romanian registry data). The Romanian Society of Pneumology hosts a page titled "Registrul Național de Hipertensiune Pulmonară" (srp.ro, **not fetched**). A patient-association site says the programme was approved by OMS 1386/2008 (**secondary, unverified**).

### 3. Sleep-disordered breathing

| Element | Current anchor | Verification |
|---|---|---|
| Scoring rules | AASM Manual for the Scoring of Sleep and Associated Events, **Version 3** (released 15 Feb 2023). AASM-accredited facilities had to implement it by 31 Dec 2023. Citation form: Troester MM, Quan SF, Berry RB et al. AASM, Darien IL, 2023. https://aasm.org/clinical-resources/scoring-manual | [web] |
| Respiratory-event rule rationale | Berry RB et al. Rules for scoring respiratory events in sleep: update of the 2007 AASM Manual. *J Clin Sleep Med* 2012;8(5):597-619. doi:10.5664/jcsm.2172 | [PM] |
| Diagnostic testing | Kapur VK et al. AASM CPG for diagnostic testing for adult OSA. *J Clin Sleep Med* 2017;13(3):479-504. doi:10.5664/jcsm.6506. PSG or technically adequate HSAT for uncomplicated patients; PSG if HSAT negative/inconclusive; PSG for significant cardiorespiratory/neuromuscular disease, opioids, stroke etc.; questionnaires must not be used alone to diagnose | [PM-abs] |
| PAP therapy | Patil SP et al. AASM CPG. *J Clin Sleep Med* 2019;15(2):335-343. doi:10.5664/jcsm.7640 | [PM] |
| ERS: non-CPAP therapy | Randerath W et al. *Eur Respir Rev* 2021;30(162):210200. doi:10.1183/16000617.0200-2021 | [PM] |
| ERS: OSA beyond AHI | Randerath W et al. Challenges and perspectives in OSA (ERS SDB group). *Eur Respir J* 2018;52(3):1702616. doi:10.1183/13993003.02616-2017 | [PM] |
| ERS: driving | Bonsignore MR et al. ERS statement on sleep apnoea, sleepiness and driving risk. *Eur Respir J* 2021;57(2):2001272. doi:10.1183/13993003.01272-2020 (prompted by the EU regulations; one co-author is from UMF Carol Davila) | [PM-abs] |
| ERS: telemedicine | Verbraecken J et al. ERS statement on advanced telemedicine for OSA (e-Sleep). *Eur Respir J* 2025;66. doi:10.1183/13993003.00557-2025 | [PM] |
| ERS/ESRS: central sleep apnoea | Randerath WJ et al. *Eur Respir J* 2025;66. doi:10.1183/13993003.00263-2025 | [PM] |
| Classification | ICSD-3-TR (AASM, 2023) | Existence confirmed via indexed papers that cite it; primary not fetched |
| Alternative severity metric | Hypoxic burden: Azarbarzin A et al. *Eur Heart J* 2019;40:1149-57. doi:10.1093/eurheartj/ehy624 | [PM] |
| Screening questionnaires | ESS: Johns MW. *Sleep* 1991;14:540-5. doi:10.1093/sleep/14.6.540. STOP: Chung F et al. *Anesthesiology* 2008;108:812-21. doi:10.1097/ALN.0b013e31816d83e4 (the STOP questionnaire paper; STOP-Bang is introduced in it **[UNVERIFIED]**) | [PM] |

**Definitions/severity:**

- **EU (Directive 2014/85/EU, Annex III §11.2):** moderate OSA syndrome = AHI 15–29; severe = AHI ≥30, both *with excessive daytime sleepiness*. Licence may be issued once the condition is controlled and treatment adherence is confirmed by authorised medical opinion. Review every ≤3 years (group 1) or ≤1 year (group 2) [web: legislation.gov.uk copy of the directive; EUR-Lex ELI https://eur-lex.europa.eu/eli/dir/2014/85].
- **Romania:** Ordin MS 1162/2010 (republished 29 Dec 2017), Annex pt. 6¹.1–6¹.4, reproduces these thresholds and intervals word for word in Romanian. It was inserted by OMS 1255/2015, in force 20 Oct 2015 [web: hospital-hosted consolidated PDF, spitalvn.ro; **official legislatie.just.ro text not fetched**].
- **CNAS reimbursement bands (CPAP/BPAP):**
  - Adults: mild AHI <15 (reimbursable only if highly symptomatic, Epworth ≥10), moderate 15–30, severe >30. Children: 1–5 / 5–10 / ≥10.
  - Diagnosis must come from polygraphy/PSG done within the last 3 years. Prescriptions run ≤90/91/92 days, renewable after a compliance-card read showing ≥4 h/night on ≥70% of nights [web: cnas.ro "Anexa CPAP-BPAP", Nov 2024].
- **AASM hypopnoea rule:** v3 recommends ≥30% flow drop with ≥3% desaturation or arousal, and accepts ≥4% desaturation as an alternative **[UNVERIFIED: recalled; manual is paywalled]**. Adult AHI bands 5/15/30 **[UNVERIFIED for AASM; EU 15/30 verified]**.

**Outcomes/MCIDs:** ESS MCID −2 points: Patel S et al. *AJRCCM* 2018;197:961-3. doi:10.1164/rccm.201704-0672LE [PM; letter, no abstract, **value UNVERIFIED**]. CPAP adherence ≥4 h/night (also the CNAS rule above [web]). FOSQ **[not checked]**.

**Registries:** ESADA (ERS CRC since 2015; established 2007 under EU COST; ~50,000 patients from 30 academic centres). The CRC is **co-chaired by Stefan Mihaicuta (UMF Victor Babeș, Timișoara, Romania)** [web: ersnet.org]. ESADA is the most direct European comparator dataset for Romanian OSA cohorts.

### 4. Thoracic oncology

| Element | Current anchor | Verification |
|---|---|---|
| TNM stage groups, 9th ed. | Rami-Porta R et al. IASLC Lung Cancer Staging Project: proposals for revision of the TNM stage groups (9th ed.). *J Thorac Oncol* 2024;19(7):1007-27. doi:10.1016/j.jtho.2024.02.011 | [PM-abs] |
| M descriptors | Fong KM et al. *J Thorac Oncol* 2024;19(5):786-802. doi:10.1016/j.jtho.2024.01.019 | [PM-abs] |
| STAS as histologic descriptor | Travis WD et al. *J Thorac Oncol* 2024;19(7):1028-51. doi:10.1016/j.jtho.2024.03.015 | [PM-abs] |
| Database | Asamura H et al. *J Thorac Oncol* 2023;18:564-75. doi:10.1016/j.jtho.2023.01.088 | [PM] |
| UICC book | Brierley JD, Giuliani M, O'Sullivan B, Rous B, Van Eycken E (eds). *TNM Classification of Malignant Tumours*, 9th ed. Wiley, 2025 (ISBN 978-1-394-21687-1). UICC launch announcement 3 July 2025. UICC errata Oct 2025 include a lung item | [web] |
| Histology | 2021 WHO Classification of Thoracic Tumours (5th ed.). Summary: Nicholson AG et al. *J Thorac Oncol* 2022;17:362-87. doi:10.1016/j.jtho.2021.11.003 | [PM] |
| Post-neoadjuvant pathology (MPR/pCR) | Travis WD et al. IASLC recommendations. *J Thorac Oncol* 2020;15(5):709-40. doi:10.1016/j.jtho.2020.01.005. % viable tumour / necrosis / stroma summing to 100% [PM-abs]. MPR ≤10% viable tumour **[UNVERIFIED: full text]** | [PM-abs] |
| Response criteria | RECIST 1.1: Eisenhauer EA et al. *Eur J Cancer* 2009;45:228-47. doi:10.1016/j.ejca.2008.10.026. iRECIST: Seymour L et al. *Lancet Oncol* 2017;18:e143-52. doi:10.1016/S1470-2045(17)30074-8 | [PM-abs] |
| ESMO early/locally advanced NSCLC (**supersedes 2017**) | Zer A et al. *Ann Oncol* 2025;36:1245-62. doi:10.1016/j.annonc.2025.08.003. Predecessor: Postmus PE et al. *Ann Oncol* 2017;28(suppl 4):iv1-iv21. doi:10.1093/annonc/mdx222 | [PM] |
| ESMO metastatic NSCLC | Oncogene-addicted: Hendriks LE et al. *Ann Oncol* 2023;34:339-57. doi:10.1016/j.annonc.2022.12.009. Non-oncogene-addicted: Hendriks LE et al. *Ann Oncol* 2023;34:358-76. doi:10.1016/j.annonc.2022.12.013. ESMO also maintains "living guideline" updates online (**not checked**) | [PM] |
| ESMO SCLC | Dingemans AC et al. *Ann Oncol* 2021;32:839-53. doi:10.1016/j.annonc.2021.03.207. No newer ESMO SCLC CPG found in PubMed. A third-party site claims an "ESMO 2026" SCLC version (**unverified**) | [PM] |
| Screening evidence | NLST: *N Engl J Med* 2011;365:395-409. doi:10.1056/NEJMoa1102873. NELSON: de Koning HJ et al. *N Engl J Med* 2020;382:503-13. doi:10.1056/NEJMoa1911793 | [PM] |
| EU screening policy | Council Recommendation of 9 December 2022 on strengthening prevention through early detection (2022/C 473/01), CELEX 32022H1213(01). For lung cancer: stepwise feasibility and implementation studies of LDCT, integrating primary and secondary prevention, starting with heavy current and former smokers | [web: EUR-Lex] |
| European screening statements | Oudkerk M et al. European position statement on lung cancer screening. *Lancet Oncol* 2017;18:e754-66. doi:10.1016/S1470-2045(17)30861-6. Incidental findings: O'Dowd EL et al. ERS/ESTS/ESTRO/ESR/ESTI/EFOMP statement. *Eur Respir J* 2023;62:2300533. doi:10.1183/13993003.00533-2023. ESTI nodule management: Snoeckx A et al. *Eur Radiol* 2026;36:135-47. doi:10.1007/s00330-025-11648-4 (with Prokop M et al. *Eur Radiol* 2026;36:122-34. doi:10.1007/s00330-025-11647-5) | [PM-abs] |
| Nodule reporting | Lung-RADS v2022 (released Nov 2022): Christensen J et al. *Chest* 2024;165:738-53. doi:10.1016/j.chest.2023.10.028 (co-published *J Am Coll Radiol* 2024;21:473-88). Incidental nodules: MacMahon H et al. Fleischner 2017. *Radiology* 2017;284:228-43. doi:10.1148/radiol.2017161659 | [PM-abs] |
| EU screening implementation | SOLACE (EU4Health): 37 partners, 15 countries, pilots in 12: Croatia, Czechia, Estonia, France, Germany, Greece, Hungary, Ireland, Italy, Netherlands, Poland, Spain. **Romania is not a pilot site** [web: HaDEA, 1 Aug 2025]. Overview: Kauczor HU et al. *Insights Imaging* 2024;15:252. doi:10.1186/s13244-024-01814-5 | [web], [PM] |
| Staging procedure (newest) | Korevaar DA et al. ERS/ESGE/ESTS CPG on EBUS/EUS for diagnosis and staging. *Eur Respir J* 2026;68. doi:10.1183/13993003.00097-2026 | [PM] |

**Key 9th-edition changes:**

- N2 split into N2a (single ipsilateral mediastinal or subcarinal station) and N2b (multiple stations).
- M1c split into M1c1 (one extrathoracic organ system) and M1c2 (multiple).
- Stage regrouping: T1N1 → IIA, T1N2a → IIB, T3N2a → IIIA, T2aN2b/T2bN2b → IIIB; M1c1/M1c2 both stay IVB.
- STAS added as a histologic descriptor.

All of the above is [PM-abs]. Effective date for 9th-ed. use: UICC book July 2025 [web]. IASLC/AJCC implementation from 1 Jan 2025 **[UNVERIFIED]**.

**Outcomes/MCIDs:**

- OS, PFS and ORR per RECIST 1.1. Progression = ≥20% increase in sum plus ≥5 mm absolute; max 5 target lesions (2 per organ); nodes measurable at ≥15 mm short axis [PM-abs].
- EORTC QLQ-C30 change bands: "a little" ≈5–10, "moderate" ≈10–20, "very much" >20 points (Osoba D et al. *J Clin Oncol* 1998;16:139-44. doi:10.1200/JCO.1998.16.1.139) [PM-abs].
- Lung module QLQ-LC29 (supersedes LC13): Koller M et al. *Lancet Oncol* 2020;21:723-32. doi:10.1016/S1470-2045(20)30093-0 [PM-abs].

**Romania:**

- **Burden and context:** Olteanu GE et al. Lung Cancer in Romania. *J Thorac Oncol* 2024;19(11):1492-1503. doi:10.1016/j.jtho.2024.08.003 [PM; full text 403]. Per a snippet of its full text [snippet]: >10,000 lung-cancer deaths in 2022, a cumulative death risk of 3.3%, and "the country lacks a formal screening program".
- **Registry gap:** Olteanu GE et al. Addressing the unmet need for a comprehensive lung cancer registry in Romania. *Front Oncol* 2023;13:1211533. doi:10.3389/fonc.2023.1211533 [PM-abs].
- **National cancer plan:** Legea 293/2022 approves the Planul național de prevenire și combatere a cancerului (legislatie.just.ro DetaliiDocument/261246; search-indexed, **not fetched**).
- **National screening project** "Screeningul Cancerului Pulmonar – Program Național de Detectare Precoce", cod SMIS 346295 [web: marius-nasta.ro; UMFCD press release 3 Dec 2025]:
  - Funding: FSE+ Programul Sănătate, contract 98945/26.08.2025; total 82.03 M lei.
  - Partners: lead Institutul „Marius Nasta”, with INSP, UMF „Carol Davila”, Centrul pentru Politici și Servicii de Sănătate and ARAS.
  - Timeline: 26.08.2025 – 25.10.2029.
  - Deliverables: a screening methodology, a smoking-cessation counselling guide, a dedicated digital screening register, and 774 staff trained, for a 27,118-person target group.
  - Not yet found: eligibility criteria (age/pack-years) and the nodule-management protocol (Lung-RADS vs ESTI vs other).
- The 2022 JTO CR&R paper "Implementing Lung Cancer Screening in Europe: Taking a Systems Approach" names Romania with Poland, Croatia and Italy as having committed to LDCT implementation [snippet; not verified].

---

## Findings with citations (cross-cutting)

1. **Version-stamping is unavoidable in all four subdomains.** At least one anchor changed in each: IIP classification 2013 → 2025 [Ryerson 2025]; ILA definition Fleischner 2020 → ATS 2025 [Podolanczuk 2025]; ESMO early NSCLC 2017 → 2025 [Zer 2025]; TNM 8 → 9 [Rami-Porta 2024; UICC 2025]; AASM manual v2.x → v3 [AASM web]. One more change is pending: the ESC PE guideline is planned for 2027 [ESC schedule, web]. Papers that compare cohorts across these boundaries (e.g. PH prevalence before and after 2022, stage shift between TNM8 and TNM9) need an explicit reclassification or sensitivity statement. The reviewer agent should prompt for it.
2. **Romanian reimbursement rules define cohorts.**
   - CNAS antifibrotic protocol L014AE covers IPF only. Nintedanib: all IPF stages. Pirfenidone: mild–moderate IPF, non-smoker ≥3 months. Both need diagnosis ≤5 years old and FEV1/FVC > LLN [web: protocol text via formaremedicala.ro copy; CNAS Jan 2025 protocol list confirms L014AE → C2-P6.20].
   - The 2022 international guideline conditionally recommends nintedanib for PPF [PM-abs]. Romanian real-world antifibrotic cohorts may therefore be IPF-only for administrative rather than clinical reasons. I found no CNAS PPF protocol (absence not proven).
   - CPAP access depends on the CNAS severity bands and the adherence gate [web]. Romanian "CPAP adherence" studies are partly measuring a reimbursement threshold.
3. **OSA severity cut-points disagree across three Romanian-relevant sources:** EU/Romanian driving law (moderate 15–29, severe ≥30, both require EDS) [web]; CNAS (moderate 15–30, severe >30) [web]; AASM (5/15/30) [UNVERIFIED]. A paper should name its source for severity bands and its hypopnoea rule (3% or arousal vs 4%).
4. **US vs European PE references now diverge.** The 2026 AHA/ACC guideline introduces its own clinical categories [PM-abs]. ESC 2019 remains the European reference until the planned 2027 update [web]. For Romanian authors submitting to EU journals, ESC 2019 is the default, with the AHA/ACC categories reported only as a secondary scheme.
5. **Romanian leadership in European collaborations is a usable data pathway.** ESADA CRC co-chair is in Timișoara [web]; a Bucharest rheumatologist co-authored the 2026 ERS/EULAR CTD-ILD guideline [PM-abs]; the Marius Nasta–led screening project builds its own register [web].

---

## Open uncertainties

1. **PPF physiological thresholds, IPF HRCT category labels, ESC 2019 PE risk classes, AASM v3 hypopnoea rule, MPR ≤10%, 6MWD-in-IPF MCID, ESS MCID −2.** All recalled, not read this session. Confirm from the full texts (AASM manual is paywalled).
2. **Official Romanian legal texts.** The OSA driving rule was read in a hospital-hosted consolidated copy of Ordin 1162/2010, and L014AE in a formaremedicala.ro copy. Fetch legislatie.just.ro and the current CNAS protocol compilation (e.g. `cnas.ro/wp-content/uploads/2025/08/Protocoale-terapeutice-august-2025.pdf`, not parsed) to confirm wording and currency.
3. **Romanian screening protocol details.** Eligibility (age, pack-years, quit-years), nodule management system and register data dictionary are not public on the pages I fetched. INSP returned 503, as it did in ticket 04.
4. **Romanian PH registry.** srp.ro names a "Registrul Național de Hipertensiune Pulmonară", but I found no publication describing it. Status and access are unknown.
5. **ESMO SCLC and metastatic NSCLC currency.** PubMed shows no post-2023 ESMO CPG for these. ESMO's living-guideline web updates were not checked (esmo.org returned 404 to scripted access).
6. **IASLC 9th-edition effective date** (1 Jan 2025) and whether Romanian pathology reporting has adopted TNM9: not verified.
7. **ICSD-3-TR**: primary publication not fetched; existence inferred from indexed papers that cite it.
8. **Burden numbers for Romania** (lung-cancer deaths, OSA prevalence, ILD prevalence): only the JTO snippet for lung cancer. ECIS/GLOBOCAN country figures were not pulled. Use the ticket-04 Eurostat/GBD routes.

---

## Implications for the profile

- **Four subdomain packs** in the `respiratory_medicine` overlay reference, each with these fields: `anchor_guideline` (with edition/year), `definitions` (with source), `severity_scheme` (named), `outcomes_mcid` (value + source + verification flag), `technical_reporting_standard`, `registries`, `romania_notes`. Mirror ticket 04's `edition`/`last_verified` fields. Add freshness checks for the AASM manual version, TNM edition, ESMO CPG dates and the ESC PE guideline (2027 trigger).
- **Reviewer prompts** (`domain_reviewer_agent` respiratory checklist, extending ticket 04):
  - ILD: is the 2022 PPF definition or the 2025 IIP terminology used? Is the FVC decline threshold stated as relative vs absolute % predicted?
  - PH: are the 2022/2024 haemodynamic thresholds used? Are pre-2022 cohorts reclassified? Which risk tool (COMPERA 2.0 / REVEAL)?
  - PE: which severity scheme (ESC 2019 vs AHA/ACC 2026)? Bleeding definition ISTH?
  - Sleep: scoring manual version, hypopnoea rule, device type (PSG vs HSAT), severity-band source, adherence definition.
  - Oncology: TNM edition; WHO 2021 histology; RECIST 1.1 vs iRECIST; QLQ-C30/LC29 with an interpretation threshold; screening-nodule system (Lung-RADS v2022 vs ESTI).
- **Romania notes block:** CNAS L014AE (IPF-only antifibrotics) and CI01I-HTP; CNAS CPAP bands and adherence gate; Ordin 1162/2010 pt. 6¹ driving rule; SMIS 346295 national screening project and its register; ESADA and eurIPFreg as European comparators. Each needs a "verify legal text currency" flag.
- **Reporting-guideline routing:** no new EQUATOR routes are needed. Screening and registry papers route through STROBE/RECORD (ticket 04), diagnostic HSAT/LDCT-AI papers through STARD/STARD-AI, and prognostic scores (GAP, PESI, COMPERA) through TRIPOD+AI. The overlay should name these pairings in the subdomain packs.
