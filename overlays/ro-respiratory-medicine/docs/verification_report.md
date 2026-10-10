# S2 verification report

Run date: 2026-10-10

## Method

Read SPEC §§9–10.4, glossary, evidence schema, data README, and `check_overlay.py`. Read the seven named research findings files. For encoded legal provisions, fetched the cited PDF using `curl -sL`, extracted the PDF text with Python 3.12 and `pypdf`, then recorded the article locator and a short Romanian proof quote. Legal copy URLs were agency-hosted or Ministry/court-hosted; none was verified on legislatie.just.ro. Therefore these rows remain explicitly marked as unofficial copies for S4 authenticity review. No value was encoded from memory. Round 2 retried the official legislatie.just.ro Law 190/2018 page and sampled live venue pages, but those responses did not expose article text or the needed author-instruction values in a readable form. Europe PMC abstracts were fetched for ACQ and K-BILD; only values explicitly present in those abstracts were encoded. Other requested sources were not verified in this run. No value was encoded from memory.

## Outcome counts

| Outcome | Count |
|---|---:|
| Promoted to primary-full-text | 16 |
| Promoted to primary-abstract | 2 |
| Advisory | 0 |
| Dropped | 0 |
| Not attempted / unresolved | 35 named §10.4 backlog entries below |

The not-attempted count treats each semicolon-separated backlog value and each venue/legal gap as an entry. The 35 rows are enumerated individually below. The broader research files contain additional edition, definition, and data-source claims; these were also not attempted and are not encoded.

## Value outcomes

| value | area | original tag in findings | outcome | value_id or reason |
|---|---|---|---|---|
| OUG 29/2022 Art. 2(1), competent authority | legal.ro.ctr | consolidated-unofficial | promoted | `ro.ctr-authority` |
| OUG 29/2022 Art. 2(2), CNBMDM remit | legal.ro.ctr | consolidated-unofficial | promoted | `ro.cnbmdm-ethics` |
| OUG 29/2022 Art. 3(2), ethics/scientific review and CTIS | legal.ro.ctr | consolidated-unofficial | promoted | `ro.ctis-evaluation` |
| OUG 29/2022 Art. 4(1)–(2), dossier language | legal.ro.ctr | consolidated-unofficial | promoted | `ro.ct-dossier-language` |
| Law 46/2003 Art. 18, biological products | legal.ro.patient_rights | consolidated-unofficial | promoted | `ro.patient-rights-samples` |
| Law 46/2003 Art. 19, research consent | legal.ro.patient_rights | consolidated-unofficial | promoted | `ro.patient-rights-research-consent` |
| Law 46/2003 Art. 20, images | legal.ro.patient_rights | consolidated-unofficial | promoted | `ro.patient-rights-images` |
| Law 46/2003 Art. 21, confidentiality | legal.ro.patient_rights | consolidated-unofficial | promoted | `ro.patient-confidentiality` |
| Law 46/2003 Art. 22, disclosure | legal.ro.patient_rights | consolidated-unofficial | promoted | `ro.patient-disclosure` |
| OMS 3390/2022 Norms Art. 15(1), person obtaining consent | legal.ro.ctr | consolidated-unofficial | promoted | `ro.clinical-consent-taker` |
| OMS 3390/2022 Norms Art. 16(2), PI qualification | legal.ro.ctr | consolidated-unofficial | promoted | `ro.pi-qualification` |
| OMS 330/2023 Norms Art. 4(1)–(2), ethics and scientific review | legal.ro.mdr | consolidated-unofficial | promoted | `ro.mdr-ethics-review` |
| OMS 330/2023 Norms Art. 16, positive ethics opinion | legal.ro.mdr | consolidated-unofficial | promoted | `ro.mdr-positive-opinion` |
| CMR Code 2025 Art. 46(1), confidentiality and INN | legal.ro.cmr | primary-full-text in research | promoted | `ro.cmr-publication-drug-name` |
| CMR Code 2025 Art. 51(b)–(e), approval and consent | legal.ro.cmr | primary-full-text in research | promoted | `ro.cmr-research-consent` |
| CMR Code 2025 Art. 62(2), conflict of interest | legal.ro.cmr | primary-full-text in research | promoted | `ro.cmr-conflict-interest` |
| GOLD FEV1 grade cut-offs | airways | recalled / snippet / unverified | not attempted | No source fetched in this run |
| CNAS protocol list | data_sources | recalled / snippet / unverified | not attempted | No source fetched in this run |
| AQLQ MID | airways | recalled / snippet / unverified | not attempted | No primary source value verified in this run |
| Sweat-chloride thresholds | airways | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Fuchs criteria | airways | recalled / snippet / unverified | not attempted | No source fetched in this run |
| PPF decline thresholds | ild | recalled / snippet / unverified | not attempted | No source fetched in this run |
| AASM hypopnoea rule | sleep | recalled / snippet / unverified | not attempted | No source fetched in this run |
| ESC PE risk classes | pulmonary_vascular | recalled / snippet / unverified | not attempted | No source fetched in this run |
| IPF 6MWD MCID | ild | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Epworth MCID | sleep | recalled / snippet / unverified | not attempted | No source fetched in this run |
| OSA driving order | sleep | recalled / snippet / unverified | not attempted | No source fetched in this run |
| IPF protocol texts | ild | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Screening eligibility | thoracic_oncology | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Romanian silicosis counts | infection_and_other | recalled / snippet / unverified | not attempted | No source fetched in this run |
| ENSP edition | methodology | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Eurobarometer 2024 RO figure | data_sources | recalled / snippet / unverified | not attempted | No source fetched in this run |
| RSV policy | infection_and_other | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Rehab reimbursement | data_sources | recalled / snippet / unverified | not attempted | No source fetched in this run |
| CURB-65 | infection_and_other | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Berlin bands | sleep | recalled / snippet / unverified | not attempted | No source fetched in this run |
| NIV pH threshold | infection_and_other | recalled / snippet / unverified | not attempted | No source fetched in this run |
| Pneumologia author instructions | venue.pneumologia | unreachable in findings | not attempted | URL listed below; no fresh fetch |
| CHEST abstract limit | venue.chest | third-party / snapshot | not attempted | No fresh source fetch |
| CHEST APC | venue.chest | unavailable | not attempted | No fresh source fetch |
| CHEST GenAI policy | venue.chest | snippet / sister-title inference | not attempted | No fresh source fetch |
| AJRCCM reference style | venue.ajrccm | unverified | not attempted | No fresh source fetch |
| AJRCCM checklists | venue.ajrccm | unverified | not attempted | No fresh source fetch |
| AJRCCM fees | venue.ajrccm | snippet | not attempted | No fresh source fetch |
| Thorax figures | venue.thorax | unverified | not attempted | No fresh source fetch |
| Thorax checklist mandate | venue.thorax | unverified | not attempted | No fresh source fetch |
| Respiratory Medicine 2024 snapshot | venue.respiratory_medicine | snapshot | not attempted | No fresh source fetch |
| WoS status of international journals | venues | unverified | not attempted | Indexing intentionally omitted by SPEC §9 |
| Law 190/2018 Arts. 3, 4, 8 | legal.ro.law_190 | consolidated-unofficial | not attempted | No PDF fetched in this run |
| Law 199/2023 article number | legal.ro.law_199 | inferred | not attempted | No source fetched in this run |
| OUG 29/2022 consolidated status incl. Law 249/2022 | legal.ro.ctr | consolidated-unofficial | not attempted | Fetched OUG print, but did not verify consolidation history on official portal |

