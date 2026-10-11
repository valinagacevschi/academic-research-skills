# Romanian scientific-language resources (wayfinder ticket 05)

Ticket: `.scratch/ro-respiratory-medicine/issues/05-romanian-scientific-language.md`
Researched: 2026-10-10. Sources are primary (NLM, WHO, Unicode, Romanian Academy, journal author pages, PubMed E-utilities) unless marked otherwise. Empirical PubMed counts come from E-utilities queries run on that date (method under F5). They are snapshots, not universal facts.

## Answer summary

1. **No Romanian MeSH or DeCS exists.** The UMLS lists MeSH plus 15 translations, and Romanian is not one of them. DeCS covers four languages (pt, es, en, fr). NLM retired its MeSH Translation Maintenance System in December 2018. Romanian MeSH keywords therefore have no authoritative ro-MeSH mapping: keywords stay English MeSH, and any Romanian keyword is a free translation.
2. **Classifications.** Romanian hospital coding uses **ICD-10-AM (CIM-10-AM, 3rd ed.)** under MoH Order 1027/2010 (RO.vi.DRG), and ICD-10 (the "999 list") on some administrative forms. A Romanian **ICD-11** translation was reported "completed" in 2022 (Romanian MoH project slides), but Romanian is **not** a released ICD-11 MMS language in WHO's ICD-API (2026-01 release). MedDRA lists Romanian as "under development" (MSSO, Aug 2026). EDQM Standard Terms are available in Romanian. SNOMED CT has no Romanian member translation listed.
3. **Orthography authority.** The Romanian Academy sets mandatory orthography (Law 752/2001). The normative dictionary is DOOM (DOOM2 2005, DOOM3 online at doom.lingv.ro). DOOM2 states explicitly that ș and ț take a **comma below (virguliță), not a cedilla**. DEX is the explanatory dictionary, not the orthographic norm.
4. **Unicode.** The correct code points are U+0218/0219 (Ș ș) and U+021A/021B (Ț ț), added in Unicode 3.0. Unicode's NamesList says that for Romanian, 0219 and 021B "should be used instead" of cedilla U+015F/U+0163. Comma-below and cedilla forms are **not** canonically equivalent, so NFC/NFD normalization never folds one into the other.
5. **PubMed in practice.** MEDLINE stores whatever the publisher supplied (UTF-8, NFC). Romanian names appear with **cedilla, comma-below, or no diacritics at all**, even within one journal. For example, Rom J Morphol Embryol 2022–24 author names use cedilla exclusively, while Rom J Intern Med mixes both. PubMed **search** is diacritics-neutral: `Mureșan`, `Mureşan` and `Muresan` return the same count.
6. **Citation styles.** Romanian medical journals use **Vancouver/ICMJE variants** with house differences: square brackets or round parentheses, UPPERCASE surnames with periods after initials (RJIM), comma placement, DOI/PMID mandatory (RJME) or forbidden (RRML), and an et al. threshold of 6. NLM's *Citing Medicine* says to **ignore (strip) diacritics** in author names and non-English titles. Journal practice ranges from stripping to keeping diacritics, cedilla or comma.
7. **Language of publication.** Leading Romanian respiratory and medical journals now publish in English. *Pneumologia* publishes in English with a Romanian abstract and accepts Romanian submissions. MEDLINE indexed *Pneumologia* only from 1999 to 2016, coded `rum` (ISO 639-2/B) for Romanian-language articles.

## Findings

### F1. MeSH / DeCS: no Romanian translation

- UMLS Metathesaurus active release lists "Medical Subject Headings and its 15 translations: MSH, MSHCZE, MSHDUT, MSHFIN, MSHFRE, MSHGER, MSHITA, MSHJPN, MSHLAV, MSHNOR, MSHPOL, MSHPOR, MSHRUS, MSHSCR, MSHSPA, MSHSWE". There is no Romanian entry. https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/active_release.html
- NLM retired the MeSH Translation Maintenance System (MTMS) on 2018-12-31. Translators must now run their own systems. https://www.nlm.nih.gov/pubs/techbull/nd18/brief/nd18_mesh_translation-mgt_system_cease.html
- DeCS (BIREME/PAHO) is "quadrilingual" (Portuguese, Spanish, English, French). https://wiki.bireme.org/en/index.php/Decs
- Web searches in Romanian and English turned up no Romanian MeSH project. This is absence of evidence, not proof of absence; see U1.
- RJME tells authors to take keywords "preferably from Index Medicus or Excerpta Medica Index", i.e. English controlled vocabularies. https://rjme.ro/guide-for-authors/

