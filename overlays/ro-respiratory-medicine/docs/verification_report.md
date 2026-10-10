# S2 verification report — consolidated (2026-10-10)

## Run dates

All evidence changes in this worktree are dated 2026-10-10. Earlier S2 rounds and this final retry round were run on that date.

## Method

Read the overlay specification and evidence schema. Re-fetched official pages with `curl`/Python `urllib` and a browser user agent; used the supplied Medicina and Maedica snapshots fetched through the r.jina.ai reader proxy today; downloaded and extracted the IJTLD and ECDC TB PDFs; and fetched abstracts/records from PubMed E-utilities and Europe PMC. Each promoted value has its source URL, locator, date, quote, and tag in the data row. No values were encoded from recall. For sources that still did not provide readable primary evidence, no row was added. Bot challenges and missing author-guide content are listed below.

## Outcome totals

Counts are per value line in the five verification fragments, plus the remaining §10.4 carry-forward entries identified in the final backlog table. The latter add ten failed-fetch outcomes and one out-of-scope dropped item.

| Outcome | Count |
|---|---:|
| Promoted | 112 |
| Advisory | 1 |
| Dropped | 24 |
| Failed-fetch / unresolved | 59 |
| **Total outcomes** | **196** |

## Per-area evidence and unresolved counts

Encoded row counts are grouped by evidence tag and use. Failed counts include source/claim backlog items with no primary evidence; all details appear in the linked fragments and §10.4 table.

| Data area | Encoded rows by tag/use | Failed / unresolved |
|---|---|---:|
| `legal_ro` | primary-full-text/fact_check: 19 | 3 |
| `airways` | primary-abstract/fact_check: 8; primary-abstract/reference: 8; primary-full-text/fact_check: 4; primary-full-text/reference: 1 | 6 |
| `ild` | primary-abstract/fact_check: 3; primary-abstract/reference: 6; primary-full-text/fact_check: 1 | 1 |
| `pulmonary_vascular` | primary-abstract/fact_check: 2; primary-abstract/reference: 1; primary-full-text/reference: 1 | 0 |
| `sleep` | primary-abstract/fact_check: 1; primary-full-text/fact_check: 2; primary-full-text/reference: 2 | 0 |
| `thoracic_oncology` | primary-abstract/fact_check: 1; primary-abstract/reference: 1; primary-full-text/reference: 5 | 0 |
| `infection_and_other` | primary-abstract/fact_check: 3; primary-abstract/reference: 4; primary-full-text/reference: 1 | 9 |
| `methodology` | primary-abstract/fact_check: 2; primary-abstract/reference: 11 | 1 |
| `data_sources` | primary-abstract/reference: 6; primary-full-text/reference: 1 | 4 |
| `venues` | primary-full-text/fact_check: 13; primary-full-text/reference: 17 | 34 |
| `citations` | primary-full-text/reference: 1; secondary/advisory: 1 | 1 |

## §10.4 backlog — final outcome

