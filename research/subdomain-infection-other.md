# Respiratory subdomain standards: infection, occupational, tobacco, rehab, critical care, interventional

Ticket: `.scratch/ro-respiratory-medicine/issues/14-respiratory-subdomain-infection-and-other.md` (primary working tree, untracked).
Branch: `research/subdomain-infection-other` (throwaway; based on `main` @ e614b32).
Extends: `research/respiratory-methodology-inventory` (ticket 04). Items ticket 04 already established are not repeated: RECORD/RECORD-PE/STROME-ID, ATS/ERS PFT standards, 2014 field-walking-test standard, WHO TB definitions framework, WHO TB Module 4 2025 URL, post-TB lung disease clinical standards, INSP/ECDC/ERVISS/Eurostat/GBD data sources.
Researched: 2026-10-10.

**How claims were checked.** Every journal citation (authors, journal, year, volume, pages, DOI, PMID) comes from a PubMed E-utilities record fetched in this session. Where this note quotes numbers or content from a paper, it says whether that came from the **PubMed abstract** (verified here) or is **recalled** (not verified this session; confirm against the full text before encoding). Grey-literature URLs were fetched with `curl` in this session (HTTP 200 unless stated). Romanian figures come from documents downloaded and text-extracted in this session (ECDC/WHO TB country profile, EARS-Net and ESAC-Net reports, OECD country profile, GATS factsheet, ECDC vaccine scheduler).

---

## Answer summary

1. **Infections beyond TB need three guideline families and two outcome standards.** Guidelines: ATS/IDSA 2019 for CAP, ERS/ESICM/ESCMID/ALAT 2023 for severe CAP, and ERS/ESICM/ESCMID/ALAT 2017 with IDSA/ATS 2016 for HAP/VAP. For NTM, use the ATS/ERS/ESCMID/IDSA 2020 treatment guideline (diagnosis still rests on the 2007 ATS/IDSA criteria) and the NTM-NET 2018 outcome definitions. **New in 2026:** an ERS core outcome set (COS) for CAP and nosocomial-pneumonia trials (Fally 2026). For COVID, the WHO Clinical Progression Scale is the outcome standard and the WHO Delphi definition of post-COVID-19 condition is the case definition.
2. **Drug-resistant TB moved fast.** WHO's pre-XDR/XDR definitions changed in 2021. WHO Module 4 (April 2025) added a 6-month BDLLfxC regimen alongside BPaLM, plus modified 9-month regimens. All rest on trials whose primary reports PubMed confirms: TB-PRACTECAL, ZeNix, endTB, and BEAT-Tuberculosis (NEJM June 2026). Romania (ECDC/WHO 2026 report, 2024 data): 8,825 TB cases (46.3/100k), 200 notified RR/MDR-TB (3.8%) of which 20 were pre-XDR, and RR/MDR treatment success of only **55.0%** for the 2022 cohort.
3. **Occupational and environmental disease.** Standards: the ATS/ERS 2019 occupational-burden statement (population attributable fractions), the ILO radiograph classification (2022 revised edition), and the EU silica limit of 0.1 mg/m³ (Directive 2017/2398, text verified). For air pollution: the ERS/ATS 2017 "adverse effect" framework, the WHO AQG 2021, and the recast EU Ambient Air Quality Directive 2024/2881. Romania keeps a national occupational-disease register (Ordin 188/2004) and INSP publishes annual occupational-morbidity reports, but insp.gov.ro returned **503** again, so I could not read them.
4. **Tobacco.** For trial outcomes, use the Russell Standard (West 2005) and Hughes 2003. For guidelines, use the WHO 2024 tobacco-cessation guideline (URL verified); I did not verify the current ENSP guideline edition. Romania: GATS 2018 found current tobacco use of 30.7% (up from 26.8% in 2011). Law 15/2016 banned smoking in enclosed public places. The national Stop Fumat programme has run since 2007 (Marius Nasta, Tel Verde 0800 878 673), and GATS records that its funding was cut after 2011.
5. **Pulmonary rehabilitation.** Standards: ATS/ERS 2013 statement, ATS 2023 CPG (abstract verified: strong recommendation in COPD, after an exacerbation, in ILD and for telerehab; conditional in PH), and the ATS 2021 "modern PR" workshop. **New MIDs** (Daynes 2025 meta-analysis, abstract): 6MWD 25 m and ISWT 48 m in respiratory conditions, ESWT 159 s in COPD. These supersede the "recalled 25–33 m" flagged in ticket 04. CRQ MID 0.5 (Jaeschke 1989) is verified as a citation only.
6. **Acute respiratory failure and critical care.** NIV: ERS/ATS 2017. HFNC: ERS 2022. Home NIV: ERS 2019. ARDS has three live documents: Berlin 2012, the **Global definition 2024** (abstract: HFNO ≥30 L/min allowed, SpO₂/FiO₂ ≤315, ultrasound for imaging), ESICM 2023 and ATS 2024 CPGs. Outcome standards: ventilator-free-days reappraisal (Yehya 2019) and the ARF-survivor core outcome measures (Needham 2017). Weaning categories: Boles 2007.
7. **Interventional pulmonology.** The ERS/ESGE/ESTS endosonography guideline was **updated in August 2026** (Korevaar 2026, GRADE, 12 questions) and supersedes Vilmann 2015. Supporting documents: CHEST EBUS-TBNA technique (2016) and sample handling (2025), the Nashville bleeding-grade Delphi (2020), CHEST cryobiopsy (2020), and the BTS bronchoscopy guidelines (2011/2013). The 2026 guideline lists a Cluj co-author ("Leon Daniello"), so Romanian practice is represented in it.
8. **The profile can reuse a common shape.** Every subdomain below resolves to the same five fields: guideline edition, definitions/severity, outcomes+MID with source, reporting/technical standard, and data source. That is the same schema ticket 04 used, so the overlay needs one reference file per subdomain, not new machinery.

