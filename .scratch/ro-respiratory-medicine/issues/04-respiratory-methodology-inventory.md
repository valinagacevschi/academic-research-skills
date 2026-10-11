# Respiratory-medicine methodology inventory

Type: research
Status: resolved
Map: ../map.md

## Question

Which methodological resources does a respiratory-medicine profile need, and which does ARS already cover? Inventory the reporting guidelines already referenced in the repo (STROBE, CONSORT, PRISMA, STARD, TRIPOD, CARE…) and where they're used. Then list what's missing for respiratory work: RECORD (routinely collected data), STROBE extensions, ATS/ERS technical standards (spirometry 2019, DLCO, FeNO, interpretation 2022), GOLD/GINA/ERS-ATS definitions, MCIDs (FEV1, SGRQ, CAT, 6MWD), TB-specific standards (WHO definitions, IJTLD guidance). Also respiratory data sources relevant to Romania: INSP/CNSCBT, the National TB Programme, ECDC, Eurostat, WHO Europe, GBD. Cite primary sources.

## Answer

- **ARS already covers clinical reporting well:** `deep-research/references/equator_reporting_guidelines.md` covers PRISMA/CONSORT/STROBE/STARD/TRIPOD+AI/CARE/SPIRIT and design routing at lines 400–455. Systematic-review tooling (RoB 2, ROBINS-I, GRADE, PROSPERO) is covered too.
- **There is no respiratory content at all.** Missing: RECORD/RECORD-PE, STROME-ID, STROBE-MR; ATS/ERS standards (spirometry 2019, DLCO 2017, interpretation 2022, lung volumes 2023, FeNO, field walking tests, GLI and race-neutral equations); GOLD/GINA 2026; WHO TB definitions; IJTLD clinical standards; MCIDs (SGRQ 4, CAT 2, ACT 3, FEV1 about 100 mL confirmed; 6MWD and ACQ unverified).
- **Data sources:** PNPSCT/Marius Nasta, ECDC/WHO Europe TB reports, ECDC Atlas, ERVISS, Eurostat (hospital discharges stop at 2021), WHO Europe HFA, GBD. INSP/CNSCBT couldn't be reached.
- **Profile shape:** keep the existing routing; add a respiratory reference file with each source's edition pinned, add-on prompts (RECORD, STROME-ID, TB diagnostics), a reviewer checklist, and a RO/EU data-source list.
- **Not covered yet:** sleep, ILD and lung cancer.

Findings: branch `research/respiratory-methodology-inventory` (commit `8d13a87`), file `research/respiratory-methodology-inventory.md` (worktree `/Users/val/dev/ars-research/respiratory-methodology-inventory`).