| Backlog value | Final outcome | Detail |
|---|---|---|
| GOLD airflow-obstruction FEV1 grade cut-offs | failed-fetch | Non-text figure in the fetched GOLD report; values not encoded. |
| CNAS protocol list | failed-fetch | No complete official protocol list verified. |
| AQLQ MID 0.5 | failed-fetch | Retrieved abstracts did not state the value. |
| Sweat-chloride thresholds | failed-fetch | Fetched abstract did not state numeric cut-offs. |
| Fuchs criteria | failed-fetch | No primary source value verified. |
| PPF decline thresholds | promoted | `ild.ppf-criteria` in the parenchymal fragment. |
| AASM hypopnoea rule | promoted | `sleep.aasm-hypopnoea-rule` in the parenchymal fragment. |
| ESC PE risk classes | promoted | `pulmonary_vascular.esc-pe-risk-classes` in the parenchymal fragment. |
| IPF 6MWD MCID | promoted | `ild.ipf-6mwd-mcid` in the parenchymal fragment. |
| Epworth MCID | promoted | `sleep.ess-mid` in the parenchymal fragment. |
| OSA driving order/bands | promoted | `sleep.eu-driving-ahi-bands` in the parenchymal fragment. |
| IPF protocol texts | failed-fetch | Protocol text editions remain unverified. |
| Screening eligibility | promoted | `thoracic_oncology.ro-screening-eligibility` in the parenchymal fragment. |
| Romanian silicosis counts | failed-fetch | No readable primary registry/report table verified. |
| ENSP edition | failed-fetch | No primary edition citation verified. |
| Eurobarometer 2024 Romania figure | failed-fetch | No source table verified. |
| RSV policy | failed-fetch | ERVISS source verified, but no Romanian policy value was verified. |
| Rehabilitation reimbursement | failed-fetch | No current official reimbursement schedule verified. |
| CURB-65 items | promoted | `infection_and_other.curb65_2003`; abstract states each item and threshold. |
| Berlin ARDS severity bands | promoted | `infection_and_other.berlin_ards_severity_2012`; abstract states all three bands. |
| NIV COPD pH threshold | failed-fetch | Retrieved ERS/ATS abstract did not state the cutoff. |
| Pneumologia author-instruction fields | failed-fetch | Fee verified; six author-format fields were not exposed by the HTTP 200 Sciendo for-authors page. |
| CHEST abstract limit, APC, GenAI placement | failed-fetch | Publisher author-information page remains behind bot verification. |
| AJRCCM reference style, reporting checklists, fees | failed-fetch | OUP guide and alternate instructions remain behind bot verification. |
| Thorax figure limits and checklist mandate | recovered (archive) | Live BMJ page is behind bot verification; values encoded from the Wayback Machine snapshot archived 2026-05-19 (`venue.thorax.*`, verified_at = snapshot date). |
| Respiratory Medicine 2024 author-guide snapshot | failed-fetch | Direct and reader-proxy requests returned challenge content. |
| WoS indexing status of international journals | dropped | Out of scope under the S2 venue brief; indexing was intentionally omitted. |
| Law 190/2018 Arts. 3, 4, 8 | promoted | Court-hosted PDF used; official portal availability itself failed. See legal fragment. |
| OUG 29/2022 article anchors | promoted | Existing rows retained from ANMDMR PDF; official portal unavailable. |
| OUG consolidation history including Law 249/2022 | failed-fetch | Consolidation history not verified on the official portal. |
| Law 46/2003 Arts. 18–22 | promoted | Existing rows retained from the Ministry consolidated PDF. |
| OMS 3390/2022 | promoted | Existing primary full-text rows retained. |
| OMS 330/2023 | promoted | Existing primary full-text rows retained. |
| Law 199/2023 article number | failed-fetch | No primary source verified. |
| CMR Deontology Code 2025 | promoted | Existing official full-text rows retained. |

Other source-specific failed-fetch values from this run are enumerated in the airways, infection/methodology, legal/citations, parenchymal, and venue fragments.

## Still unverified — re-verification backlog

- Airways: Rome ECOPD severity thresholds; GOLD FEV1 grades; AQLQ MID; fourth ECFS paper; sweat-chloride thresholds; Fuchs criteria.
- Infection and public-health values: WHO 2025 DR-TB regimen; NIV COPD pH cutoff; CR-Klebsiella trend; community antibiotic use; GATS tobacco prevalence; older-adult influenza vaccination; ILO radiograph classification; Romanian silicosis counts; RSV policy.
- Methodology/data sources: ENSP edition; IPF protocol text editions; CNAS protocol list; Eurobarometer figure; rehabilitation reimbursement.
- Legal/citation sources: official legislatie.just.ro retrieval; OUG consolidation history; Law 199/2023 article number; NLM author-diacritics rule; INSP TB downloads.
- Venue fields: the six Pneumologia author-guide fields; all seven requested CHEST, AJRCCM, Thorax, and Respiratory Medicine fields are detailed by field in the venue fragment.
- Source fields absent from the fetched instructions are recorded as dropped in the venue fragment; those 23 omitted values are not asserted as requirements. WoS indexing remains out of scope.

## Bot-blocked sources

- AJRCCM: https://academic.oup.com/ajrccm/pages/author-guidelines and alternate https://academic.oup.com/ajrccm/pages/general-instructions — reader proxy returned the challenge page; direct alternate returned HTTP 403.
- CHEST: https://journal.chestnet.org/authinfo_prep and alternate https://journal.chestnet.org/infoforauthors — reader proxy returned challenge pages. The ScienceDirect guide redirected to the blocked journal author page.
- Thorax: https://thorax.bmj.com/pages/authors — reader proxy returned the challenge page; direct request returned HTTP 403. Recovered 2026-10-10 from https://web.archive.org/web/20260519161404/https://thorax.bmj.com/pages/authors (section text decoded from the page data; every quoted value matched).
- Archive check 2026-10-10 for the other three: AJRCCM instructions last archived 2019-10-18, CHEST authinfo_prep 2021-08-29, Respiratory Medicine guide for authors 2024-01-10. All are outside the 6-month review window and were not encoded.
- Respiratory Medicine: https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors and Elsevier alternate — reader-proxy requests returned challenge content.

ERS author instructions were readable through the reader proxy on retry and the supported ERJ values were promoted; it is not classified as still bot-blocked. Pneumologia returned HTTP 200 but did not expose most author-instruction values.

## Per-value fragments

- [Airways](verification/airways.md)
- [Infection and methodology](verification/infection_methods.md)
- [Legal sources and citations](verification/legal_sources_citations.md)
- [Parenchymal, vascular, sleep, and oncology](verification/parenchymal.md)
- [Venues](verification/venues.md)
