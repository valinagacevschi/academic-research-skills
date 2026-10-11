# Romanian regulatory landscape for respiratory research

Resolves wayfinder ticket `.scratch/ro-respiratory-medicine/issues/01-romanian-regulatory-landscape.md`.
Retrieved/verified: 2026-10-10. Not legal advice. Every claim below cites the text it comes from. Where I could not read the controlling text, I say so.

**How I got the sources.** `legislatie.just.ro` (the official Portal Legislativ) refused every non-browser request from this environment (HTTP/2 stream reset or empty reply), and the browser tool was down. So I read copies hosted by the issuing or competent bodies: anm.ro, ms.ro, portal.just.ro, cmr.ro, plus EUR-Lex and the EDPB site. Some ms.ro/anm.ro files are consolidated prints made by commercial tools (G&G "Eurolex", "Lex Expert"). These are marked *consolidated-unofficial*. Before anyone writes a registry `authority_anchor` from one of them, re-check it against the Portal Legislativ link that is also given.

---

## 1. Answer summary

- **Interventional medicinal-product trials (most respiratory drug trials, e.g. inhaled therapies, biologics in asthma/COPD):** EU CTR 536/2014 applies directly. Romania implements it through **OUG 29/2022**, approved with amendments by **Law 249/2022**. **ANMDMR** is the competent authority and national contact point. It does the scientific review (Part I). The **CNBMDM** (Comisia Națională de Bioetică a Medicamentului și a Dispozitivelor Medicale) is the single national ethics body for CTR purposes. Everything is submitted through CTIS. The dossier is in Romanian, but documents not meant for subjects may be in English. Since 31 Jan 2023, initial applications go through CTIS only. **OMS 3390/2022** sets the recruitment and consent rules. Consent must be taken by a physician who is on the investigator team. The PI must be a specialist with more than 3 years in the specialty, or a *medic primar*.
- **Device clinical investigations (e.g. spirometers, ventilators, inhaler devices, digital respiratory monitors):** the EU MDR 2017/745 applies, together with **OUG 46/2021** and **OMS 330/2023**. Again CNBMDM gives the ethics opinion and ANMDMR the authorisation or validation. ANMDMR will not approve without a positive CNBMDM opinion.
- **Non-interventional / observational studies (retrospective chart reviews, registries, cohort studies):** no Romanian statute I found sets up one national approval route. Non-interventional PASS go through ANMDMR's pharmacovigilance directorate or PRAC. In practice, other observational studies are approved by a **local ethics committee**: the hospital's research ethics committee (*comisia de etică* of the hospital) or the university's research-ethics subcommission (Law 199/2023). The CMR Deontology Code (2025) requires an opinion from "CNBMDM **or** local ethics committees" before research on persons. The legal basis and powers of hospital research ethics committees are thinly regulated. This is the biggest open uncertainty.
- **Data protection:** the GDPR plus **Law 190/2018**. Law 190/2018 **Art. 8(1)** lets research processing derogate from GDPR Arts **15, 16, 18 and 21**, but only under Art. 89(1) safeguards and only to the extent strictly necessary. Law 190/2018 contains **no express research condition under GDPR Art. 9(2)(j)**. Health-data research without consent therefore needs some other identified Union or Member-State legal basis. This is unresolved in Romanian law (see §3). Law 190/2018 also restricts processing of the **CNP** (national ID number) (Art. 4) and health-data profiling or automated decision-making (Art. 3).
- **Patient-rights Law 46/2003:** **Art. 19** makes the patient's consent *mandatory* for participation in scientific research. **Arts. 21–22** make all information about the patient confidential, even after death. It may be disclosed only with explicit consent or where the law expressly requires it. The law contains **no research waiver**. Read literally, retrospective use of identifiable records without consent conflicts with Art. 22 unless the data are anonymised or another law "expressly requires" the disclosure. Practice (hospital and university committees approving retrospective studies on de-identified data) seems to depend on anonymisation, not on a statutory waiver.
- **Colegiul Medicilor (CMR):** the new Deontology Code (Hotărârea AGN CMR 2/2025, published in MO 1141/10.12.2025, in force 1 Jan 2026) binds every physician member. It requires an ethics opinion, express written consent, information about the right to withdraw, and adherence to Helsinki, Oviedo and the CTR. In publications it requires strict patient confidentiality and INN (DCI) drug names only.