### F2. Medical terminology references and classifications

| Resource | Romanian status | Source |
|---|---|---|
| ICD-10-AM (CIM-10-AM, 3rd ed., Australian modification) | Official for DRG hospital coding. Romanian tabular lists of diseases and procedures, Bucharest 2010 | MoH Order 1027/15.07.2010, listed at DSP Neamț: http://www.sant.ro/informatii-utile/statistica-si-informatica/clasificare-ro.vi.drg ; PDF: http://www.sant.ro/informatii-utile/statistica-si-informatica/clasificare-ro.vi.drg/1/1/ListaTabelara_proceduri_ICD_10_AM.pdf/at_download/file ("a treia ediție" wording seen via search-engine snippet of the preface; the PDF text layer was not extractable) |
| ICD-10 "999 list" | Used on sick-leave, referral and prescription forms (per MoH slides) | Geană, Ciutan, Mușat, Rădulescu, Klasifikon 2022, slide 10: https://www.uzis.cz/res/file/akce/20221013-who-fic/05-radulescu.pdf |
| ICD-11 | Romanian translation of the tabular list "completed" (2022), reviewed by 43 MoH specialists, mapped to ICD-10-AM (8,572 direct + 6,089 manual correspondences). **Not** a released ICD-11 MMS language at WHO: 2026-01 MMS languages are ar, zh, cs, en, fr, de, kk, la, pt, ru, sk, es, sv, tr, uz | Same slides, slides 2, 4, 9; WHO ICD-API: https://icd.who.int/docs/icd-api/SupportedClassifications/ |
| MedDRA | Romanian listed under "Languages Under Development" (with Bulgarian, Danish, Maltese, Uzbek) | MSSO "What's New with MedDRA 29.1" (Aug 2026): https://files.meddra.org/training/MSSOEvent/CourseTrainingMaterial/Webinars/001447_Whats_New_with_MedDRA_V29.1.pdf |
| EDQM Standard Terms (dose forms, routes) | Available in Romanian (one of 35 languages) | https://standardterms.edqm.eu |
| EMA QRD product-information templates | Published in all EU languages, including română | https://www.ema.europa.eu/en/human-regulatory-overview/marketing-authorisation/product-information-requirements/product-information-qrd-templates-human |
| SNOMED CT | No Romanian member translation listed | https://www.implementation.snomed.org/member-translations |
| IATE (EU term base) | Includes RO; general EU terminology, partly medical | https://iate.europa.eu/ |

Orthographic and lexical authority:

- Under Law 752/2001 the Romanian Academy "se îngrijește de cultivarea limbii române și stabilește regulile ortografice obligatorii". The norms are in DOOM2 (2005) and, now, DOOM3 (online, >65,000 entries). Punctuation follows ÎOOP (1995). Sources: Academy page https://acad.ro/institutia/limba_romana_reglementari.html and DOOM2 summary (Academy text mirrored by dexonline) https://dexonline.ro/article/Ortografie_-_2005_-_Ce_e_nou_%C3%AEn_DOOM2
- DEX (Dicționarul explicativ, Institutul de Lingvistică „Iorgu Iordan – Al. Rosetti”) is the explanatory dictionary. dexonline aggregates DEX, DOOM2/3, MDN, DETS (etymological dictionary of scientific terms) and others, but its terms forbid scraping or automated extraction without written consent, except for official public datasets (footer of the page above). A pack must not bulk-harvest it.
- Specialist medical dictionaries: V. Rusu, *Dicționar medical* (Editura Medicală; 2nd ed. 2004 cited in academic lexicography, https://solirom.ro/publications/COLEXI_2023.pdf). This is a secondary citation; the editions were not verified.

### F3. ș/ț comma-below vs ş/ţ cedilla

- **Norm:** DOOM2, note to the alphabet table: "ș și ț au sub s și t o virguliță, și nu o sedilă (care se utilizează sub c în alte limbi: ç). În unele programe de calculator, ș, spre deosebire de ț, apare în mod greșit cu sedilă." (link above)
- **Unicode** (NamesList.txt, UCD 18.0): U+015F LATIN SMALL LETTER S WITH CEDILLA is annotated "the character 0219 should be used instead for Romanian", and U+0163 likewise for 021B. U+0218–021B decompose to base + U+0326 COMBINING COMMA BELOW. The cedilla forms decompose to base + U+0327. DerivedAge: 0218..021F = Unicode 3.0. https://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt , https://www.unicode.org/Public/UCD/latest/ucd/DerivedAge.txt
- **Romanian national standard:** SR 13011:1999 is commonly cited (secondary sources only; one source writes "SR 13411"). Not verified; see U3.
- **Real-world mixing (observed):**
  - The DSP Neamț MoH-network page contains both forms: s-comma 56, s-cedilla 8, t-comma 214, t-cedilla 46 (e.g. "Neamţ" next to "Neamț").
  - Revista Română de Medicina Familiei's Vancouver page mixes "şi"/"menţionat" (cedilla) with "Acuratețea" (comma).
  - The NLM Catalog record for *Pneumologia* stores the title decomposed, as t + U+0326, and has "Românǎ" with U+030C caron, a mis-encoded ă. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nlmcatalog&id=100941067&retmode=xml

### F4. PubMed/MEDLINE handling of diacritics

- Since September 2010 MEDLINE uses an expanded character set "with diacritical marks on characters in author names, article titles, vernacular titles, full journal titles, and abstracts". XML is UTF-8, NFC. Through August 2010 only nine diacritics on small Latin letters were supported, cedilla included but **not comma below**, and older data was not converted. https://www.nlm.nih.gov/databases/dtd/medline_characters.html
- PubMed searching "ignores those marks", so retrieval is diacritics-neutral. The MEDLINE (ASCII) display shows no diacritics. https://www.nlm.nih.gov/pubs/techbull/nd07/nd07_diacritics.html
- **Observed with E-utilities** (esearch + efetch, ≤200 records per set; character counts in LastName/ForeName):
  - Rom J Morphol Embryol 2022–24: ş 162, ţ 164, Ş 65, Ţ 11, and **zero** comma-below. 2007–09: cedilla only.
  - Rom J Intern Med 2020–26: ș 8 / ş 22, ț 3 / ţ 10, Ș 6 / Ş 6, Ț 2. Abstracts: ș 286, ț 509.
  - *Pneumologia* 2003–09 and 2012–16: mostly cedilla, with a few comma-below.
  - Romania-affiliation respiratory papers, 2024: mostly comma-below (ș 23 vs ş 5).
  - Search test: `Mureșan[au]` = `Mureşan[au]` = `Muresan[au]` = 1371. Query translation: `Muresan[Author]`. Likewise `Ștefănescu`/`Ştefănescu`/`Stefanescu` = 1210 each.
- Romanian-language records carry `<Language>rum</Language>`, ISO 639-2/B; the T code is `ron` and ISO 639-1 is `ro` (https://loc.gov/standards/iso639-2/php/langcodes_name.php?code_ID=376). They also carry an English bracketed ArticleTitle plus a VernacularTitle. Example: PMID 25665367, "[23-th Congress of Romanian Pneumology Society, 2014-- competition between generations]." / "Congresul SRP 2014--competiţie intre generaţii." The vernacular title uses cedilla and lacks î in "între".
- NLM Catalog: *Pneumologia* (NLM ID 100941067, MedlineTA `Pneumologia`, ISSN 0377-5011/2067-2993) has MEDLINE coverage v48n4 1999 to v65n4 2016. Esearch finds 0 records for 2017–2026.

### F5. Author names in citations and indexing

- *Citing Medicine* (NLM, 2nd ed.), journal author rules: "Ignore diacritics, accents, and special characters in names… Treat letters marked with a diacritic or accent as if they are not marked (Å → A, Ç → C …)". The same rule applies to organization names and to non-English article titles. Non-English article titles are translated into English in square brackets, with the language at the end of the reference. Journal titles stay in the original language, abbreviated. Organization names in Roman-alphabet languages are given as published. https://www.nlm.nih.gov/bsd/uniform_requirements.html (ICMJE samples) and the Citing Medicine 2nd-ed. PDF (2007, "Last updated March 17, 2017"), Box "Other surname rules" and chapter 1, title and language rules. The PDF was read from a third-party mirror, https://www.sdms.org/docs/default-source/JDMS/citing-medicine-2007.pdf ; the canonical copy is NCBI Bookshelf "Citing Medicine" (NBK7256), which was blocked by reCAPTCHA during this research.
- Romanian names follow Western order: given name(s), then surname. Hyphenated double surnames are common (e.g. "Ştefănescu-Dima", "Grosu-Bularda" in RJME records), and so are double given names (e.g. "Simona Nicoleta" → initials SN). Citing Medicine's compound-surname examples keep the compound together (e.g. "Halley des Fontaines V"). No explicit hyphen rule was checked. (Name examples are from the PubMed XML fetched above.)
- Journal practice ranges from stripping to keeping diacritics. The RJIM instructions show both in one document: "BAICUS C., … RIMBAS M." (stripped) and "VOIOSU T., BENGUŞ A., … BĂLĂNESCU P., BĂICUŞ C., et al." (kept, with cedilla). https://sciendo-parsed-data-feed.s3.eu-central-1.amazonaws.com/RJIM/Instruction_for_Authors.pdf

### F6. Citation styles of Romanian medical journals (Vancouver variants)

| Journal | Style evidence | Notable deviations from NLM/ICMJE | Source |
|---|---|---|---|
| Romanian Journal of Morphology and Embryology (Craiova) | Numbered, square brackets, "List names of all the authors"; DOI, PMID and PMCID **mandatory**. Example: `Ahn S, Woo JW, Lee K, Park SY. … J Pathol Transl Med, 2020, 54(1):34–44. https://doi.org/… PMID: … PMCID: …` | Comma after journal; year comma volume; en dash; all authors | https://rjme.ro/guide-for-authors/ |
| Romanian Journal of Internal Medicine (Sciendo) | Numbered in [square brackets], "system used for manuscripts submitted to biomedical journals"; first 6 authors, then "et al." | UPPERCASE surnames, period after initials (`VOIOSU T., BENGUŞ A.`) | RJIM PDF above |
| Romanian Journal of Laboratory Medicine (RRML) | "References style: Vancouver, without DOI numbers"; CSL file provided; numbers in round parentheses; file names "without diacritics" | No DOI; parentheses | https://www.rrml.ro/instructiuni_autori.php |
| Revista Română de Medicina Familiei | Romanian-language Vancouver guide: first 6 authors, then "et al."; surname + initials separated by commas | "et al." kept in Latin even in Romanian text | https://revmedfam.ro/stilul-vancouver-de-redactare-a-bibliografiei |
| Medicine and Pharmacy Reports (Cluj) | "Vancouver citation style … numbered in the order of occurrence … consult the Uniform Requirements of the ICMJE" | None stated | https://medpharmareports.com/index.php/mpr/about/submissions |
| *Pneumologia* (Romanian Society of Pneumology; Sciendo/Paradigm) | English-language OA journal; Romanian abstract retained; Romanian submissions accepted and translated by the editors | Reference rules page (pneumologia.eu/Instructiuni-autori-87.htm) returned HTTP 500; **style not verified** | https://www.srp.ro/2017/pneumologia.aspx ; https://reference-global.com/journal/PNEUM |
| Revista Medico-Chirurgicală (Iași) | Submission checklist refers to journal "stylistic and bibliographic requirements" | Specific style not extracted | https://revmedchir.ro/index.php/revmedchir/about/submissions |

## Open uncertainties

- **U1.** No Romanian MeSH is a negative finding from UMLS/DeCS lists plus searches. A local, unofficial translation (e.g. a university library or the Republic of Moldova) could exist outside UMLS. To confirm, ask the NLM MeSH team or the Biblioteca Națională de Medicină / UMF libraries.
- **U2.** It is unknown whether the completed Romanian ICD-11 translation has been delivered to WHO or published nationally. WHO does not list it as of release 2026-01. The ICD-10-AM edition currently in force is also uncertain: 3rd ed. per the 2010 order, and later MoH orders (e.g. 2459/2022 listed at DSP Neamț) were not checked.
- **U3.** Exact standard number and title of the Romanian character-set standard (SR 13011:1999 per secondary sources) is unverified because ASRO text is paywalled.
- **U4.** *Pneumologia*'s current reference style is unverified (author page unreachable).
- **U5.** The PubMed counts cover small samples (≤200 records per set) and say nothing beyond them. They show mixing exists, not its population rates.
- **U6.** DOOM3 (2021) wording on the comma vs cedilla note was not checked directly. The DOOM2 note is the verified text.
- **U7.** The Rusu *Dicționar medical* editions and other medical dictionaries (e.g. Editura Medicală bilingual dictionaries) are cited from secondary bibliographies only.

## Implications for the ro locale pack and evals

**`ro-en` output-language-pair registry entry** (configuration only, per `shared/output_language_pair.md` overlay boundary):

- Token `ro-en`: L1 Romanian (`ro`), script Latin; L2 English (`en`), script Latin. This is the first Latin/Latin pair, so script class cannot distinguish the abstracts and any check must use language-level cues.
- Do not use `rum`/`ron` as tokens. Registry tokens are opaque, but the pack's language metadata should record ISO 639-1 `ro`, 639-2/T `ron`, and MEDLINE `rum`, because PubMed `<Language>` uses `rum`.
- Romanian keywords: state plainly that no Romanian MeSH exists. Keep English MeSH as the controlled keyword set and treat Romanian keywords as translations, never "ro-MeSH terms". The pack must not claim DeCS or MeSH authority for Romanian.

**Orthography rules for generated Romanian text** (a pack style note, not a core rule):

- Emit only U+0218/0219/021A/021B for Ș ș Ț ț. Never emit U+015E/015F/0162/0163 in Romanian prose. Normalize output to NFC; this composes t + U+0326 to U+021B but does **not** convert cedilla to comma, so an explicit mapping is needed.
- When **quoting** a bibliographic record (author names, vernacular titles), preserve the record's characters as supplied. Do not silently "correct" cedilla to comma inside citations, because that would alter metadata used for matching.

**Citation and author-name handling:**

- Matching and verification must be diacritics- and variant-insensitive. Fold ș/ş→s, ț/ţ→t, ă/â→a and î→i for comparison, as PubMed search does, while displaying the original form.
- Default style: Vancouver/ICMJE per *Citing Medicine*, which strips diacritics in names. Offer journal-variant profiles rather than one "Romanian Vancouver". Observed axes: bracket type, author-count/et al. threshold (all vs 6), surname case, initial punctuation, DOI/PMID mandatory vs forbidden.
- Romanian-language sources cited in English output: give an English translation in [brackets], add the language name "Romanian." at the end, and keep the journal title in the original language. "et al." stays in Latin even in Romanian text (RRMF).

**Candidate citation-locale evals** (modelled on `plugin-evals-citation-locale/` cases 09–11; fictional names):

1. *Cedilla/comma equivalence:* a reference list where the same author appears as "Ştefănescu" and "Ștefănescu" (and "Stefanescu"). The agent must treat these as one author and must not report a mismatch or duplicate.
2. *Preserve as supplied:* the agent must not rewrite a cedilla name in a quoted reference while it writes comma-below in its own Romanian prose.
3. *No fabricated ro-MeSH:* when asked for "Romanian MeSH keywords", the agent says no official translation exists and supplies English MeSH plus labelled translations.
4. *Journal-variant fidelity:* given a target journal profile (e.g. RJME: all authors, DOI+PMID+PMCID, comma-year format), the agent formats accordingly and does not normalize to plain NLM.
5. *Non-English title rule:* a Romanian-language *Pneumologia* article cited in an English manuscript gets an English bracketed title, the original journal abbreviation `Pneumologia`, and a trailing "Romanian.".
6. *Hyphenated surname / double initials:* "Ana-Maria Popescu-Rădulescu" renders as "Popescu-Rădulescu AM" (Vancouver), with the hyphen kept, and is not split into two authors.
