# Respiratory subdomain standards: airways disease

Ticket: `.scratch/ro-respiratory-medicine/issues/11-respiratory-subdomain-standards.md` (primary working tree; not edited here).
Branch: `research/subdomain-airways` (throwaway; based on `main` @ e614b32).
Extends: `research/respiratory-methodology-inventory.md` on branch `research/respiratory-methodology-inventory` (ticket 04). Ticket 04 already has the PFT technical standards (spirometry 2019, DLCO 2017, interpretation 2022, lung volumes 2023, oscillometry, FeNO 2005/2011, field walking tests, GLI equations), the GOLD 2026 and GINA 2026 landing URLs, the ATS/ERS asthma control and exacerbation definitions (Reddel 2009), the Cazzola 2008 COPD outcomes task force, and the MCIDs for SGRQ, CAT, trough FEV1, ACT and 6MWD. None of that is repeated below except where this note adds a correction or new verification.
Researched: 2026-10-10.

**How claims were checked.** Every DOI in this file was looked up in this session with PubMed E-utilities (`esearch` on `DOI[doi]`, then `esummary`). Author, journal, year, volume and pages come from those records. Where a number (an MCID, a cut-off) is quoted, the source column says whether it was read in the PubMed abstract, in the open full text (PMC, the GOLD/GINA PDFs, the CNAS/ANM PDFs), or is **unverified (memory)**. GOLD 2026 text was read from `GOLD-REPORT-2026-v1.3-8Dec2025_WMV2.pdf` and the pocket guide `GOLD-Pocket-Guide-2026-v1.1-20Nov2025_WMV2.pdf`. GINA 2026 text was read from `GINA-2026-Strategy-Report-WMS.pdf`. All three were downloaded from goldcopd.org and ginasthma.org on 2026-10-10. Romanian reimbursement facts come from official CNAS and ANMDMR PDFs. Figures embedded as images in those PDFs could not be read.

---

## Answer summary

1. **COPD: GOLD 2026 changed two things a reviewer must catch.** (a) **Group E now starts at one moderate exacerbation** in the previous year. Up to GOLD 2025 it was ≥2 moderate or ≥1 hospitalised. So any "GOLD E" cohort definition has to state which edition it uses. (b) GOLD 2026 adopts the **Rome proposal** to grade ECOPD severity at the point of care, using VAS dyspnoea, respiratory rate, heart rate, SaO2, CRP and ABG. The traditional mild/moderate/severe grading by healthcare use survives only as a trial-style post-hoc label. GOLD 2026 also renames CAT™ to **CAAT™** (Chronic Airways Assessment Test), with interchangeable scores, and adds a "disease activity" section with targets of **low disease activity, disease stability and disease control**.
2. **Asthma: GINA 2026 keeps the ERS/ATS 2014 concept of severe asthma.** It defines severe asthma as a subset of difficult-to-treat asthma: uncontrolled despite adherence to optimised high-dose ICS-LABA, or worsening when that dose is reduced. Biologic phenotyping rests on GINA's refractory Type-2 criteria (blood eosinophils ≥150/µL, FeNO ≥20 ppb, sputum eosinophils ≥2%, allergen-driven) and on the ERS/ATS 2020 cut-offs (eosinophils ≥150 for anti-IL-5; ≥260/µL plus FeNO ≥19.5 ppb for anti-IgE response). **ACQ MID 0.5** is now verified from two sources (Juniper 2005 abstract; GINA 2026). This closes an open item from ticket 04.
3. **Bronchiectasis has a new edition.** The **2025 ERS clinical practice guideline** (Chalmers et al., *ERJ* 2025;66:2501126) supersedes Polverino 2017. For clinical research, the exacerbation definition is Hill 2017: ≥3 of 6 symptoms worsening for ≥48 h, plus a clinician decides treatment must change. Severity is graded with **BSI** and **FACED**, PRO MID comes from **QOL-B** (Respiratory Symptoms scale, 8.0 points), and radiological diagnosis follows Aliberti 2022. **Romania is listed as an EMBARC member country.**
4. **CF: the ECFS standards are now a 2023–2024 four-paper series.** It replaces Castellani 2018 as the standards-of-care reference. Diagnosis still cites the CFF 2017 consensus (Farrell). CFQ-R Respiratory MCID is 4.0 when stable and 8.5 during an exacerbation. For Romania, CF sits in **national programme P6.4 "Mucoviscidoză"**, ELX/TEZ/IVA has been reimbursed since 2022, and newborn screening also started in 2022. Romania contributes data to the ECFS Patient Registry.
5. **AATD.** The current European document is still the **ERS 2017 statement** (Miravitlles), plus the 2024 EARCO Delphi on assessment and monitoring. The **EARCO** registry is the European data source. The CT lung-density endpoint comes from RAPID (Chapman 2015). ANMDMR's 2020 HTA of Respreeza recommended unconditional listing (80 points). **Whether a CNAS protocol now exists is unverified.**
6. **Chronic cough.** The ERS 2020 guideline (Morice) is still the current ERS document. No ERS update was found in PubMed for 2023–2026. It defines chronic cough as >8 weeks in adults and >4 weeks in children. **LCQ MID 1.3** is verified from the abstract. Cough assessment methodology is in the ERS 2007 assessment guideline.
7. **Romania, reimbursement drives the definitions.** CNAS protocols encode trial-style definitions that appear in Romanian real-world papers. Examples: dupilumab-for-COPD (eosinophils ≥300/µL, or ≥150/µL with exacerbation history; ≥2 moderate or ≥1 severe ECOPD), tezepelumab (GINA-defined severe asthma; response = ACT +3 or ACQ-6 −0.5 and no severe exacerbations at 4 months). A Romanian paper's inclusion criteria will often mirror these protocols rather than GOLD or GINA, and the profile should prompt authors to say which applies.