---

## 2. Findings with citations

### 2.1 EU CTR 536/2014: interventional medicinal-product trials

| # | Fact | Source |
|---|---|---|
| CTR-1 | A "clinical trial" is a clinical study where assignment to a therapeutic strategy is decided in advance outside normal practice, **or** prescribing the IMP is decided together with inclusion, **or** extra diagnostic/monitoring procedures beyond normal practice are applied. A "non-interventional study" is a clinical study that is not a clinical trial. | CTR Art. 2(2)(1)–(4). https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0536 |
| CTR-2 | Conditions include risk/benefit justification, information under Art. 29(2)–(6), consent under Art. 29(1),(7),(8), and protection of privacy and data. | CTR Art. 28(1) (same URL) |
| CTR-3 | Simplified consent in **cluster trials** is available only where a single Member State allows it and it does not contradict national law. OUG 29/2022 and OMS 3390/2022 contain no provision allowing it (my inference from reading both texts in full: absence of authorisation). | CTR Art. 30(1), 30(3)(a); OUG 29/2022 (full text); OMS 3390/2022 |
| CTR-4 | Summary of results to the EU database **within 1 year** of the end of the trial in all MSCs, plus a lay summary (Annex IV/V). | CTR Art. 37(4) |
| CTR-5 | TMF archived for **at least 25 years**. Medical files are archived according to national law. | CTR Art. 58 |

### 2.2 Romanian implementation of the CTR: OUG 29/2022, Law 249/2022, OMS 3390/2022

Source PDF (ANMDMR-hosted, consolidated-unofficial print of MO 283/24.03.2022): https://www.anm.ro/_/STUDII%20CLINICE/OUG%2029-2022.pdf. Portal Legislativ: https://legislatie.just.ro/Public/DetaliiDocument/253151. Approving law: Law 249/2022, https://legislatie.just.ro/Public/DetaliiDocumentAfis/257765 (Chamber of Deputies record: https://www.cdep.ro/ords/pls/legis/legis_pck.htp_act?ida=187152).