---

## Per-condition tables

Legend: **[A]** = content checked in the PubMed abstract this session; **[C]** = citation checked only, content recalled; **[U]** = unverified.

### 1. Community-acquired pneumonia (CAP)

| Field | Content |
|---|---|
| Guidelines | ATS/IDSA 2019: Metlay JP et al. *Am J Respir Crit Care Med* 2019;200:e45-e67. doi:10.1164/rccm.201908-1581ST (PMID 31573350). ERS/ESICM/ESCMID/ALAT **severe CAP** 2023: Martin-Loeches I et al. *Eur Respir J* 2023;61:2200735. doi:10.1183/13993003.00735-2022 (PMID 37012080); co-published *Intensive Care Med* 2023;49:615-32. doi:10.1007/s00134-023-07033-8, correction doi:10.1007/s00134-023-07082-z. [A: first international sCAP guideline, 8 questions, GRADE] |
| Definitions / severity | CURB-65: Lim WS et al. *Thorax* 2003;58:377-82. doi:10.1136/thorax.58.5.377 [C]. PSI: Fine MJ et al. *N Engl J Med* 1997;336:243-50. doi:10.1056/NEJM199701233360402 [C]. Severe-CAP major/minor criteria from IDSA/ATS 2007: Mandell LA et al. *Clin Infect Dis* 2007;44 Suppl 2:S27-72. doi:10.1086/511159 [C]. ATS/IDSA 2019 retains these criteria [U, recalled]. |
| Outcomes | **ERS COS for pneumonia trials:** Fally M et al. *Eur Respir J* 2026;68:2501926. doi:10.1183/13993003.01926-2025 (PMID 42276741). [A] CAP set: treatment success/failure, all-cause mortality, serious adverse events, readmission (admission for community trials), duration of symptoms, time to clinical stability (hospitalised). Mortality at 30 days from enrolment; readmission at 30 days post-discharge. |
| Reporting | No pneumonia-specific EQUATOR extension found. Use core CONSORT/STROBE plus COS adherence. |
| Data | ERVISS/ECDC (ticket 04). Paediatric note: IDSA/PIDS 2026 paediatric CAP updates (e.g. St Peter SD et al. *Clin Infect Dis* 2026, doi:10.1093/cid/ciag191) are out of scope for adult work. |

### 2. Hospital-acquired / ventilator-associated pneumonia (HAP/VAP)

| Field | Content |
|---|---|
| Guidelines | ERS/ESICM/ESCMID/ALAT 2017: Torres A et al. *Eur Respir J* 2017;50:1700582. doi:10.1183/13993003.00582-2017 (PMID 28890434) [A: GRADE, 7 PICO]. IDSA/ATS 2016: Kalil AC et al. *Clin Infect Dis* 2016;63:e61-e111. doi:10.1093/cid/ciw353 (PMID 27418577). Executive summary: *Clin Infect Dis* 2016;63:575-82. doi:10.1093/cid/ciw504. |
| Definitions | VAP-recurrence Delphi: Gaillet A et al. *Intensive Care Med* 2025;51:506-17. doi:10.1007/s00134-025-07856-7 [C]. The European and US guidelines differ (abstract of Torres 2017 notes "important differences between approaches in Europe and the USA"). Papers must say which definition they use. |
| Outcomes | Fally 2026 nosocomial COS [A]: treatment success/failure, all-cause mortality, SAEs, readmission, need for ventilatory support. |
| Romania context (AMR) | See §6 (AMR). |