---

## Per-condition tables

Legend for the "Check" column: **PM-abs** = number read in the PubMed abstract; **FT** = read in open full text or the official PDF; **mem** = from memory, unverified.

### 1. COPD

| Item | Current document / value | Source (verified DOI) | Check |
|---|---|---|---|
| Strategy report | GOLD 2026 Report v1.3 (8 Dec 2025); Pocket Guide v1.1 (20 Nov 2025). Most recent GOLD executive summary in a journal: GOLD 2023 | Agustí A et al. *Eur Respir J* 2023;61(4):2300239. doi:10.1183/13993003.00239-2023 (PMID 36858443) | FT (GOLD PDFs) |
| Definition / diagnosis | Post-bronchodilator FEV1/FVC <0.7 "mandatory" for diagnosis. Pre-BD spirometry can *exclude* COPD | GOLD 2026 pocket guide, Diagnosis key points | FT |
| Precursors | **Pre-COPD**: symptoms and/or structural or functional abnormality without obstruction. **PRISm**: FEV1/FVC ≥0.7 with FEV1 <80% predicted, both post-BD | GOLD 2026 report, ch. 1 | FT |
| Airflow severity | GOLD grades 1–4 by post-BD FEV1 (Figure 2.10). Thresholds are in a figure image | GOLD 2026 | FT title only; thresholds **mem** (≥80/50–79/30–49/<30 %pred) |
| Combined assessment | ABE tool. **Group E now includes ≥1 moderate exacerbation in the previous year**. Symptom thresholds: mMRC ≥2 or CAAT™ ≥10 (SGRQ ≥25 equivalent) | GOLD 2026 report, ch. 2 ("Group E has been modified to include individuals with one moderate exacerbation in the previous year") | FT |
| Disease activity (new 2026) | Low disease activity = no exacerbations, no symptom worsening, no accelerated lung-function loss. "Disease stability" and "disease control" are defined separately | GOLD 2026 report, ch. 2 | FT |
| ECOPD definition | Acute event with dyspnoea and/or cough and sputum worsening over ≤14 days, possibly with tachypnoea and/or tachycardia | GOLD 2026 pocket guide; Celli BR et al. *Am J Respir Crit Care Med* 2021;204(11):1251-8. doi:10.1164/rccm.202108-1819PP (PMID 34570991) | FT |
| ECOPD severity (Rome) | **Mild**: VAS <5, RR <24, HR <95, SaO2 ≥92% and change ≤3%, CRP <10 mg/L. **Moderate**: ≥3 of 5 of VAS ≥5, RR ≥24, HR ≥95, SaO2 <92% and/or change >3%, CRP ≥10. **Severe**: as moderate plus ABG hypercapnia and acidosis (PaCO2 >45 mmHg, pH <7.35) | GOLD 2026 report Fig. 4.2 text; Rome proposal (above) | FT |
| Rome validation | Korean ED/inpatient cohort (n=740 events) | Lee HJ et al. *Ther Adv Respir Dis* 2023;17:17534666231172917. doi:10.1177/17534666231172917 (PMID 37338152) | PM-abs |
| Exacerbation management guideline | ERS/ATS 2017 | Wedzicha JA et al. *Eur Respir J* 2017;49(3):1600791. doi:10.1183/13993003.00791-2016 (PMID 28298398) | PM-abs |
| Core outcome set (ECOPD trials) | Survival, treatment success, breathlessness, QoL, ADL, need for higher care, ABG, disease progression, future exacerbations and admissions, safety, adherence | Mathioudakis AG et al. ERS statement. *Eur Respir J* 2022;59(5):2102006. doi:10.1183/13993003.02006-2021 (PMID 34649975) | PM-abs |
| Exacerbation PRO | EXACT-PRO | Leidy NK et al. *Am J Respir Crit Care Med* 2011;183(3):323-9. doi:10.1164/rccm.201005-0762OC (PMID 20813886) | DOI verified; MID not checked |
| CAT / CAAT™ | Original CAT validation; GOLD 2026 says CAT™ and CAAT™ scores are interchangeable | Jones PW et al. *Eur Respir J* 2009;34(3):648-54. doi:10.1183/09031936.00102509 (PMID 19720809) | DOI verified; interchangeability FT |
| mMRC | Validation as a disability measure | Bestall JC et al. *Thorax* 1999;54(7):581-6. doi:10.1136/thx.54.7.581 (PMID 10377201) | DOI verified |
| CCQ MCID | **0.4** (total score) | Kocks JW et al. *Respir Res* 2006;7:62. doi:10.1186/1465-9921-7-62 (PMID 16603063) | PM-abs |
| BODE | Multidimensional prognostic index | Celli BR et al. *N Engl J Med* 2004;350(10):1005-12. doi:10.1056/NEJMoa021322 (PMID 14999112) | DOI verified |
| Pulmonary rehab | ATS/ERS 2013 statement | Spruit MA et al. *Am J Respir Crit Care Med* 2013;188(8):e13-64. doi:10.1164/rccm.201309-1634ST (PMID 24127811) | DOI verified |
| Rehab core outcome set | COS for PR in COPD | Souto-Miranda S et al. *Thorax* 2023;78(12):1240-7. doi:10.1136/thorax-2023-220522 (PMID 37758457) | DOI verified; content not read |
| ICS eosinophil thresholds | <100 cells/µL little or no ICS effect; ≥300 cells/µL is the top of the continuous relationship. Initial LABA+LAMA+ICS in group E if eos ≥300 | GOLD 2026 report, ch. 3 and appendix | FT |