## Unreachable sources

- `https://legislatie.just.ro/Public/DetaliiDocument/253151` — findings report that the official portal refused non-browser requests; not retried during this run. Agency copy used for the OUG rows.
- `https://legislatie.just.ro/Public/DetaliiDocument/41483` — not fetched during this run; Ministry-hosted consolidated print used for Law 46 rows.
- `https://legislatie.just.ro/Public/DetaliiDocument/203151` — not fetched during this run; not used for any encoded row.
- `https://www.cmr.ro/wp-content/uploads/2025/12/Codul-de-deontologie-medicala-2025.pdf` — HTTP 404. Working official CMR PDF was fetched at `https://www.cmr.ro/wp-content/uploads/2026/01/codul-de-deontologie-medicala-al-colegiului-medicilor-din-romania-din-30102025-1.pdf` and used.
- `https://pneumologia.eu/Instructiuni-autori-87.htm` — reported HTTP 500 in research; not retried during this run.


## Round 2 additions and remaining requested coverage

| value | area | original tag in findings | outcome | value_id or reason |
|---|---|---|---|---|
| ACQ minimal important difference, approximately 0.5 | airways | primary-abstract (freshly fetched) | promoted | `airways.acq-mcid` |
| K-BILD total MCID, 4.7 improvement / 2.7 deterioration | ild | primary-abstract (freshly fetched) | promoted | `ild.kbild-mcid` |
| Law 190/2018 Arts. 3, 4, 8 | legal_ro | consolidated-unofficial | not attempted | Official portal response was not a readable article page; no legal value encoded |
| Remaining 10 venue records and their requested fields (abstract, headings, limits, checklists, AI placement, APC; ERS Congress counting rule) | venues | mixed | not attempted | Sources not freshly verified to readable author-instruction text in this run |
| GOLD 2026 Group E rule; GINA 2026 T2 cut-offs | airways | primary-full-text in findings | not attempted | Fresh guideline text not retrieved/read in this run |
| ACQ, ACT, CAT, SGRQ, FEV1, QOL-B, CFQ-R, LCQ MCIDs (except ACQ above) | airways | mixed | not attempted | Numeric abstract/full-text evidence not fetched and checked in this run |
| FVC decline 2–6%; K-BILD 3.9 | ild | mixed | not attempted | K-BILD abstract located but the requested 3.9 FVC/MID claims were not verified |
| mPAP >20 mmHg; PVR >2 WU; PAH 6MWD ~33 m | pulmonary_vascular | mixed | not attempted | Source text not fetched/read in this run |
| 6MWD 25 m; ISWT 48 m | methodology | primary-abstract in findings | not attempted | Source text not fetched/read in this run |
| Thoracic oncology QLQ-C30 bands | thoracic_oncology | unverified | not attempted | Source text not fetched/read in this run |
| Guideline names, issuing bodies, years/editions and DOI in SPEC §§6.2–6.3 | methodology | mixed | not attempted | Complete primary-source verification not performed |
| Data sources in SPEC §6.4 | data_sources | mixed | not attempted | Complete primary-source verification not performed |
| Comma-below Unicode code points and NLM Citing Medicine diacritics rule | citations | mixed | not attempted | Standards pages not fetched/read in this run |
| Measurement standards in SPEC §6.2 | methodology | mixed | not attempted | Full set of standards sources not fetched/read in this run |

## Files with no round-2 additions

The files `pulmonary_vascular.json`, `sleep.json`, `thoracic_oncology.json`, `infection_and_other.json`, `methodology.json`, `data_sources.json`, `venues.json`, and `citations.json` remain empty because no eligible primary evidence for their requested rows was verified in this run. This is an explicit unresolved outcome, not a finding that those areas have no relevant values. `legal_ro.json` retains its 16 round-1 rows; Law 190/2018 remains unresolved.