| # | Fact | Provision |
|---|---|---|
| RO-CT-1 | **ANMDMR** is designated competent authority for interventional medicinal-product trials and national contact point for CTR Ch. II–III. | OUG 29/2022 Art. 2(1) |
| RO-CT-2 | **CNBMDM** is designated as the independent body (no legal personality) that carries out the ethics review and issues opinions under the CTR. Its composition and rules are set by ministerial order. | OUG 29/2022 Art. 2(2) |
| RO-CT-3 | Ethics review by CNBMDM, scientific review by ANMDMR. The decision is transmitted via **CTIS**. CNBMDM's ethics review covers Part I aspects (Art. 6 CTR) and Part II (Art. 7 CTR). Ethics review is based on ICH E6 GCP. | OUG 29/2022 Art. 3(2)–(4) |
| RO-CT-4 | Dossier submitted via CTIS **in Romanian**. Documentation not intended for subjects may be in English. | OUG 29/2022 Art. 4(1)–(2) |
| RO-CT-5 | Persons deprived of liberty and residents of residential-care institutions **may not be enrolled** in interventional trials in Romania. | OUG 29/2022 Art. 6(1) |
| RO-CT-6 | Mandatory sponsor insurance. CNBMDM assesses its adequacy. | OUG 29/2022 Art. 8 |
| RO-CT-7 | Personal-data processing in interventional trials follows the GDPR (no special national derogation in the OUG). | OUG 29/2022 Art. 9 |
| RO-CT-8 | Contraventions apply to unauthorised trials, unsuitable sites, **failure to publish information under CTR Art. 81**, and safety-reporting breaches. Fines run from 30,000 to 75,000 lei (up to 100,000 lei on repeat offences), and the trial can be suspended. ANMDMR enforces. | OUG 29/2022 Arts. 10–12 |
| RO-CT-9 | A refusal by ANMDMR/CNBMDM can be contested within 30 days, then taken to the administrative court. | OUG 29/2022 Art. 16 |
| RO-CT-10 | OMS 904/2006 (the old GCP rules under Directive 2001/20) applied only until 31 Jan 2025. ANMDMR authorises sites only for phase I and bioequivalence trials. | OUG 29/2022 Arts. 15, 18; ANMDMR notice 05.04.2022, https://www.anm.ro/medicamente-de-uz-uman/informatii-de-interes-pentru-sponsori/ |
| RO-CT-11 | Since **31.01.2023**, initial interventional-trial applications in Romania go **only via CTIS**. All Directive-era trials had to transition by 30 Jan 2025. | ANMDMR notices 27.01.2023 and transition notice (same URL) |
| RO-CT-12 | Recruitment channels are limited to a defined list (own patients, other specialists/GPs/pharmacists, posters, CNBMDM-pre-approved e-resources, nationally recognised patient organisations, health NGOs). Recruitment materials must be in Romanian. The procedure must comply with the GDPR. | OMS 3390/2022, Norms Art. 14. PDF: https://www.anm.ro/_/STUDII%20CLINICE/Ordin%203390-2022.pdf (published in MO 1088/11.11.2022) |
| RO-CT-13 | The person taking consent must be a **physician on the investigator team**, trained in the protocol and GCP. Minors able to form an opinion must give their **assent** in addition to the legal representative's consent. Incapacitated persons able to form an opinion sign together with the representative. | OMS 3390/2022, Norms Art. 15 |
| RO-CT-14 | **PI** must be a specialist physician with more than 3 years in the specialty, or a *medic primar*. Team members must come from listed professions. A pediatrician is mandatory in pediatric trials. The site-suitability form is signed by the PI, the head of department and the hospital manager. | OMS 3390/2022, Norms Art. 16 |

### 2.3 CNBMDM: composition and remit

- **OMS 80/2023** (MO 49/18.01.2023) approves CNBMDM's composition and Rules of Organisation and Functioning. PDF: https://www.anm.ro/_/ORDINE/OMS%20nr.%2080-2023.pdf. Portal Legislativ: https://legislatie.just.ro/public/DetaliiDocument/264000.
  - Art. 1: CNBMDM does the ethics review and issues opinions under the CTR as implemented by OUG 29/2022 and Law 249/2022. It must include at least one non-health-professional member representing patients.
  - Art. 2: 9 permanent members and 3 alternates, appointed by ministerial order.
  - Art. 5: its remit covers **interventional** medicinal-product trials (mono- or multicentre), **device clinical studies**, and proposals for "clinical pharmacology, **pharmacovigilance**, pharmacodynamics, physiopathology and pharmacokinetics" studies on human subjects. Art. 5(f) covers an opinion on the consent-form format, and Art. 5(h) recruitment methods and sites.
  - *Uncertainty:* the "pharmacovigilance … studies" wording in Art. 5(a)/(i) arguably reaches some non-interventional PASS. The Rules do not mention other observational studies (registries, chart reviews).
- **OMS 1157/2026** (MO 705/25.08.2026) replaced Annex 1 (membership list) of OMS 80/2023. I saw it through the infodosar.ro MO digest, https://www.infodosar.ro/monitorul-oficial/ministerul-sanatatii/329633-ordin-1157-2026. The functioning rules are unchanged as far as that digest shows, but I have not read the MO itself.
- Contact (from ANMDMR): http://www.bioetica-medicala.ro, secretariat@bioetica-medicala.ro. The CNBMDM site is behind a WAF that blocked this environment. Source: https://www.anm.ro/dispozitive-medicale/investigatii-clinice-si-studii-referitoare-la-performanta/

### 2.4 Medical-device clinical investigations