### 2. Asthma

| Item | Current document / value | Source | Check |
|---|---|---|---|
| Strategy report | GINA 2026. Executive summary: Reddel HK et al. *Am J Respir Crit Care Med* 2026 (epub 8 Oct). doi:10.1093/ajrccm/aamag542 (PMID 42847657). The 2026 key changes cover AIR options, severe asthma and biologic selection, and acute management | PM-abs + FT |
| Difficult-to-treat vs severe | Difficult-to-treat: uncontrolled despite medium/high-dose ICS-LABA, or needs high dose to stay controlled. **Severe**: uncontrolled despite adherence to optimised high-dose ICS-LABA plus management of contributory factors, or worsens when the dose is decreased. A "retrospective label" | GINA 2026 §8 | FT |
| ERS/ATS severe asthma definition | High-dose ICS plus a second controller and/or systemic CS needed to prevent loss of control, or uncontrolled despite this | Chung KF et al. *Eur Respir J* 2014;43(2):343-73. doi:10.1183/09031936.00202013 (PMID 24337046) | PM-abs |
| ERS/ATS severe asthma management | Anti-IL-5/5R if eos ≥150/µL; anti-IgE more likely to work if eos ≥260/µL and FeNO ≥19.5 ppb; tiotropium; macrolide trial; anti-IL-4R for eosinophilic or OCS-dependent asthma | Holguin F et al. *Eur Respir J* 2020;55(1):1900588. doi:10.1183/13993003.00588-2019 (PMID 31558662) | PM-abs |
| T2 phenotyping (GINA) | Consider refractory T2 inflammation if, on high-dose ICS or OCS: blood eos ≥150/µL, FeNO ≥20 ppb, sputum eos ≥2%, or clinically allergen-driven. Test before OCS or ≥1–2 weeks after. Look for other causes if eos ≥300/µL; if eos ≥1500/µL consider EGPA and similar | GINA 2026 §8 | FT |
| Biologics (EAACI) | GRADE recommendations per biologic and per outcome | Agache I et al. *Allergy* 2021;76(1):14-44. doi:10.1111/all.14425 (PMID 32484954) | PM-abs |
| Remission | Clinical remission = ≥12 months with no significant symptoms (validated tool), optimised/stable lung function, patient–clinician agreement, no systemic CS. Complete remission adds resolution of inflammation ± negative BHR | Menzies-Gow A et al. *J Allergy Clin Immunol* 2020;145(3):757-65. doi:10.1016/j.jaci.2019.12.006 (PMID 31866436). GINA 2026 discusses remission but does not fix one definition | PM-abs; FT |
| ACQ MID | **0.5** for ACQ-5, -6 and -7. Well-controlled ≤0.75; GINA recommends ACQ-5 | Juniper EF et al. *Respir Med* 2005;99(5):553-8. doi:10.1016/j.rmed.2004.10.008 (PMID 15823451); GINA 2026 §2 | PM-abs + FT (**resolves ticket-04 open item 2 for ACQ**) |
| AQLQ MID | 0.5 commonly cited | Juniper 1994 (not looked up) | **mem** |
| Registries | **ISAR** (global): ISAR Study Group. *Chest* 2020;157(4):805-14. doi:10.1016/j.chest.2019.10.051 (PMID 31838187). **SHARP** (ERS CRC, federated common data model): van Bragt JJMH et al. *ERJ Open Res* 2021;7(2):00064-2021. doi:10.1183/23120541.00064-2021 (PMID 33898615). SHARP remission analysis has a co-author from the National Institute of Pneumology, Bucharest: Fouka E et al. *Lancet Respir Med* 2026;14(8):659-72. doi:10.1016/S2213-2600(26)00141-4 (PMID 42341792) | PM-abs; Romanian affiliation from PubMed XML |

