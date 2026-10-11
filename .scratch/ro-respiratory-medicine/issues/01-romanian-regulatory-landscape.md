# Romanian regulatory landscape for respiratory research

Type: research
Status: resolved
Map: ../map.md

## Question

What does Romanian and EU law and practice require of respiratory research before and during publication? Cover: ethics committee approval (institutional/local committees, the national bioethics commission for medicines and medical devices), ANMDMR's role, EU CTR 536/2014 for interventional trials, GDPR plus Romanian Law 190/2018 (Art. 9 health data, research exemptions), patient-rights Law 46/2003, informed-consent and waiver rules for retrospective chart reviews and registry studies, and anything Colegiul Medicilor imposes. Output: facts with primary-source citations (official texts, legislatie.just.ro, EUR-Lex), shaped so they could become a `ro.*` profile in `shared/human_subjects_authority_registry.json` (look at the existing `tw.*`/`eu.*` profiles for the shape).

## Answer

- **Interventional drug trials:** EU CTR 536/2014 applies directly, implemented by OUG 29/2022 (approved by Law 249/2022). Submission is through CTIS only. ANMDMR is the competent authority; CNBMDM is the single national ethics body. Under OMS 3390/2022 a study-team physician takes consent and the PI must be a specialist with more than 3 years in the specialty. Prisoners and care-home residents can't be enrolled.
- **Device studies:** EU MDR plus OMS 330/2023. A positive CNBMDM opinion is always required, then ANMDMR validates or authorises depending on device class.
- **Observational studies (chart reviews, registries):** there is no national approval route; in practice a local hospital or university ethics committee approves them. The Colegiul Medicilor code accepts "CNBMDM or local ethics committees".
- **GDPR and Law 190/2018:** Art. 8 lets research skip the data-subject rights in GDPR Arts. 15, 16, 18 and 21, given Art. 89 safeguards. The law gives no explicit Art. 9(2)(j) legal basis for research use of health data, so that stays an open question. Use of the CNP (national ID number) is restricted.
- **Law 46/2003:** research needs consent (Art. 19), and confidential data can be disclosed only with consent or a legal mandate (Art. 22). There is no research waiver; retrospective studies rely on anonymisation in practice.
- **2025 Deontology Code (CMR, in force 2026):** requires an ethics opinion, written consent, confidentiality, and INN (generic) drug names in publications.
- **Carry into the spec:** the legal texts were read from agency-hosted copies because legislatie.just.ro was unreachable. Re-verify them on the official portal before the registry cites them as controlling text. Draft `ro.*` registry profiles are in the findings file.

Findings: branch `research/romanian-regulatory-landscape` (commit `0e0e36f`), file `research/romanian-regulatory-landscape.md` (worktree `/Users/val/dev/ars-research/romanian-regulatory-landscape`).