- **OMS 330/2023** (MO 120/13.02.2023) approves the methodological norms on clinical evaluation and device clinical investigations, issued under **OUG 46/2021** (the national framework for MDR 2017/745). PDF: https://www.anm.ro/_/DM/LEGISLATIE/Ordin%20330-2023.pdf
  - Norms Art. 4(1): CNBMDM does the ethics review as the MDR Art. 2(56) ethics committee. Art. 4(2): ANMDMR does the scientific review.
  - Norms Art. 16: class I and non-invasive class IIa/IIb investigations may start once ANMDMR validates the application **and** CNBMDM has given a positive opinion. Class III, invasive IIa/IIb and active implantables need ANMDMR authorisation **and** a positive CNBMDM opinion.
- ANMDMR states it approves device investigations and IVDR performance studies **only** with the CNBMDM ethics opinion. GCP follows EN ISO 14155 / ISO 20916. Source: https://www.anm.ro/dispozitive-medicale/investigatii-clinice-si-studii-referitoare-la-performanta/

### 2.5 Non-interventional studies and PASS

- Non-interventional PASS fall under EU pharmacovigilance law (Dir. 2010/84/EU, Impl. Reg. 520/2012) and Law 95/2006 Title XVIII, Ch. X. ANMDMR's Pharmacovigilance and Risk Management Directorate handles them. The protocol needs approval from the national competent authority or PRAC before the study starts. Interventional PASS fall under the CTR and Law 249/2022. Source: https://www.anm.ro/medicamente-de-uz-uman/farmacovigilenta/studii-de-siguranta-post-autorizare/
- I found **no** national act that requires ANMDMR or CNBMDM approval for a non-PASS observational study, such as an academic retrospective COPD cohort or an ILD registry. This is a negative finding with medium confidence (see §3).

### 2.6 Hospital and university ethics committees

- **OMS 1502/2016** (MO 1/03.01.2017) sets up the **Consiliul etic** in public hospitals. This is a hospital ethics/integrity council. It is *not* a research ethics committee. One of its duties is to give a **consultative opinion to "the hospital's ethics committee" (*comisia de etică din cadrul spitalului*) for each clinical study run in the hospital**, assessing ethical vulnerabilities, integrity and patient rights. Source: Art. 8(1)(n). Text read from the ms.ro-hosted MO copy: https://www.ms.ro/media/documents/OMS-1502_2017-COMPONENETA-ATRIBUTII-CONSILIUL-ETIC.pdf. Portal Legislativ: https://legislatie.just.ro/Public/DetaliiDocumentAfis/185429. This confirms that a separate hospital-level research *comisie de etică* exists in the regulatory model. The order does not define its legal basis. I have not checked later amendments to OMS 1502/2016.
- **Law 199/2023 on higher education**, Ch. XX "Etica și deontologia universitară": every university has a *comisie de etică universitară* (4-year mandate, independent), with a **research-ethics subcommission**. The subcommission covers publication and authorship, the dignity of research participants, research-data management, conflicts of interest, fraud and harm prevention. The article number is probably Art. 160. I inferred that from the PDF layout and have not verified it. Source: https://www.aracis.ro/wp-content/uploads/2024/10/legea-invatamantului-superior-nr-199-2023.pdf (Lege5 print, consolidated-unofficial).
- **Institutional practice (not law), as evidence of how retrospective studies are handled:**
  - UMF Cluj's research-ethics committee asks for the study type (prospective, retrospective, observational), the protocol, a data-processing agreement and a consent template. https://umfcluj.ro/programe-studii/doctorat/doctoranzi/comisia-etica-cercetarii-stiintifice/
  - UMFST Târgu Mureș (Board decision 28/09.11.2020) exempts student theses that *only* process data already recorded in institutional documents, with no prospective evaluation, provided confidentiality is respected. It **recognises the opinions of the SCJU/SCJ Târgu Mureș hospital ethics committees** for retrospective studies on existing records "with the identity of the patients obliterated". https://arhiva.umfst.ro/universitate/comisii-de-etica/comisia-de-etica-a-cercetarii-stiintifice/regulament-proceduri.html
- **Law 206/2004** on good conduct in research (CNECSDTI) governs research misconduct (fabrication, falsification, plagiarism). It is relevant at publication stage, not for prospective approval. I did not read it in full. Copy: https://cnecsdti.research.gov.ro/wp-content/uploads/cne/2016/lege-nr-206_27-05-2014.pdf

