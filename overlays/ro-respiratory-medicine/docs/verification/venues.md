# Venue verification — final round (2026-10-10)

Retried all previously unreadable HTTP 200 pages and all publisher bot-blocks. Re-read saved Medicina and Maedica snapshots fetched today through the r.jina.ai reader proxy. Downloaded and extracted the IJTLD author PDF. Values promoted below have row locators in `data/venues.json`; missing fields are explicitly unresolved or absent from the fetched instructions.

| value | final outcome / value_id or reason | URL tried |
|---|---|---|
| ers_journals: abstract limit | promoted — `venue.ers_journals.abstract_limit` | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: abstract structure | dropped — Fetched ERJ author guide did not specify required abstract headings. | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: main-text limit | promoted — `venue.ers_journals.main_text_limit` | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: reference limit | promoted — `venue.ers_journals.reference_limit` | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: reporting checklists | promoted — `venue.ers_journals.checklists` | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: AI-disclosure placement | dropped — Fetched ERJ author guide did not state a GenAI disclosure placement. | https://publications.ersnet.org/authors/erj/instructions |
| ers_journals: APC/fee | promoted — `venue.ers_journals.apc` | https://publications.ersnet.org/authors/erj/instructions |
| ajrccm: abstract limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: abstract structure | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: main-text limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: reference limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: reporting checklists | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: AI-disclosure placement | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| ajrccm: APC/fee | failed-fetch (bot-blocked after retry); no research-file value encoded | https://academic.oup.com/ajrccm/pages/author-guidelines |
| chest: abstract limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: abstract structure | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: main-text limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: reference limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: reporting checklists | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: AI-disclosure placement | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| chest: APC/fee | failed-fetch (bot-blocked after retry); no research-file value encoded | https://journal.chestnet.org/authinfo_prep |
| thorax: abstract limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: abstract structure | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: main-text limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: reference limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: reporting checklists | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: AI-disclosure placement | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| thorax: APC/fee | failed-fetch (bot-blocked after retry); no research-file value encoded | https://thorax.bmj.com/pages/authors |
| resp_med: abstract limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: abstract structure | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: main-text limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: reference limit | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: reporting checklists | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: AI-disclosure placement | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| resp_med: APC/fee | failed-fetch (bot-blocked after retry); no research-file value encoded | https://www.sciencedirect.com/journal/respiratory-medicine/publish/guide-for-authors |
| ijtld: abstract limit | promoted — `venue.ijtld.abstract_limit` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: abstract structure | promoted — `venue.ijtld.abstract_structure` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: main-text limit | promoted — `venue.ijtld.main_text_limit` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: reference limit | promoted — `venue.ijtld.reference_limit` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: reporting checklists | promoted — `venue.ijtld.checklists` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: AI-disclosure placement | dropped — Fetched 2025 guide did not state GenAI disclosure placement. | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| ijtld: APC/fee | promoted — `venue.ijtld.publication_charges` | https://theunion.org/sites/default/files/2025-06/Instructions-for-Authors%20IJTLD%202025%20Updated.pdf |
| medicina: abstract limit | promoted — `venue.medicina.abstract_limit` | https://www.mdpi.com/journal/medicina/instructions |
| medicina: abstract structure | promoted — `venue.medicina.abstract_structure` | https://www.mdpi.com/journal/medicina/instructions |
| medicina: main-text limit | dropped — No main-text word/page cap stated in fetched instructions; free-format initial submission has no strict formatting requirements. | https://www.mdpi.com/journal/medicina/instructions |
| medicina: reference limit | promoted — `venue.medicina.reference_style` (style is stated; no count limit) | https://www.mdpi.com/journal/medicina/instructions |
| medicina: article structure | promoted — `venue.medicina.article_structure` | https://www.mdpi.com/journal/medicina/instructions |
| medicina: reporting checklists | promoted — `venue.medicina.checklists` | https://www.mdpi.com/journal/medicina/instructions |
| medicina: AI-disclosure placement | promoted — `venue.medicina.ai_disclosure` | https://www.mdpi.com/journal/medicina/instructions |
| medicina: APC/fee | dropped — No Medicina-specific APC amount stated on the instructions page. | https://www.mdpi.com/journal/medicina/instructions |
| pneumologia: abstract limit | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; it exposed journal overview but no abstract format. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: abstract structure | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; no abstract structure exposed. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: main-text limit | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; no manuscript limit exposed. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: reference limit | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; no reference limit exposed. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: reporting checklists | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; no reporting checklist mandate exposed. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: AI-disclosure placement | failed-fetch — For-authors tab was re-fetched (HTTP 200) but exposed no author-instruction value; no GenAI policy exposed. | https://sciendo.com/journal/PNEUM?tab=for-authors |
| pneumologia: APC/fee | promoted — `venue.pneumologia.publication_fee` | https://sciendo.com/journal/PNEUM?tab=for-authors |
| rjme: abstract limit | promoted — `venue.rjme.abstract_limit` | https://rjme.ro/guide-for-authors/ |
| rjme: abstract structure | promoted — `venue.rjme.abstract_structure` | https://rjme.ro/guide-for-authors/ |
| rjme: main-text limit | dropped — Freshly fetched guide contains no main-text numeric cap. | https://rjme.ro/guide-for-authors/ |
| rjme: reference limit | dropped — Freshly fetched guide specifies a reference style but no reference-count limit. | https://rjme.ro/guide-for-authors/ |
| rjme: reference style | promoted — `venue.rjme.reference_style`; square-bracket numbering and identifiers stated in the guide. | https://rjme.ro/guide-for-authors/ |
| rjme: reporting checklists | dropped — Freshly fetched guide does not specify a reporting-checklist mandate. | https://rjme.ro/guide-for-authors/ |
| rjme: AI-disclosure placement | dropped — Freshly fetched guide does not specify GenAI disclosure placement. | https://rjme.ro/guide-for-authors/ |
| rjme: APC/fee | dropped — Freshly fetched guide does not state a fee. | https://rjme.ro/guide-for-authors/ |
| maedica: abstract limit | dropped — Fetched PDF contains no abstract word-count cap. | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: abstract structure | promoted — `venue.maedica.abstract_structure` | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: main-text limit | promoted — `venue.maedica.main_text_limit` | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: reference limit | promoted — `venue.maedica.reference_style` (style is stated; no count limit) | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: reporting checklists | dropped — Fetched PDF contains no reporting-checklist mandate. | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: AI-disclosure placement | dropped — AI-use percentage is given, but no disclosure placement is stated. | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: AI-use percentage | promoted — `venue.maedica.ai_policy`; maximum accepted AI use is 30%. | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| maedica: APC/fee | dropped — Fetched PDF contains no APC/fee statement. | https://www.maedica.ro/wp-content/uploads/misc/Instructions_for_authors.pdf |
| ers_congress: abstract limit | promoted — `venue.ers_congress.abstract_limit` | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: abstract structure | promoted — `venue.ers_congress.counting_rule` (the existing row records character accounting; 1810 limit/title/cell/figure rule) | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: main-text limit | dropped — Congress abstract FAQ gives no manuscript main-text limit. | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: reference limit | dropped — Congress abstract FAQ gives no reference-count limit. | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: reporting checklists | dropped — Congress abstract FAQ gives no reporting-checklist mandate. | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: AI-disclosure placement | dropped — Congress abstract FAQ gives no AI-disclosure placement. | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| ers_congress: APC/fee | dropped — Congress FAQ gives publication context but no APC/abstract fee. | https://www.ersnet.org/frequently-asked-questions-about-abstracts/ |
| srp_congress: abstract limit | promoted — `venue.srp_congress.abstract_limit` | https://www.congres-srp.ro/rezumate/ |
| srp_congress: abstract structure | promoted — `venue.srp_congress.abstract_content` | https://www.congres-srp.ro/rezumate/ |
| srp_congress: main-text limit | dropped — Abstract page gives no main-text limit (congress abstract only). | https://www.congres-srp.ro/rezumate/ |
| srp_congress: reference limit | dropped — Abstract page gives no reference-count limit. | https://www.congres-srp.ro/rezumate/ |
| srp_congress: reporting checklists | dropped — Abstract page gives no reporting-checklist mandate. | https://www.congres-srp.ro/rezumate/ |
| srp_congress: AI-disclosure placement | dropped — Abstract page gives no AI-disclosure placement. | https://www.congres-srp.ro/rezumate/ |
| srp_congress: APC/fee | promoted — `venue.srp_congress.registration_requirement` (registration fee payment is required; amount not stated) | https://www.congres-srp.ro/rezumate/ |