### 3. Bronchiectasis (non-CF, adult)

| Item | Current document / value | Source | Check |
|---|---|---|---|
| Guideline | **ERS clinical practice guideline 2025**: 8 PICO + 3 narrative questions. Strong for airway clearance, PR, long-term macrolide (high exacerbation risk), and inhaled antibiotics for chronic *P. aeruginosa*. Against routine ICS and long-term non-macrolide oral antibiotics | Chalmers JD et al. *Eur Respir J* 2025;66(6):2501126. doi:10.1183/13993003.01126-2025 (PMID 41016738). Clinical summary: *Breathe* 2026;22(2):260001. doi:10.1183/20734735.0001-2026 (PMID 41988091). Superseded: Polverino E et al. *Eur Respir J* 2017;50(3):1700629. doi:10.1183/13993003.00629-2017 (PMID 28889110) | PM-abs |
| Diagnosis (trials) | Radiological and clinical criteria, international consensus | Aliberti S et al. *Lancet Respir Med* 2022;10(3):298-306. doi:10.1016/S2213-2600(21)00277-0 (PMID 34570994) | DOI verified; criteria not extracted |
| Exacerbation (research) | Deterioration in ≥3 of: cough; sputum volume/consistency; sputum purulence; breathlessness/exercise tolerance; fatigue/malaise; haemoptysis, for ≥48 h, **and** clinician decides treatment must change | Hill AT et al. *Eur Respir J* 2017;49(6):1700051. doi:10.1183/13993003.00051-2017 (PMID 28596426) | PM-abs |
| Severity: BSI | Predictors include prior admissions, MRC ≥4, FEV1 <30%, *P. aeruginosa*, other colonisation, ≥3 lobes, age, BMI, ≥3 exacerbations. AUC 0.80 for mortality, 0.88 for hospitalisation | Chalmers JD et al. *Am J Respir Crit Care Med* 2014;189(5):576-85. doi:10.1164/rccm.201309-1575OC (PMID 24328736) | PM-abs |
| Severity: FACED | 0–7 points: FEV1 <50% (2), Age ≥70 (2), Chronic *P. aeruginosa* (1), Extension >2 lobes (1), Dyspnoea MRC >II (1). Outcome is 5-year mortality | Martínez-García MÁ et al. *Eur Respir J* 2014;43(5):1357-67. doi:10.1183/09031936.00026313 (PMID 24232697) | PM-abs |
| PRO MID | QOL-B Respiratory Symptoms **8.0 points** | Quittner AL et al. *Thorax* 2015;70(1):12-20. doi:10.1136/thoraxjnl-2014-205918 (PMID 25323621) | PM-abs |
| Registry | **EMBARC** (ERS CRC). 16,963 patients from 27 countries plus Israel, 2015–2022. Central/eastern Europe had more severe BSI (51.3% vs 35.1%) and more hospitalisations. **Romania listed as a participating country** | Chalmers JD et al. *Lancet Respir Med* 2023;11(7):637-49. doi:10.1016/S2213-2600(23)00093-0 (PMID 37105206); members page https://www.bronchiectasis.eu/embarc-members (HTTP 200, 2026-10-10) | PM-abs; FT |