### 2.7 GDPR plus Law 190/2018

Source: Law 190/2018, MO 651/26.07.2018. PDF hosted by portal.just.ro: https://portal.just.ro/101/Documents/LEGE__190_2018_date_cu_caracter_personal.pdf. Portal Legislativ: https://legislatie.just.ro/Public/DetaliiDocument/203151. GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04/eng

| # | Fact | Provision |
|---|---|---|
| DP-1 | Processing of **genetic, biometric or health data for automated decision-making or profiling** is allowed only with explicit consent or under express legal provisions with appropriate safeguards. | Law 190/2018 Art. 3(1) |
| DP-2 | Health data processed for **public health** (as defined in Reg. 1338/2008) may not later be processed for other purposes by third parties. This matters for reusing surveillance data, e.g. TB registers. | Law 190/2018 Art. 3(2) |
| DP-3 | The **CNP** (national identification number) may be processed only under GDPR Art. 6(1) grounds. If the ground is legitimate interest, the law requires minimisation and security measures, a DPO, set retention periods, and staff training. | Law 190/2018 Art. 4 |
| DP-4 | Public-interest processing of personal and special data under GDPR Art. 6(1)(e) and Art. 9(2)(g) requires TOMs, a DPO where Art. 10 requires one, and retention limits. | Law 190/2018 Art. 6 |
| DP-5 | **Research derogation:** GDPR Arts. **15, 16, 18, 21** do not apply to scientific or historical research processing, to the extent those rights would make the research impossible or seriously impair it and the derogation is necessary. | Law 190/2018 Art. 8(1) |
| DP-6 | The derogations apply only with the **Art. 89(1) GDPR safeguards**, and only to the research part of processing that has more than one purpose. | Law 190/2018 Art. 8(3)–(4) |
| DP-7 | Law 190/2018 does **not** contain a provision expressly constituting the Union/Member-State law that GDPR Art. 9(2)(j) needs for research processing of health data. My reading of the full 17-article text found only Arts. 3, 4, 6 and 8 relevant. Without that law, non-consent health-data research needs another Art. 9(2) condition or another identified law. | Law 190/2018 (full text); GDPR Art. 9(2)(j) |
| DP-8 | EDPB view for trials: safety reporting, archiving and inspection processing rests on Art. 6(1)(c) + 9(2)(i). Purely research processing rests on explicit consent (6(1)(a) + 9(2)(a)), public task (6(1)(e)), or legitimate interest (6(1)(f)), combined with 9(2)(i) or (j). CTR informed consent is **not** the same thing as GDPR consent. | EDPB Opinion 3/2019, §§10–17, https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_opinionctrq_a_final_en.pdf |
| DP-9 | DPO designation follows GDPR Arts. 37–39. Public bodies may share one DPO. | Law 190/2018 Art. 10 |

### 2.8 Patient-rights Law 46/2003 and its norms (OMS 1410/2016)

Source: Law 46/2003, consolidated to Law 328/2023 (MO 1020/08.11.2023). ms.ro-hosted consolidated-unofficial print: https://ms.ro/media/documents/LEGE_Nr._46_2003_forma_la_data_de_20.11.2023.pdf. Portal Legislativ: https://legislatie.just.ro/Public/DetaliiDocument/41483