### 3. Nontuberculous mycobacterial pulmonary disease (NTM-PD)

| Field | Content |
|---|---|
| Guideline | ATS/ERS/ESCMID/IDSA 2020: Daley CL et al. *Eur Respir J* 2020;56:2000535. doi:10.1183/13993003.00535-2020 (PMID 32636299); also *Clin Infect Dis* 2020;71:905-13 (summary). doi:10.1093/cid/ciaa1125 [A: 22 PICO, 31 recommendations, GRADE; covers MAC, *M. kansasii*, *M. xenopi*, *M. abscessus*]. |
| Diagnosis | The 2020 guideline covers treatment only. Diagnostic criteria are still those of ATS/IDSA 2007: Griffith DE et al. *Am J Respir Crit Care Med* 2007;175:367-416. doi:10.1164/rccm.200604-571ST [C]. |
| Outcomes | NTM-NET consensus outcome definitions (culture conversion, cure, microbiological cure, failure, recurrence): van Ingen J et al. *Eur Respir J* 2018;51:1800170. doi:10.1183/13993003.00170-2018 [C]. Refractory NTM-PD consensus: Moreira-Sousa D et al. *Eur Respir J* 2026;67. doi:10.1183/13993003.00400-2025 [C, not read]. |
| Romania | No Romanian NTM epidemiology found in PubMed (the one "Romania + NTM" hit is about bat guano). NTM-PD is probably under-ascertained alongside high TB incidence [U, inference]. |

### 4. COVID-19 and post-COVID-19 condition