### 4. Cystic fibrosis

| Item | Current document / value | Source | Check |
|---|---|---|---|
| Standards of care | ECFS 2023–2024 update, a four-paper series. (i) CFTR variant-specific therapy: Southern KW et al. *J Cyst Fibros* 2023;22(1):17-30. doi:10.1016/j.jcf.2022.10.002 (PMID 36916675). (ii) Establishing and maintaining health: Southern KW et al. *J Cyst Fibros* 2024;23(1):12-28. doi:10.1016/j.jcf.2023.12.002 (PMID 38129255). (iii) Recognising and addressing CF health issues: Burgel PR et al. *J Cyst Fibros* 2024;23(2):187-202. doi:10.1016/j.jcf.2024.01.005 (PMID 38233247). Previous edition: Castellani C et al. *J Cyst Fibros* 2018;17(2):153-78. doi:10.1016/j.jcf.2018.02.006 (PMID 29506920) | PM-abs ("second in a series of four"); **4th paper not identified** |
| Diagnosis | CFF consensus 2017 (sweat chloride thresholds) | Farrell PM et al. *J Pediatr* 2017;181S:S4-15.e1. doi:10.1016/j.jpeds.2016.09.064 (PMID 28129811) | DOI verified; thresholds **mem** (≥60 mmol/L CF; 30–59 intermediate) |
| Pulmonary exacerbation (trials) | Fuchs criteria (4 of 12 signs/symptoms) | Fuchs HJ et al. *N Engl J Med* 1994;331(10):637-42. doi:10.1056/NEJM199409083311003 (PMID 7503821) | DOI verified; criteria count **mem** |
| PRO MCID | CFQ-R Respiratory: **4.0 when stable, 8.5 during exacerbation** | Quittner AL et al. *Chest* 2009;135(6):1610-8. doi:10.1378/chest.08-1190 (PMID 19447923) | PM-abs |
| Technical standard | Multiple-breath washout / LCI consensus | Robinson PD et al. *Eur Respir J* 2013;41(3):507-22. doi:10.1183/09031936.00069712 (PMID 23397305) | DOI verified |
| Registry | **ECFS Patient Registry** (42 countries in the 2023 highlights; Romania present). 2024 Annual Data Report: Zolin A et al. 2026, Zenodo doi:10.5281/zenodo.20085096 (resolves, HTTP 200). Pan-European trend paper: Kerem E et al. *Eur Respir J* 2024;63(3):2301241. doi:10.1183/13993003.01241-2023 (PMID 38302155). It shows lower-income European countries did not share the FEV1 and survival gains seen elsewhere | FT; PM-abs |

### 5. Alpha-1 antitrypsin deficiency