| # | Fact | Provision |
|---|---|---|
| PR-1 | Patient consent is **mandatory** for participation in clinical medical teaching **and in scientific research**. Persons unable to express their will may not be used for research, except with the legal representative's consent **and** where the research is also in the patient's interest. | Law 46/2003 Art. 19 |
| PR-2 | Consent is mandatory for collecting, storing and using **all biological products** taken from the body, for the diagnosis or treatment the patient agreed to. Research use of leftover samples or biobanks needs separate justification. | Law 46/2003 Art. 18 |
| PR-3 | All information on the patient's condition, results, diagnosis, prognosis, treatment and personal data is **confidential, even after death**. | Law 46/2003 Art. 21 |
| PR-4 | Confidential information may be disclosed **only with explicit consent or where the law expressly requires it**. The only consent-free exception is disclosure to other accredited providers involved in the patient's treatment (Art. 23). There is **no research exception**. | Law 46/2003 Arts. 22–23 |
| PR-5 | Photographing or filming without consent is banned, except where needed for diagnosis or treatment or to avoid suspicion of malpractice. This matters for imaging and bronchoscopy figures in papers. | Law 46/2003 Art. 20; OMS 1410/2016 Norms Art. 7 (written form, Annex 1) |
| PR-6 | Research participation of persons unable to express their will requires the legal representatives' consent and must also serve the patient's interest. | OMS 1410/2016 Norms Art. 8(1). ms.ro consolidated print: https://ms.ro/media/documents/ORDIN_Nr._1.410_2016_forma_la_data_de_20.11.2023.pdf |
| PR-7 | Breach of confidentiality or other patient rights by health staff is sanctioned (disciplinary, contravention or criminal, as the case may be). | Law 46/2003 Art. 37 |

I did not check whether Law 46/2003 was amended after November 2023.

### 2.9 Colegiul Medicilor din România: Deontology Code (2025)

Source: CMR Deontology Code, an integral part of Hotărârea AGN CMR 2/2025 of 30.10.2025, published in MO Partea I nr. 1141/10.12.2025, in force 01.01.2026. https://www.cmr.ro/wp-content/uploads/2026/01/codul-de-deontologie-medicala-al-colegiului-medicilor-din-romania-din-30102025-1.pdf

| # | Fact | Provision |
|---|---|---|
| CMR-1 | Binding on all CMR member physicians and on physicians providing services temporarily in Romania. | Art. 1(1) |
| CMR-2 | Physicians must ensure Helsinki, Oviedo and **CTR 536/2014** are respected and that the **local or national ethics body's opinion** exists. | Art. 1(2) |
| CMR-3 | Physicians may involve their patients in studies only with the agreement of the patient or legal guardian, where justified by preventive, diagnostic or therapeutic value, and where participation will not harm health or the doctor-patient relationship. | Art. 50(2) |
| CMR-4 | Research on persons able to consent requires: proportionate risk; an opinion from **CNBMDM or local ethics committees**; information on rights and safeguards; consent that is **express, specific, free and recorded in writing**; and information on the right to withdraw. | Art. 51 |
| CMR-5 | Incapacitated adults: consent of the legal representative, and only if comparable data cannot be obtained from competent subjects. Minors: parental or legal-representative consent, only if the study can only be done on minors, and with no objection from the minor. | Arts. 52–53 |
| CMR-6 | No person may be subjected to experiments, invasive or non-invasive tests or interventions for research except under conditions expressly and restrictively set by law. | Art. 55 |
| CMR-7 | **Publication:** physicians may present cases or papers and publish studies with *strict respect for patient confidentiality and identity* under the law. Drugs must be referred to **only by INN (DCI)**. Content must be evidence-based and sourced. | Art. 46(1)–(2) |
| CMR-8 | Professional secrecy continues after the patient's death. Its limits are set by law. | Arts. 30–31 |
| CMR-9 | Conflict-of-interest disclosure duty. | Art. 62 |

### 2.10 Other instruments to note (not read in full)

- **Oviedo Convention** (ETS 164), ratified by Romania by Law 17/2001. Ch. V covers research. Referenced by CMR Art. 1(2). Not read.
- **EHDS Regulation (EU) 2025/327**: secondary use of health data through health-data access bodies, applying in stages from 2027 onward. It will change the retrospective-data route in future. https://eur-lex.europa.eu/eli/reg/2025/327. I did not verify its application dates article by article.

---

## 3. Open uncertainties