| Field | Content |
|---|---|
| Acute guidelines | ERS living guideline: Chalmers JD et al. *Eur Respir J* 2021;57:2100048. doi:10.1183/13993003.00048-2021; update June 2022: Roche N et al. doi:10.1183/13993003.00803-2022. WHO living guideline on drugs for COVID-19: Agarwal A et al. *BMJ* 2020;370:m3379. doi:10.1136/bmj.m3379 (later versions exist; pin the version cited) [C]. |
| Outcome standard | WHO Clinical Progression Scale plus minimal outcome set: WHO Working Group. *Lancet Infect Dis* 2020;20:e192-7. doi:10.1016/S1473-3099(20)30483-7 [A: viral burden, survival (mortality at discharge or day 60), WHO Clinical Progression Scale]. |
| Post-COVID definition | WHO Delphi: Soriano JB et al. *Lancet Infect Dis* 2022;22:e102-7. doi:10.1016/S1473-3099(21)00703-9 [A: history of probable or confirmed infection, usually 3 months from onset, symptoms lasting ≥2 months, not explained by an alternative diagnosis]. |
| Follow-up / management | ERS statement on long-COVID follow-up: Antoniou KM et al. *Eur Respir J* 2022;60:2102174. doi:10.1183/13993003.02174-2021 [C]. ERS/ATS rehab interim guidance: Spruit MA et al. *Eur Respir J* 2020;56:2002197. doi:10.1183/13993003.02197-2020 [C]. **New:** Cao B et al. "Clinical practice guideline for long COVID prevention and treatment." *Eur Respir J* 2026 (Jul). doi:10.1183/13993003.02611-2025 (PMID 41856572) [A: GRADE, 10 recommendations, PREPARE-registered]. NICE NG188 (https://www.nice.org.uk/guidance/ng188, HTTP 200). |

### 5. Influenza / RSV vaccination (respiratory-risk groups)

| Field | Content |
|---|---|
| Evidence anchors | RSVPreF3 OA efficacy: Papi A et al. *N Engl J Med* 2023;388:595-608. doi:10.1056/NEJMoa2209604 [C]. I found no ERS vaccination guideline in PubMed for this question. Vaccination papers will cite national schedules and ECDC. |
| Romania schedule (ECDC Vaccine Scheduler, fetched) | Influenza: IIV3/IIV4/LAIV for children, IIV3/IIV4/QIV-HD for adults. Adults 45–65 without chronic conditions get 50% reimbursement; ≥65 get full reimbursement. Pneumococcal: PCV13/PCV15+PPSV23 or PCV20 in adults. **The Romania schedule lists no RSV vaccine.** |
| Romania coverage | OECD/European Observatory *State of Health in the EU: Romania Country Health Profile 2023*: **34.8%** of people ≥65 vaccinated against influenza in 2021, against an EU average of 50.8%. The ECDC 2023–24 recommendations survey lists Romania's risk-group recommendations, and influenza vaccines are 100% reimbursed for those aged <19. |

### 6. Antimicrobial resistance (AMR) context, Romania

| Indicator | Value | Source (fetched) |
|---|---|---|
| Carbapenem-resistant *K. pneumoniae* BSI, estimated incidence per 100k | Romania **7.12 (2019) → 20.31 (2024)**, +185.3%. EU 3.51 (2024) | ECDC *Antimicrobial resistance in the EU/EEA (EARS-Net) – AER 2024*, Table 7 |
| MRSA BSI incidence per 100k | Romania 13.72 (2019) → 13.15 (2024) | same, Table 6 |
| Representativeness caveat | Romania population coverage **15%**, representativeness "Low/Low/Low", blood-culture rate 32.9 sets/1,000 patient-days | same, Table 1 |
| Community antibiotic use | 24.2 DDD/1,000/day (2021) vs EU 14.4 | OECD Romania Country Health Profile 2023 |
| Antimycobacterials (J04A) | Romania 0.89 DDD/1,000/day, the EU/EEA maximum (EU mean 0.2), 2023 | ECDC ESAC-Net AER 2023 |
| National strategy | HG 1005/2023: *Strategia națională pentru prevenirea și limitarea infecțiilor asociate asistenței medicale și combaterea fenomenului de rezistență la antimicrobiene, 2023–2030* | legislatie.just.ro (search-indexed; direct fetch timed out) |

Profile implication: a Romanian HAP/VAP or sCAP paper that discusses empirical therapy should cite the EARS-Net country figures and disclose the 15% coverage limitation.

### 7. Drug-resistant TB (extends ticket 04 §E)

| Field | Content |
|---|---|
| Definitions | WHO 2021 pre-XDR/XDR: Viney K et al. *Eur Respir J* 2021;57:2100361. doi:10.1183/13993003.00361-2021 (PMID 33833074) [C: no abstract; recalled: pre-XDR = MDR/RR + fluoroquinolone resistance; XDR = pre-XDR + resistance to ≥1 further Group A drug (bedaquiline or linezolid)]. |
| WHO guideline | *WHO consolidated guidelines on TB, Module 4: treatment and care* (15 Apr 2025), https://www.who.int/publications/i/item/9789240107243 (HTTP 200). The WHO news release (fetched) says it adds a new 6-month **BDLLfxC** regimen for MDR/RR-TB with or without FQ resistance, keeps 6-month **BPaLM** (MDR/RR and pre-XDR, per the NCBI Bookshelf recommendation table), and adds **modified 9-month** regimens where FQ resistance is excluded. |
| Trials behind regimens | TB-PRACTECAL: Nyang'wa BT et al. *N Engl J Med* 2022;387:2331-43. doi:10.1056/NEJMoa2117166; long-term: *Lancet Respir Med* 2024;12:117-28. doi:10.1016/S2213-2600(23)00389-2. ZeNix: Conradie F et al. *N Engl J Med* 2022;387:810-23. doi:10.1056/NEJMoa2119430. endTB: Guglielmetti L et al. *N Engl J Med* 2025;392:468-82. doi:10.1056/NEJMoa2400327. **BEAT-Tuberculosis:** Conradie F et al. *N Engl J Med* 2026;394:2429-39. doi:10.1056/NEJMoa2503687 [A: 6-month BDLLfxC strategy non-inferior to 9-month SOC, success 86.1% vs 86.0%, margin 10 pp]. STREAM long-term: Goodall RL et al. *Lancet Respir Med* 2024;12:975-87. doi:10.1016/S2213-2600(24)00186-3. |
| EU care standard | ERS/ECDC *European Union standards for tuberculosis care, 2017 update*: Migliori GB et al. *Eur Respir J* 2018;51:1702678. doi:10.1183/13993003.02678-2017 [C]. |
| Outcomes | WHO 2021+ outcome definitions (ticket 04). Trial composite: cure/completion at end of treatment and at 76 weeks (BEAT [A]). |
| **Romania (ECDC/WHO *TB surveillance and monitoring in Europe 2026*, country profile, 2024 data)** | Population 19,067,576. TB cases **8,825 (46.3/100k)**; new + relapse 8,453 (44.3/100k); estimated 11,000 [9,300–14,000]; laboratory-confirmed 73.5%; DST results 80.1%. **Notified RR/MDR-TB 200 (3.8%)**, of which **pre-XDR 20**. Estimated RR-TB among bacteriologically confirmed pulmonary cases: 280 [260–310]. Treatment success: new culture-positive pulmonary (2023 cohort) **84.0%**; **RR/MDR-TB (2022 cohort) 55.0%**, died 19.4%, failed 14.4%, lost to follow-up 10.1%. URL: https://ecdc.europa.eu/sites/default/files/documents/Country-profile-Romania-TB-2024.pdf (the filename says 2024, the content is the 2026 report). Regional context (WHO Europe/ECDC release, 23 Mar 2026): EU/EEA 817 RR/MDR-TB cases, 3.5% of TB, 56% treatment success. |

### 8. Occupational lung disease (silicosis and others)

| Field | Content |
|---|---|
| Burden statement | ATS/ERS 2019: Blanc PD et al. *Am J Respir Crit Care Med* 2019;199:1312-34. doi:10.1164/rccm.201904-0717ST [C; recalled: gives population attributable fractions for asthma, COPD, IPF, etc.]. Update review: Murgia N et al. *Pulmonology* 2025;31:2416808. doi:10.1016/j.pulmoe.2024.03.004 [A: confirms the 2019 statement's findings]. |
| Radiographic classification | ILO *Guidelines for the use of the ILO International Classification of Radiographs of Pneumoconioses, revised edition 2022* (OSH Series 22; published 14 Feb 2023): https://www.ilo.org/publications/guidelines-use-ilo-international-classification-radiographs-pneumoconioses-1 (HTTP 200). Papers must say whether readers were ILO/B-reader certified [U: practice expectation]. |
| Silica review | Hoy RF, Chambers DC. *Allergy* 2020;75:2805-17. doi:10.1111/all.14202 [C] (engineered-stone silicosis). |
| Work-related asthma | Baur X et al. *Eur Respir Rev* 2012;21:125-39. doi:10.1183/09059180.00004711 [C]. No newer ERS occupational-asthma guideline found [U]. |
| Exposure limit | Directive (EU) 2017/2398 amending 2004/37/EC: respirable crystalline silica dust limit value **0.1 mg/m³** (Annex III, verified in EUR-Lex PDF). |
| Romania | Ordin MS 188/2004 set up the *Registrul operativ național al bolilor profesionale* and a national methodological centre [search-indexed via costelgilca.ro; official text not fetched]. INSP publishes annual *Morbiditatea profesională în România* (2022 and 2023 reports search-indexed at insp.gov.ro/download/…). **Fetch returned 503.** Content, including silicosis case counts, is unverified. |

### 9. Environmental exposure (air pollution) reporting

| Field | Content |
|---|---|
| Framework | ERS/ATS 2017 policy statement, "What constitutes an adverse health effect of air pollution?": Thurston GD et al. *Eur Respir J* 2017;49:1600419. doi:10.1183/13993003.00419-2016 [C]. |
| Reference levels | WHO global air quality guidelines 2021: https://www.who.int/publications/i/item/9789240034228 (HTTP 200; title verified) [C: annual PM2.5 AQG 5 µg/m³, recalled]. EU Directive (EU) 2024/2881 (ambient air quality, recast): https://eur-lex.europa.eu/eli/dir/2024/2881/oj (HTTP 200) [2030 limit values not read]. |
| Reporting | No EQUATOR guideline specific to air-pollution exposure was found this session. Use STROBE for cohort/case-crossover/time-series designs [U: consider ROSES/other; not checked]. A profile check should require pollutant, metric (annual mean / lag structure), exposure-assignment method (monitor, LUR, satellite), and the reference standard used (WHO AQG 2021 vs EU limit). |
| Romania | OECD Romania profile 2023: PM2.5 and ozone contributed to about **7% of deaths in 2019 (>17,000)** against an EU average of 4% (IHME source). EEA country estimates (secondary MDPI citation: 17,900 PM2.5 deaths in 2022) [U]. |

### 10. Smoking cessation / tobacco

| Field | Content |
|---|---|
| Trial outcome standard | Russell Standard: West R, Hajek P et al. *Addiction* 2005;100:299-303. doi:10.1111/j.1360-0443.2004.00995.x [C; recalled: 6-month continuous abstinence, biochemically verified, with a grace period]. Hughes JR et al. *Nicotine Tob Res* 2003;5:13-25 (PMID 12745503; no DOI in PubMed) [C]. |
| Guidelines | WHO *Clinical treatment guideline for tobacco cessation in adults* (2024): https://www.who.int/publications/i/item/9789240096431 (HTTP 200, title verified). ENSP *Tobacco and Nicotine Dependence Treatment Guidelines*: a newsletter refers to a "5th edition" [U: year and URL not verified]. |
| Romania prevalence | GATS Romania 2011 & 2018 comparison factsheet (INSP + MoH + WHO): current tobacco use **26.8% (2011) → 30.7% (2018)**; women 16.8% → 21.7%; 4,571 interviews, response rate 88.0%. OECD Romania profile 2023: about 1 in 5 adults smoked daily in 2019 (EHIS). Special Eurobarometer "Attitudes of Europeans towards tobacco and related products" (2024) exists (europa.eu/eurobarometer/surveys/detail/2995), but the page is JS-rendered and I did not get the Romania value. |
| Romania policy/programmes | Law 15/2016: smoke-free enclosed public places (GATS factsheet). *Subprogramul Național Stop Fumat*: since 2007, coordinated by Institutul „Marius Nasta”, Tel Verde 0800 878 673 (programme page fetched). GATS says cessation coverage fell after 2011 because of funding cuts. |

### 11. Pulmonary rehabilitation (PR)

| Field | Content |
|---|---|
| Statements / guidelines | ATS/ERS 2013 statement: Spruit MA et al. *Am J Respir Crit Care Med* 2013;188:e13-64. doi:10.1164/rccm.201309-1634ST [C]. ATS CPG 2023: Rochester CL et al. *Am J Respir Crit Care Med* 2023;208:e7-e26. doi:10.1164/rccm.202306-1066ST [A]. ATS workshop "Defining modern PR": Holland AE et al. *Ann Am Thorac Soc* 2021;18:e12-29. doi:10.1513/AnnalsATS.202102-146ST [C]. No ERS PR guideline newer than 2013 found [U]. |
| Outcomes + MIDs | **Daynes E et al. *Eur Respir Rev* 2025;34:240198. doi:10.1183/16000617.0198-2024** (erratum doi:10.1183/16000617.5198-2024) [A: anchor-based, exercise interventions. 6MWD **25 m (24–26)** respiratory; ISWT **48 m (39–57)** respiratory; ESWT **159 s (94–224)** COPD; pooled 6MWD 26 m, ISWT 53 m]. ISWT in COPD: Evans RA et al. *Thorax* 2019;74:994-5. doi:10.1136/thoraxjnl-2018-212725 [C]. CRQ MID 0.5: Jaeschke R et al. *Control Clin Trials* 1989;10:407-15. doi:10.1016/0197-2456(89)90005-6 [C]. CAT and SGRQ MIDs: ticket 04. |
| Romania | PubMed has almost no Romanian PR outcome studies (one ICF-based lung-cancer functional profile, *Rom J Morphol Embryol* 2025). CNAS reimbursement for PR not established [U]. |

### 12. Acute respiratory failure, ventilation, ARDS

| Field | Content |
|---|---|
| NIV (acute) | ERS/ATS CPG: Rochwerg B et al. *Eur Respir J* 2017;50:1602426. doi:10.1183/13993003.02426-2016 [A: 11 PICO including COPD exacerbation, cardiogenic oedema, de novo hypoxaemia, immunocompromised, trauma, palliation, post-op, weaning]. The pH threshold for COPD (recalled: pH ≤7.35) [U]. |
| HFNC | ERS CPG: Oczkowski S et al. *Eur Respir J* 2022;59:2101574. doi:10.1183/13993003.01574-2021 [C]. |
| Home NIV (COPD) | ERS: Ergan B et al. *Eur Respir J* 2019;54:1901003. doi:10.1183/13993003.01003-2019 [C]. |
| ARDS definitions | Berlin: ARDS Definition Task Force (Ranieri VM). *JAMA* 2012;307:2526-33. doi:10.1001/jama.2012.5669 [C; recalled severity bands mild 200–300, moderate 100–200, severe ≤100 mmHg PaO₂/FiO₂ with PEEP ≥5]. **Global definition 2024:** Matthay MA et al. *Am J Respir Crit Care Med* 2024;209:37-47. doi:10.1164/rccm.202303-0558WS [A: HFNO ≥30 L/min counts; PaO₂/FiO₂ ≤300 **or** SpO₂/FiO₂ ≤315 (if SpO₂ ≤97%); ultrasound accepted for bilateral opacities; in resource-limited settings no PEEP, flow or device requirement]. |
| ARDS guidelines | ESICM 2023: Grasselli G et al. *Intensive Care Med* 2023;49:727-59. doi:10.1007/s00134-023-07050-7 [C]. ATS 2024 update: Qadir N et al. *Am J Respir Crit Care Med* 2024;209:24-36. doi:10.1164/rccm.202311-2011ST [C]. |
| Weaning | ERS/ATS/ESICM/SCCM/SRLF conference: Boles JM et al. *Eur Respir J* 2007;29:1033-56. doi:10.1183/09031936.00010206 [C; simple/difficult/prolonged categories, recalled]. |
| Outcomes | Ventilator-free days: Yehya N et al. *Am J Respir Crit Care Med* 2019;200:828-36. doi:10.1164/rccm.201810-2050CP [C]. ARF-survivor core outcome measures: Needham DM et al. *Am J Respir Crit Care Med* 2017;196:1122-30. doi:10.1164/rccm.201702-0372OC [A: EQ-5D, SF-36v2 optional, HADS, IES-R reached consensus; no PFT measure recommended; 6MWT top-scoring for physical function without consensus]. Sepsis-3: Singer M et al. *JAMA* 2016;315:801-10. doi:10.1001/jama.2016.0287 [C]. |
| Romania | No Romanian ICU/ARDS registry identified [U]. |

### 13. Interventional pulmonology

| Field | Content |
|---|---|
| Endosonography (lung cancer) | **ERS/ESGE/ESTS CPG 2026:** Korevaar DA et al. *Eur Respir J* 2026;68:2600097. doi:10.1183/13993003.00097-2026 (PMID 42167778) [A: endosonography over mediastinoscopy for nodal staging; systematic over targeted staging; combined EBUS-TBNA+EUS(-B)-FNA preferred; no add-on mediastinoscopy after negative endosonography; 21G/22G standard; insufficient evidence for routine cryobiopsy; simulation-based competence]. Supersedes Vilmann P et al. *Eur Respir J* 2015;46:40-60. doi:10.1183/09031936.00064515 (also *Endoscopy* 2015). |
| Technique / sampling | CHEST: Wahidi MM et al. *Chest* 2016;149:816-35. doi:10.1378/chest.15-1216 [C]. CHEST sample acquisition/handling: Gilbert CR et al. *Chest* 2025;167:899-909. doi:10.1016/j.chest.2024.08.056 [C]. |
| Complication definitions | Bleeding after transbronchial biopsy (Nashville Delphi): Folch EE et al. *Chest* 2020;158:393-400. doi:10.1016/j.chest.2020.01.036 [C]. |
| Cryobiopsy (ILD) | CHEST: Maldonado F et al. *Chest* 2020;157:1030-42. doi:10.1016/j.chest.2019.10.048 [C]. Expert statement: Hetzel J et al. *Respiration* 2018;95:188-200. doi:10.1159/000484055 [C]. |
| General bronchoscopy | BTS diagnostic flexible bronchoscopy: Du Rand IA et al. *Thorax* 2013;68 Suppl 1:i1-44. doi:10.1136/thoraxjnl-2013-203618. BTS advanced: *Thorax* 2011;66 Suppl 3:iii1-21. doi:10.1136/thoraxjnl-2011-200713 [C]. |
| Pleural | ERS/EACTS malignant pleural effusion statement: Bibby AC et al. *Eur Respir J* 2018;52:1800349. doi:10.1183/13993003.00349-2018 [A: LENT score validated for prognosis; talc and IPC both effective]. |
| Reporting | Diagnostic-yield studies fall under STARD (core). No EBUS-specific reporting checklist found [U]. |
| Romania | Romanian EBUS series exist (e.g. Şimon M et al. *Rom J Morphol Embryol* 2017;58:79-87, no DOI in PubMed; Andrei GM et al. *J Clin Med* 2025;14:6179. doi:10.3390/jcm14176179). Korevaar 2026 lists a co-author from "Leon Daniello" Clinical Hospital of Pulmonology, Cluj (PubMed affiliation 18, truncated in my fetch). |

---

## Findings with citations (cross-cutting)

1. **Outcome standardisation exists for most subdomains, and the profile should prompt for it.** Pneumonia: Fally 2026 COS. NTM: van Ingen 2018. COVID: WHO 2020 minimal set. DR-TB: WHO outcome definitions plus 76-week trial composite. PR: Daynes 2025 MIDs. ARF survivors: Needham 2017. ICU: Yehya 2019 VFD. A paper that uses a non-COS outcome as primary should justify it. That is a reviewer prompt, not a hard rule.
2. **Definitions change version mid-literature.** Berlin 2012 → Global 2024 (ARDS); WHO XDR 2006 → 2021; WHO outcome definitions 2013 → 2021; NTM 2007 diagnosis vs 2020 treatment. The profile should store `definition_edition` for each and flag a paper that mixes cohorts across versions without saying so.
3. **Three 2025–26 documents were published after ticket 04 and need freshness tracking:** Korevaar 2026 (EUS), Fally 2026 (pneumonia COS), BEAT-Tuberculosis 2026, plus WHO Module 4 2025. GOLD and GINA already need the annual freshness check, and these belong on the same list.
4. **Romanian data quality caveats are themselves standards.** EARS-Net rates Romania's representativeness "Low", with 15% population coverage. INSP is unreachable to scripts. Romania's RR/MDR-TB success (55.0%) is below even the EU/EEA's already-low 56%. A Romanian manuscript should state these surveillance limits when it benchmarks against EU figures.

---

## Open uncertainties

1. **insp.gov.ro (503).** I could not read the occupational-morbidity reports (2022, 2023) or CNSCBT influenza/SARI reports. Silicosis counts in Romania remain unknown.
2. **Recalled content [C]** still needs full-text checks before encoding. That covers: CURB-65 items, the IDSA/ATS 2007 minor criteria, Berlin severity bands, the NIV pH threshold, Russell Standard details, the WHO AQG 5 µg/m³ value, the XDR definition wording, and the Boles weaning categories.
3. **ENSP guideline edition and year**, plus Eurobarometer 2024 Romania smoking prevalence (JS-rendered page): not obtained.
4. **Romania RSV policy.** The ECDC scheduler shows no RSV entry. Whether national RSV recommendations or reimbursement exist for older adults or pregnancy is unverified.
5. **PR in Romania.** Reimbursement pathway (CNAS) and availability not established. There are almost no Romanian PR outcome papers in PubMed.
6. **HG 1005/2023 AMR strategy.** Title confirmed via search index only; legislatie.just.ro timed out.
7. **Air-pollution reporting checklist.** I did not determine whether any EQUATOR-listed guideline covers exposure assessment.
8. **ATS/IDSA CAP update.** I did not see a 2025–26 adult update in PubMed (only paediatric IDSA/PIDS 2026). Recheck before release.
9. **Sleep, ILD and lung cancer** remain outside this ticket (as ticket 04 noted). Korevaar 2026 touches lung-cancer staging only.

---

## Implications for the profile

- **One reference file per subdomain** (infection, DR-TB, occupational/environmental, tobacco, rehab, critical care, interventional), using the five-field schema above, with `edition`, `verified_on` and a `[A]/[C]/[U]` status per value. Only `[A]` numbers (e.g. the Daynes MIDs, the Global ARDS thresholds, the Fally COS items) should ship as checkable facts. `[C]` items ship as citations with "see source".
- **Freshness list:** add WHO TB Module 4, the ERS/ESGE/ESTS EUS guideline, the Fally COS and the Global ARDS definition to the GOLD/GINA freshness mechanism proposed in ticket 04.
- **Reviewer prompts (`domain_reviewer_agent` respiratory checklist additions):** (a) pneumonia trial uses the ERS COS or justifies deviation; (b) ARDS paper names Berlin vs Global definition; (c) DR-TB paper names WHO definition year (2021 XDR) and regimen (BPaLM/BDLLfxC/9-month); (d) NTM paper uses 2007 diagnostic plus NTM-NET outcome definitions; (e) PR paper cites MID source (Daynes 2025); (f) cessation trial uses Russell Standard abstinence; (g) occupational imaging uses ILO 2022 classification; (h) air-pollution exposure: metric, assignment method and reference standard stated; (i) EBUS staging paper says whether staging was systematic or targeted (Korevaar 2026).
- **Romania locale facts (`ro` pack):** TB/RR-TB 2024 numbers and the 55% RR/MDR success figure (ECDC/WHO 2026); EARS-Net CRKP trend plus the low-representativeness caveat; community antibiotic use 24.2 DDD; GATS 2018 prevalence; Law 15/2016; Stop Fumat; influenza reimbursement rules and 34.8% coverage in people ≥65; air-pollution share of deaths (7%). Each needs a `source_year`, and the ECDC/EARS-Net items should refresh annually.
- **No new EQUATOR routing needed.** All subdomains route through core CONSORT/STROBE/STARD plus ticket 04's RECORD/STROME-ID add-ons. The new material is outcomes and definitions, not reporting checklists.