| Item | Current document / value | Source | Check |
|---|---|---|---|
| European statement | ERS 2017: diagnosis and treatment of pulmonary disease in AATD. Calls for national/international registries and expert centres | Miravitlles M et al. *Eur Respir J* 2017;50(5):1700610. doi:10.1183/13993003.00610-2017 (PMID 29191952) | PM-abs |
| Earlier standard (still cited for testing) | ATS/ERS 2003 standards | *Am J Respir Crit Care Med* 2003;168(7):818-900. doi:10.1164/rccm.168.7.818 (PMID 14522813) | DOI verified |
| Monitoring consensus | EARCO Delphi: 38 pulmonologists, 15 countries. Agreement on spirometry, plethysmography, HRCT and augmentation start; disagreement on low-dose CT | Miravitlles M et al. *Respir Res* 2024;25(1):318. doi:10.1186/s12931-024-02929-5 (PMID 39160517) | PM-abs |
| Efficacy endpoint | CT lung density decline (RAPID RCT) | Chapman KR et al. *Lancet* 2015;386(9991):360-8. doi:10.1016/S0140-6736(15)60860-1 (PMID 26026936) | DOI verified |
| Other national/regional | Canadian Thoracic Society 2025 targeted testing and augmentation guideline: Hernandez P et al. *Chest* 2025;167(4):1044-63. doi:10.1016/j.chest.2024.08.037 | PubMed record |
| Registry | **EARCO** (ERS CRC) international registry; many 2022–2026 PubMed papers use EARCO data. No Romanian EARCO publication found | PubMed search | Romanian participation **unverified** |

### 6. Chronic cough

| Item | Current document / value | Source | Check |
|---|---|---|---|
| Guideline | ERS 2020, adults and children. No ERS update found in PubMed 2023–2026. Other recent documents: CICADA (Australia 2024), ABEA refractory chronic cough consensus 2026, KAAACI 2026 | Morice AH et al. *Eur Respir J* 2020;55(1):1901136. doi:10.1183/13993003.01136-2019 (PMID 31515408) | PM-abs |
| Definition | **>8 weeks in adults; >4 weeks in children** (3–8 weeks in children = "prolonged acute cough"). "Refractory" chronic cough for antitussive trials typically means >1 year | ERS 2020 full text (PMC6942543), "Definition of chronic cough" | FT |
| Assessment methodology | ERS 2007 guideline on cough assessment (cough challenge, objective monitoring, PROs) | Morice AH et al. *Eur Respir J* 2007;29(6):1256-76. doi:10.1183/09031936.00101006 (PMID 17540788) | DOI verified |
| PRO | LCQ (total 3–21): Birring SS et al. *Thorax* 2003;58(4):339-43. doi:10.1136/thorax.58.4.339 (PMID 12668799) | DOI verified |
| LCQ MID | **1.3** total; domains: physical 0.2, social 0.2, psychological 0.8 | Raj AA et al. *Handb Exp Pharmacol* 2009;(187):311-20. doi:10.1007/978-3-540-79842-2_16 (PMID 18825348) | PM-abs |
| Cough frequency MCID, cough VAS MCID | Not researched | — | open |

---

## Findings (Romania-specific, with citations)

**F1. COPD burden data are thin and mostly grey literature.**
- The first national spirometry prevalence study (CPSS with SRP scientific support, Mihălțan) ran July–August 2011. It used a nationally representative sample of 9,639 adults, and 23% of those tested by spirometry showed an obstructive pattern. Source: Botoșani Pneumophthisiology Hospital summary at pneumobt.ro, which was read. The study appears only as a book and a *CHEST* meeting abstract (journal.chestnet.org S0012-3692(16)55528-7, HTTP 403 to scripts). It is not in PubMed.
- Press reports put prevalence at **8.3% of adults over 40** from an SRP 2019 prevalence study. This is secondary (formaremedicala.ro and medichub.ro snippets); the primary report was not found.
- The profile should therefore send burden claims to GBD and Eurostat (ticket 04 data-source table) and flag national prevalence figures as non-peer-reviewed.