1. **Legal basis of hospital research ethics committees.** OMS 1502/2016 Art. 8(1)(n) assumes a hospital *comisie de etică* for clinical studies, and the CMR Code Art. 51(b) accepts "local ethics committees". I found no act that sets their composition, scope (observational vs. interventional) or procedure. Check Law 95/2006 (hospital titles), any OMS on hospital research committees, and individual hospital ROFs.
2. **Consent waiver for retrospective chart reviews.** Romanian statute has no explicit waiver. Law 46/2003 Arts. 19 and 22 read literally require consent for research and for disclosure of confidential information. Practice depends on anonymisation or "obliterated identity" (UMFST). Whether *pseudonymised* data used in-house by the treating team counts as "disclosure" under Art. 22 is unresolved. **Do not encode a waiver route as available.** Encode it as `external_authority_required`, with the local ethics committee and DPO as decision-makers.
3. **GDPR Art. 9(2)(j) basis in Romania.** Law 190/2018 Art. 8 gives Art. 89(2)-type derogations from data-subject rights. It does not expressly provide the Art. 9(2)(j) "Union or Member State law" basis. I found no ANSPDCP guidance on health-research processing (search: dataprotection.ro). Whether controllers in practice rely on explicit consent, on 9(2)(i) or 9(2)(h), or on Law 190 Art. 8 plus Art. 89 as an implied basis is unverified.
4. **CNBMDM remit over non-interventional studies.** The OMS 80/2023 Art. 5 wording ("pharmacovigilance … studies on human subjects") might reach non-interventional PASS or other NIS. Current CNBMDM practice could not be checked because its site blocked this environment.
5. **Consolidation currency.** Law 46/2003 and OMS 1410/2016 copies are consolidated to November 2023. The OMS 1502/2016 copy is the 2017 original. OUG 29/2022 as amended by Law 249/2022: the Portal Legislativ title now reads "…pentru reglementarea unor măsuri…", which suggests Law 249 added content I have not seen. For example, OMS 3390 refers to "art. 15 alin. (5)" of the OUG "cu modificările și completările ulterioare". Read the consolidated OUG on legislatie.just.ro.
6. **Law 199/2023 article number** for the university ethics commission. Probably Art. 160, but not verified.
7. **Retention of medical files** for trial subjects (CTR Art. 58 defers to national law). I did not locate the Romanian retention period.
8. **Device investigations under OUG 46/2021**: I read only OMS 330/2023, not the OUG.

---

## 4. Implications for the overlay (`ro.*` profiles in `shared/human_subjects_authority_registry.json`)

Shape follows the existing profiles: `profile_id`, `axis`, `authority_scope_ids`, `coverage_status: "bounded_subset"`, `covered_provisions`, `known_exclusions`, `known_gaps`, `no_completeness_claim: true`, `source_ids`, `applies_if`, and `requirements[]`. Each requirement has `obligation_kind`, `waiver_or_exception_route.state`, `authoritative_decision_maker`, `interaction.collision_key/policy`, and `authority_anchor`. The current registry has `us.*`, `tw.*` and `eu.gdpr.research-core-bounded`, and the `overlays` list is empty.

**New `fact_definitions`** (user-declared booleans, unknown when null, following the `scope.tw_hsra` style):
- `scope.ro_ctr_national`: an interventional medicinal-product trial with a Romanian site (CTR + OUG 29/2022).
- `scope.ro_mdr_investigation`: a device clinical investigation with a Romanian site (MDR + OMS 330/2023).
- `scope.ro_patient_rights`: the activity involves patients of Romanian healthcare providers (Law 46/2003).
- `scope.ro_law_190`: Romanian controller or processing within Law 190/2018.
- `professional.ro_cmr_member`: an investigator or author is a CMR-registered physician.
- `data.ro_cnp_processed`: the CNP is processed.
- `activity.retrospective_records_only`: the study only uses existing records.

**Candidate profiles:**

1. `ro.ms.ctr-national-implementation`, axis `review_ethics`, scope `ro.ctr`. applies_if `activity.human_subjects ∧ scope.ro_ctr_national`.
   - `ro.oug29.art2-3.cnbmdm-ethics-review` (require): ethics opinion from CNBMDM via CTIS. Decision-maker CNBMDM. collision `committee.opinion`, `parallel_authorities` (stacks with the CTR itself). Anchor OUG 29/2022 Art. 2(2), 3(2)–(3).
   - `ro.oug29.art4.romanian-language-dossier` (require): subject-facing documents in Romanian.
   - `ro.oug29.art6.excluded-populations` (prohibit): no enrolment of prisoners or residential-care residents. Waiver `not_applicable`.
   - `ro.oms3390.art15.consent-by-investigator-physician` (require). collision `participant.information`.
   - `ro.oms3390.art16.pi-qualification` (condition).
   - `ro.oug29.art10.ctr-art81-publication` (require, sanctioned): links to the publishing workflow (CTIS results within 1 year, CTR Art. 37(4)).