**F2. The Romanian Society of Pneumology publishes Romanian-language adaptations, not independent guidelines.**
- The SRP guidelines page (https://www.srp.ro/ghiduri/newindex.aspx, HTTP 200) lists:
  - GOLD 2017 and GINA 2020 pocket-guide translations
  - "Recomandări de diagnostic și tratament în BPOC 2019"
  - SRP–GOLD 2023 vaccination recommendations
  - SRAIC + SRP recommendations for severe asthma
  - Romanian-language AATD material, including European expert-group recommendations
- None is a GRADE guideline. Romanian papers normally cite GOLD and GINA directly, and the profile should accept that.

**F3. CNAS therapeutic protocols turn GOLD and GINA criteria into reimbursement rules.** The framework is Ord. MS/CNAS 564/499/2021, regularly amended (secondary: aopsnaj.ro snippet). The January 2026 CNAS list of modified protocols (https://cnas.ro/wp-content/uploads/2026/01/ALL-lista-protocoalelor-terapeutice-ianuarie-2026-pentru-site.pdf, read) contains two airway protocols:
- **D11AH05-BPOC, dupilumab for COPD**, sublist C1-G31H, cost-volume contract. Inclusion: GOLD-diagnosed COPD, age >18, on triple therapy (or LABA+LAMA if ICS is inappropriate), ≥2 moderate (systemic CS or antibiotic) or ≥1 severe (hospitalised) exacerbation in the previous year, and eosinophils ≥300/µL, or ≥150/µL with steroid-treated exacerbations. Response is reviewed at 52 weeks.
- **R03DX11, tezepelumab**, C1-G31H. Inclusion: GINA-defined severe asthma; ≥6 months of specialist follow-up on high-dose ICS+LABA with adherence and inhaler technique confirmed; ≥3 exacerbations in the previous year or chronic/intermittent OCS. Full response at 4 months = ACT +≥3 or ACQ-6 −≥0.5 (MCIDs used as reimbursement thresholds) **and** no severe exacerbations. Treatment continues only for complete or partial responders.
- Protocols for omalizumab, mepolizumab and benralizumab were not in this list (it covers only modified protocols). The full list of protocols in force was not retrieved.

**F4. CF: national programme and modulator access since 2022.**
- The ANMDMR HTA report for Kalydeco+Kaftrio (dossier submitted 07.07.2022; https://www.anm.ro/_/EVALUARE%20TEHNOLOGII%20MEDICALE/MUTARI/10005_2022_Kalydeco+Kaftrio.pdf, read) places CF drugs in **sublist C, section C2, programme P6 "boli rare și sepsis sever", subprogramme P6.4 "Mucoviscidoză"**. IVA was introduced by Ord. 1.206/233/2022 of 26 April 2022. The report includes a CNAS monitoring form completed by CF centres.
- Marinău et al. (*Children* 2026;13(9):1178. doi:10.3390/children13091178, PMID 42794198) report that newborn screening and national reimbursement of CFTR modulators both started in 2022, at the National CF Centre in Timișoara. Of their 46 patients, 84.8% were on modulators, median ppFEV1 was 99%, and the case-to-live-birth ratio in Bihor County was 1:7820.

**F5. AATD augmentation.** ANMDMR's HTA of Respreeza (human α1-proteinase inhibitor; report 17821, 09.11.2020) gave **80 points** and concluded the drug "meets the conditions for unconditional inclusion" in the reimbursed list. It also recommended drafting a therapeutic protocol. Source: https://www.anm.ro/_/EVALUARE%20TEHNOLOGII%20MEDICALE/17821_09.11.2020_Respreeza.pdf, read. Whether a CNAS protocol was then issued and is in force was not verified.

**F6. Severe asthma real-world evidence from Romania** is single-centre and retrospective.
- Mărginean C et al. *J Clin Med* 2026;15(6):2444. doi:10.3390/jcm15062444 (PMID 41899366). Târgu-Mureș, n=48, omalizumab, benralizumab and dupilumab, 24-month follow-up.
- The study defines its own remission composites: clinical = ACT ≥20, no severe exacerbations, no maintenance OCS; biological = FeNO <20 ppb and eos <150/µL.
- This is the heterogeneity the Menzies-Gow framework and GINA warn about. The profile should ask authors to cite the remission definition they used.

**F7. European network participation by Romania:**
- EMBARC: country list (F, table 3)
- ECFSPR: 2023 highlights (table 4)
- SHARP: Romanian co-author affiliation (table 2)
- EARCO: not found

These networks are the natural data sources for Romanian multicentre airway papers, alongside the national sources in ticket 04 (DRG, CNAS, INSP).

---

## Open uncertainties

1. **GOLD figure contents.** The GOLD 2026 grade thresholds (Fig. 2.10) and the exact ABE grid (Fig. 2.13) are images. The Group E change was read in the text, but the FEV1 grade cut-offs are from memory. Confirm them against the figure before encoding.
2. **GOLD 2026 hospitalised-ECOPD scale** (no respiratory failure / respiratory failure / ventilatory failure). GOLD presents it next to Rome, which makes it a second severity vocabulary. How reviewers should treat papers that use only the older healthcare-use grading (mild/moderate/severe by treatment) is a judgement call for the profile, not a rule.
3. **Complete list of CNAS respiratory protocols in force.** Not retrieved: omalizumab, mepolizumab, benralizumab, dupilumab-asthma, triple-therapy inhalers, roflumilast, CF drugs under P6.4, and AATD augmentation. https://www.protocoaleterapeutice.ro/ (third-party) claims 426 protocols in force. The official source is cnas.ro.
4. **Fourth ECFS 2023–2024 standards paper** not identified.
5. **CF diagnostic sweat-chloride thresholds and the Fuchs criteria count** are from memory.
6. **AQLQ MID, cough-frequency MCID, EXACT/E-RS MIDs, Bronchiectasis Impact Measure** not checked.
7. **Romanian national prevalence** (COPD 2011 and 2019; asthma). No peer-reviewed national estimate found in PubMed. School-based ISAAC-type studies exist only for Cluj and Bistrița.
8. **Romanian bronchiectasis and AATD epidemiology.** PubMed returned zero hits for Romania plus bronchiectasis or AATD in titles.
9. **Asthma and bronchiectasis core outcome sets** were not searched in COMET. Only the ECOPD COS (ERS 2022) and the COPD-PR COS were found.
10. **ERS chronic cough 2020** is assumed current because no successor was found in PubMed. The ERS website guideline list was not checked.

---

## Implications for the profile

- **Version-pinned definitions table.** The overlay should ship a per-condition table with fields `definition_source`, `edition`, `key_thresholds`, `last_verified`. GOLD changed Group E between 2025 and 2026, so a "GOLD E" label is ambiguous without an edition. The reviewer prompt should flag any GOLD or GINA classification given without an edition year.
- **ECOPD severity check.** If a COPD paper grades exacerbations, ask whether it uses the healthcare-use (post-hoc) grading or Rome/GOLD 2026, and whether Rome variables were collected prospectively. Point to the ERS 2022 ECOPD core outcome set for trial outcomes.
- **Severe-asthma check.** Require the definition source (GINA 2026, ERS/ATS 2014, or the CNAS protocol), the T2 biomarker thresholds and when they were sampled relative to OCS (GINA), and an explicit remission definition (Menzies-Gow framework or a stated variant).
- **MCID registry additions** (to ticket 04 table D), each with its source:
  - ACQ 0.5 (now verified)
  - CCQ 0.4
  - QOL-B Respiratory Symptoms 8.0
  - CFQ-R Respiratory 4.0 stable / 8.5 exacerbation
  - LCQ 1.3

  Mark the AQLQ value "unverified".
- **Severity scores as prediction models.** BSI and FACED are prognostic scores, so papers deriving or validating similar scores route to TRIPOD+AI and PROBAST+AI (already in core). The overlay only needs to name BSI and FACED as the reference comparators.
- **Romania reimbursement awareness.** Add a short `ro`-locale note: Romanian cohorts on biologics or CFTR modulators are selected by CNAS protocol criteria (cite the protocol code and the edition of Ord. 564/499/2021 amendments). Response definitions in those protocols, such as ACT +3 or ACQ −0.5 at 4 months, are reimbursement rules, not validated endpoints. Treat this as a selection-bias and external-validity prompt for the reviewer agent.
- **Data sources.** Add EMBARC, ECFSPR (Zenodo annual reports), SHARP/ISAR and EARCO to the ticket-04 data-source list, with "Romania participates: yes / yes / yes (via co-author) / unknown".
- **Freshness.** GOLD (November/December), GINA (May) and the ECFS registry (annual report in May) all revise every year. Reuse the freshness-check pattern proposed in ticket 04. The ERS bronchiectasis guideline (2025) and the ECFS standards (2023–2024) are multi-year documents that need only a `last_verified` date.
- **Scope.** All six conditions in the ticket have enough primary sourcing for a first overlay version. The Romanian epidemiology claims are weak (F1, open items 7–8). The profile should not offer national prevalence numbers as defaults.