2. `ro.ms.mdr-clinical-investigation`, axis `review_ethics`. A CNBMDM positive opinion is a precondition for every device class (OMS 330/2023 Norms Art. 4, 16).
3. `ro.parliament.law-46-2003.patient-rights-research`, axis `review_ethics` (participant consent plus confidentiality).
   - `ro.l46.art19.research-consent` (require). Waiver `external_authority_required`. Romanian statute gives **no** waiver. Do not offer a "waiver available" route for prospective research.
   - `ro.l46.art21-22.confidentiality` (prohibit unless explicit consent or express legal requirement). Waiver `external_authority_required`, decision-maker local ethics committee + controller/DPO. Add to `known_gaps` that the statute lacks a research exception and that anonymisation practice is not a legal waiver.
   - `ro.l46.art18.biological-samples-consent` (require).
   - `ro.l46.art20.imaging-consent` (require): relevant to figures in manuscripts.
4. `ro.parliament.law-190-2018.research-bounded`, axis `data_protection`. It should **extend** `eu.gdpr.research-core-bounded` rather than duplicate it, as a first entry in `overlays` if the schema supports that. Otherwise make it a separate profile with collision keys shared with the EU profile.
   - `ro.l190.art8.research-rights-derogation` (route). This is the concrete Member-State law for the existing `eu.gdpr.article-89.2.member-state-derogation` requirement, so it resolves `gdpr.member_state_research_law_identified` **only for Arts. 15/16/18/21**. It does not resolve the Art. 9(2)(j) basis (`known_gaps`).
   - `ro.l190.art4.cnp-safeguards` (safeguard). applies_if `data.ro_cnp_processed`.
   - `ro.l190.art3.health-data-profiling` (condition).
5. `ro.cmr.deontology-code-2025`, axis `review_ethics` (professional), authority_level TBD (see the note at the end). applies_if `professional.ro_cmr_member`.
   - Art. 51 (ethics opinion + written express consent).
   - Art. 46 (publication confidentiality, INN-only drug names). Route this to the manuscript and integrity checks in the paper-writing skills.

**Workflow implications:**
- The routing question the overlay must ask first is **interventional (CTR or MDR) vs. observational**. Interventional work goes to CNBMDM + ANMDMR via CTIS, or ANMDMR directly for devices. Observational work goes to the local hospital or university ethics committee, plus the DPO. Non-interventional PASS goes to ANMDMR pharmacovigilance or PRAC.
- For **retrospective respiratory chart reviews** (e.g. COPD exacerbation cohorts, TB outcomes, ILD registries), the overlay should require: a local ethics opinion, a DPO-reviewed GDPR basis (Art. 6 + Art. 9 condition stated explicitly), anonymisation or pseudonymisation that is documented, and a CNP-handling note. It should flag Law 46/2003 Art. 22 as an unresolved legal risk and not hide it.
- **Publication checks** to add to the overlay's manuscript stage: an ethics-approval statement naming the approving committee (CNBMDM or the local committee), the consent statement (or anonymisation statement for retrospective studies), the CTIS/EU CT number for CTR trials, INN-only drug naming (CMR Art. 46), patient-identifiable images only with Art. 20 consent, and a COI disclosure (CMR Art. 62).
- `authenticity_status` for anchors should be `official_controlling_language` only once checked on legislatie.just.ro or the MO. Until then, use `authoritative_unofficial` (an existing registry value), because current sources are consolidated prints. `source_language: "ro"`, `controlling_language: true`.
- `authority_level`: the registry currently uses only `supranational` and `national`. The CMR Code profile needs either a new value (e.g. `professional_body`) or `national` plus a note. That is a schema decision for the overlay.
