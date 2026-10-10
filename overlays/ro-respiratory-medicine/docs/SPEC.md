# Spec: Romanian respiratory-medicine overlay for ARS (v1)

Status: hand-off ready, 2026-10-10. Implementer: delegated (Codex), one slice at a time (§12).
Upstream baseline: `Imbad0202/academic-research-skills` `main` @ `e614b32` (v3.23.0).
Vocabulary: [GLOSSARY.md](GLOSSARY.md). Bold terms below are defined there.

This spec is self-contained. The decisions behind it were made on a wayfinder map (local, untracked: `.scratch/ro-respiratory-medicine/map.md`). Each section names the ticket it came from, for provenance only. Facts come from these research branches in this repo:

| Branch | Commit | Used for |
|---|---|---|
| `research/upstream-extension-points` | `4840f6a` | what the overlay can add without core edits |
| `research/romanian-regulatory-landscape` | `0e0e36f` | `ro.*` profile drafts (§4 of its findings) |
| `research/venue-landscape` | `a148621` | venue notes |
| `research/respiratory-methodology-inventory` | `8d13a87` | design add-ons, data sources |
| `research/subdomain-airways` | `0f55175` | airways subdomain reference |
| `research/subdomain-ild-vascular-sleep-oncology` | `ed278ab` | ILD, vascular, sleep, oncology references |
| `research/subdomain-infection-other` | `40169a8` | infection and other references |
| `research/romanian-scientific-language` | `e617161` | citation rules (diacritics, Vancouver variants) |
| `research/ro-hs-alt-registry` | `8bcc048` | proof that the alternate human-subjects registry works |

---

## 1. Destination and scope

ARS adapted for respiratory-medicine research and paper publishing in Romania. Primary users are Romanian pulmonologists and residents writing journal papers; PhD candidates are secondary. It covers all of pulmonology. It is delivered as an **overlay**: no core file changes, so the fork keeps merging upstream cleanly.

**In scope:**
- a `respiratory_medicine` field profile;
- registry deltas (human-subjects, review criteria);
- design add-ons and **subdomain references**;
- the Romanian ethics gate;
- patient-data handling;
- venue support;
- fact verification;
- tests and evals;
- activation.

**Out of scope:**
- Any Romanian-language output: no `ro-en` pair, no Romanian abstracts (the author writes the SRP congress Romanian half), no `ro` locale pack, no Romanian trigger phrases. Users may still converse in Romanian.
- Edits to any core file. Core fixes become **upstream asks** (§13).
- Doctoral theses and CNATDCU/UMF career criteria.
- Pilot clinician validation and institutional ethics-committee overlays.

Hard boundary (`shared/output_language_pair.md` § Overlay boundary): the overlay never overlays `SKILL.md`, agents, IRON RULEs, integrity protocols, schemas, modes or oversight rules.

## 2. Vocabulary

Copy the glossary to `docs/GLOSSARY.md` (done). Use its terms exactly, in code identifiers and docs. In particular, never write "locale pack" or "pack".

## 3. Overlay layout and activation

*From: Overlay mechanism decision.*

```
overlays/ro-respiratory-medicine/
  MANIFEST.json            # upstream_commit, registry_versions{hs, rc}, profile digest, overlay_version
  ACTIVATE.md              # activation preamble (§3.2)
  install.py               # writes the preamble into a project's AGENTS.md/CLAUDE.md; opt-in CNP hook (§8)
  check_overlay.py         # the overlay lint + drift check (§10.3)
  profile/respiratory_medicine.json
  registries/
    human_subjects.delta.json      # source of truth (§5)
    review_criteria.delta.json
    build_registries.py            # generator
    generated/                      # build artifacts, committed, pinned
      human_subjects_authority_registry.json
      review_criteria_registry.json
  references/
    subdomains/{airways,ild,pulmonary_vascular,sleep,thoracic_oncology,infection_and_other}.md
    design_addons.md
    data_sources_ro_eu.md
    reviewer_prompts.md
    venue_notes.md
    edition_watch.md
    citations_ro.md
  venue_extras/
    venue_extras.schema.json
    check_venue_extras.py
  hooks/cnp_guard.py
  tests/                    # pytest (§11.1)
  plugin-evals/             # model-behaviour evals (§11.2)
  docs/{SPEC.md, GLOSSARY.md, UPSTREAM_ASKS.md}
.github/workflows/ro-overlay.yml   # the only file outside the overlay directory
```

### 3.1 Tracking upstream
- `MANIFEST.json` records `upstream_commit`, the upstream `registry_version` each generated registry was built from, and the profile `content_sha256`.
- `check_overlay.py` fails when upstream's registry version differs from the manifest. The fix is to re-run `build_registries.py`.
- The check runs in fork CI (`ro-overlay.yml`) and locally after every upstream merge. A red check blocks the merge.
- Upstream's locale-pack ownership policy does not apply, since we don't seek "supported" listing.

### 3.2 Activation preamble (`ACTIVATE.md`)
A plain instruction block that the user adds to their project's agent instructions. `install.py` does this and is idempotent, with a marked begin/end block. It must state:
1. Output is English only.
2. Human-subjects resolution, review-pathway traces and packet manifests use `registries/generated/human_subjects_authority_registry.json`. Review-target resolution uses `registries/generated/review_criteria_registry.json`. Pass these as `--registry` and never use the core paths.
3. At intake, before drafting: build the Romanian context record (§7.2), show the venue notes for a named target (§9), and run patient-data tier handling (§8).
4. Field profile: `profile/respiratory_medicine.json` is dormant (§4). Its behaviour is carried here: design add-ons (§6), subdomain references, reviewer prompts.
5. Fact rule: only values tagged primary are facts; `secondary` values are advisory "verify" notes (§10).
6. Citations: follow `references/citations_ro.md`.

Rejected alternatives: a wrapper skill (adds a `SKILL.md` at the boundary and competes for triggers), and docs only.

## 4. Field profile

*From: Overlay mechanism decision; First-class study designs.*

- `profile/respiratory_medicine.json`, sealed with upstream `seal_profile` (canonical bytes + `content_sha256`). It must pass `scripts/research_workflow_profile.py` validation, and `select --profile <path> --selected-by user_explicit` must emit a receipt.
- **Profile fields:**
  - `research_family: clinical_human_subjects`, `provenance.source: user_authored`;
  - `declared_family_label: "Respiratory medicine (RO)"`;
  - `display_name` in `en` and `zh_TW` only (the schema is closed). The Romanian name appears in docs only.
- **`stage_map`:** all nine stages `applicable`.
- **`authority_points`** (`task_family` → authority → requirement):
  - `methodology`: EQUATOR routing (core) + overlay design add-ons;
  - `retrieval`: the RO/EU data-source list;
  - `drafting`: the subdomain references, edition-stamped;
  - `review`: the respiratory reviewer prompts;
  - `integrity_check`: the evidence-tag rule (§10).
- **`alternative_categories`:** `{state: declared, categories: [alternative_design, alternative_measurement]}`.
- **Dormant:** no ARS stage reads profiles yet (upstream #742). When one does, remove the duplicated behaviour from `ACTIVATE.md`.

## 5. Registry deltas and generators

*From: Overlay mechanism decision; Probe a RO profile in an alternate human-subjects registry; Romanian ethics-gate behaviour; First-class study designs.*

### 5.1 Generator (`build_registries.py`)
- Reads the **current** core registry and the delta, appends the delta's facts, sources, profiles and criteria, then writes the generated copy.
- Generated `registry_id` values: `human-subjects-authority-ro-respiratory-overlay` and `review-criteria-ro-respiratory-overlay`.
- Generated `registry_version` = `<upstream registry_version>-ro.<n>`.
- Recomputes every delta `profile_digest` via upstream `resolve_human_subjects_authority.digest` (sha256 of the canonical JSON without the digest field). Never edits core rows.
- Runs `--check-registry` (human-subjects) and `validate_registry` (review criteria) on the output. Any failure is a build failure.

Constraints found by the probe (`research/ro-hs-alt-registry`):
- every `requirements[].authority_anchor.source_id` must be in its profile's `source_ids`;
- the anchor's `source_language` must equal the source row's, and anchor provisions must be within `allowed_provisions`;
- a context pins `profile_digest` in `selected_profiles` and `display_precedence`, so profile edits mean re-pinning user contexts. Document this in `ACTIVATE.md`;
- a RO context cannot be resolved against the core registry (unknown facts), and every registry release changes the digest, so older resolved artifacts fail replay. That is expected; document it.

Downstream binders (#669 pathway trace, #667 packet manifest) bind by `registry_pointer` (id, version, digest), not by path, and work with the generated file.

### 5.2 Human-subjects delta
**Facts** (boolean, author-declared, unknown when null):
- `scope.ro_ctr_national`
- `scope.ro_mdr_investigation`
- `scope.ro_patient_rights`
- `scope.ro_law_190`
- `professional.ro_cmr_member`
- `data.ro_cnp_processed`
- `activity.retrospective_records_only`

**Profiles** (all `coverage_status: bounded_subset`, `no_completeness_claim: true`). Requirement drafts are in §4 of the `research/romanian-regulatory-landscape` findings.

| profile_id | axis | Notes |
|---|---|---|
| `ro.ms.ctr-national-implementation` | review_ethics | CNBMDM opinion via CTIS; Romanian-language subject documents; excluded populations (prohibit); consent by investigator physician; PI qualification; CTR Art. 37(4) results publication |
| `ro.ms.mdr-clinical-investigation` | review_ethics | CNBMDM positive opinion for every device class (OMS 330/2023) |
| `ro.parliament.law-46-2003.patient-rights-research` | review_ethics | Arts. 19 (consent) and 21–22 (confidentiality) as `external_authority_required`, decided by local ethics committee + controller/DPO. **No waiver route offered.** `known_gaps`: the statute has no research exception, and anonymisation practice is not a legal waiver. Arts. 18 (samples) and 20 (images) required |
| `ro.parliament.law-190-2018.research-bounded` | data_protection | Selected **alongside** `eu.gdpr.research-core-bounded` (several profiles per axis are allowed). Art. 8 derogation for GDPR Arts. 15/16/18/21 only; Art. 9(2)(j) basis listed in `known_gaps`; Art. 4 CNP safeguards when `data.ro_cnp_processed` |
| `ro.cmr.deontology-code-2025` | review_ethics | `authority_level: national` + `known_gaps` note that it is a professional-body code. Art. 51 (ethics opinion + written consent), Art. 46 (INN-only drug names), Art. 62 (COI) |

- Non-interventional PASS goes in `known_exclusions`.
- Sources: `source_language: ro`, `controlling_language: true`, `authenticity_status: authoritative_unofficial` until checked on legislatie.just.ro / Monitorul Oficial, then `official_controlling_language` (§10).
- No institutional overlays are shipped. The preamble tells the author to declare `overlay_selection_state.institutional = none_declared_by_author`.

### 5.3 Review-criteria delta
Rows within the existing 4 authority classes and 3 dimensions (both enums are closed):
- one `field_society_standard` row: ERS/ATS technical standards for respiratory measurement;
- `reporting_design_overlay` rows: RECORD (routine-records studies), STROME-ID (infection/TB);
- rows for the Romanian manuscript-statement checks (§7.3), `dimension: submission_readiness`.
- **No `official_venue_type` rows** in v1: there are no verified reviewer criteria for these venues.
- Each row needs a source receipt in the style of `shared/review_criteria_sources/`. Keep the four core broad rows verbatim. Any row whose source isn't `current` is advisory (core resolver behaviour).

## 6. Design add-ons and subdomain references

*From: First-class study designs; the three respiratory-subdomain standards tickets; Respiratory-medicine methodology inventory.*

### 6.1 Rule
Core ARS chooses the reporting guideline (`deep-research/references/equator_reporting_guidelines.md` §10, Q0–Q6) and the overlay **never re-routes**. The overlay is design × subdomain:
- a **first-class design** gets design add-ons;
- a **fallback design** gets only the design-independent subdomain content.

### 6.2 First-class designs and their add-ons (`references/design_addons.md`)
| Design (core route) | Add-ons |
|---|---|
| Cohort / case-control / cross-sectional (STROBE) | RECORD whenever data come from routine records (always ask); STROME-ID for infection/TB; Romanian data-source note: hospital records, PNPSCT/Marius Nasta TB registry, CNAS reimbursement protocols as a selection-bias source (not validated endpoints); prompt to put the edition year on any guideline-defined cohort label (e.g. "GOLD E" changed in 2026) |
| Diagnostic accuracy (STARD) | Measurement standards: ATS/ERS spirometry 2019 with race-neutral GLI equations, DLCO 2017, lung volumes 2023, FeNO; AASM v3 for sleep tests; Lung-RADS v2022; TB-diagnostics prompt; ERS/ESGE/ESTS endosonography 2026 |
| Case report / case series (CARE) | Edition-stamped definitions; check it's a true series with no comparison group, not an unadmitted cohort |
| Systematic review / meta-analysis (PRISMA) | MCID anchors for GRADE imprecision judgements; check for guideline edition drift across included studies |

**Fallback designs:** RCTs and protocols (CONSORT/SPIRIT), prediction models (TRIPOD+AI), qualitative, economic, QI, MR, NRSI.

### 6.3 Subdomain references (`references/subdomains/*.md`)
- **Six files:** airways; ILD; pulmonary vascular; sleep; thoracic oncology; infection, occupational, rehab, critical care and interventional.
- **Every row:** definition/threshold/outcome set/MCID + source + edition + evidence tag + `verified_at` (§10).
- **Applies to every design.** For example, a COPD-exacerbation RCT gets the ERS 2022 core outcome set and MCIDs.

Starting content is in the research branches. Notable items:
- GOLD 2026 Group E and Rome grading;
- GINA 2026 T2 cut-offs;
- ERS 2025 bronchiectasis;
- IPF/PPF 2022;
- ESC/ERS 2022 + WSPH 2024;
- AASM v3;
- TNM 9th edition;
- WHO 2025 TB Module 4;
- ERS 2026 pneumonia core outcome set;
- 6MWD 25 m / ISWT 48 m.

Romanian context goes in the relevant rows: CNAS CPAP vs EU driving OSA bands, antifibrotics reimbursed for IPF only, the national lung-cancer screening project 2025–29, TB 2024 figures, the AMR data-representativeness caveat.

### 6.4 Supporting references
- `data_sources_ro_eu.md`: PNPSCT/Marius Nasta, ECDC/WHO Europe TB, ECDC Atlas, ERVISS, Eurostat (hospital discharges stop at 2021), WHO Europe HFA, GBD, INSP/CNSCBT (marked unreachable until verified).
- `citations_ro.md`:
  - generated text uses comma-below ș/ț (U+0218–021B); quoted reference data keeps the publisher's characters (cedilla included);
  - Vancouver variants are taken from the venue notes;
  - no Romanian MeSH exists, so keywords are English MeSH.
- `reviewer_prompts.md`: the respiratory reviewer prompts. These are the ~9 prompts proposed in the infection-and-other research, plus checks on classification version, severity scheme and MCID source. The activation preamble points the reviewer at them.

## 7. Ethics gate

*From: Romanian ethics-gate behaviour.*

### 7.1 Posture
Never refuse; ask and record.
- Core's ethics review agent never vetoes. Human-subjects results come only from an author-declared, replay-validated context.
- Gaps surface as `submission_readiness=gaps_located` and external-actor dependencies.
- Missing manuscript statements are **Conditional**, never Critical. Drafting continues.

### 7.2 Intake touchpoint (via the preamble)
Before drafting, the author builds the Romanian context record:
1. **Routing question first:** CTR medicinal-product trial / MDR device investigation / observational.
2. The §5.2 facts.
3. `scope.eu_gdpr` and the GDPR facts.
4. Profile selection.

Then resolve against the generated registry. Never infer anything from locale, affiliation or manuscript text.

### 7.3 Review touchpoint (Phase 5)
The ethics agent reads the resolved context. The reviewer prompts and §5.3 rows check that the manuscript has:
- an ethics statement naming the committee (CNBMDM or local), with approval number and date;
- a consent statement, or an anonymisation statement plus the committee's decision. "Consent waived by committee X" is allowed only when the author declares the committee said so;
- the EU CT number (CTIS) for CTR trials, plus any registry the venue requires;
- INN-only drug names;
- consent for any identifiable image (Law 46 Art. 20);
- a COI disclosure.

## 8. Patient data

*From: Patient data in prompts.*

**Tiers:**
- **Aggregate data:** no action.
- **Line-level data:** one warning per session, then continue only after the user confirms their controller/DPO allows sending it to the model provider.
- **Direct identifiers:** the agent stops once (not a refusal). It never echoes or writes them to workspace files, asks for a redacted re-paste, and notes the transcript already holds them.

**Code-to-data:** line-level analysis runs locally in scripts ARS writes (R/Python/SPSS), and only aggregate results return. A local or EU-hosted model is the user's own choice.

**Legal framing.** Show these as questions for the controller/DPO, never as rulings:
- GDPR Art. 9(2) condition;
- Art. 28 processor agreement with the model provider;
- Chapter V transfer;
- Law 190 Art. 4 (CNP);
- Law 46 Arts. 21–22.

No registry change.

**Case reports and images:**
- narrative allowed without direct identifiers (relative dates, age in years, rare details generalised);
- never paste identifiable images; anonymised imaging is fine with DICOM metadata stripped.

**CNP hook (`hooks/cnp_guard.py`):**
- opt-in, offered by `install.py`, for Claude Code `UserPromptSubmit` + `PreToolUse(Read)`;
- blocks on a checksum-valid CNP: 13 digits, valid sex/century digit, valid date, valid county code, checksum with weights `279146358279`;
- no heuristic name or address detection;
- other runtimes rely on the preamble alone.

## 9. Venues

*From: Target-venue support and indexing checks; Venue landscape research.*

**Venues covered:**
- international journals: ERS journals (ERJ + ERJ Open Research, one entry), AJRCCM, CHEST, Thorax, Respiratory Medicine, IJTLD;
- open access / Romanian: *Medicina*, *Pneumologia*, RJME, *Maedica*;
- congresses: ERS Congress, and the SRP congress English half.

**Venue notes (`references/venue_notes.md`):** per-venue values, each with source URL, `verified_at` and evidence tag: abstract structure and limit with unit, text/reference limits, extras, citation style, required checklists, AI-disclosure placement, APC.
- At intake the preamble shows the row as "what the overlay found; check current author instructions". The scholar declares the values they confirm into core's venue profile (`declared_by: scholar`).
- **Never pre-fill a venue-profile file.** Unconfirmed fields stay null and report NOT-CHECKED.

**Venue extras:** `venue_extras.schema.json` (scholar-declared) covers what the core venue profile can't hold:
- abstract character limit + counting rule;
- required abstract headings;
- highlights / key messages / plain-language summary;
- checklists required with submission.

`check_venue_extras.py` checks them. ERS: 1810 characters including spaces for body + tables + figures; each table cell +1 character, each figure +277; title separate, ≤250 characters.

**AI disclosure:** the venue notes carry placement as advisory; core's unknown-venue path governs rendering. *Maedica*'s "≤30% AI" is flagged for the author, never claimed as met.

**Venue-status check:** advisory, at submission readiness, never blocking and never ranking venues. It covers five items, each recorded with URL + date:
- Clarivate MJL;
- Scopus discontinued list;
- NLM Catalog;
- current UEFISCDI SCIE/ESCI list;
- manuscript–journal scope fit (RJOR precedent).

Indexing is never cached. A journal's own claims never count.

***Pneumologia*:** ship the known facts (English-only, Scopus-only, not WoS Core, out of MEDLINE since 2016, no fee, SRP prize link). Format fields stay unverified until the verification pass (§10.4).

## 10. Fact verification

*From: Fact-verification policy for overlay content.*

### 10.1 Evidence tags
`primary-full-text`, `primary-abstract`, `secondary`, `recalled`, `unreachable`. Mapping onto core `freshness`:
- both primary tags → `current` + `verified_at`;
- `secondary` → `unverified`;
- `recalled` and `unreachable` are never encoded.

### 10.2 Encoding rule
- **Both primary tags:** fact; may drive checks at the grades set in this spec.
- **`secondary`:** advisory with a visible "verify" caveat, never a check.
- **`recalled` / `unreachable`:** not encoded.
- **Numeric thresholds** need ≥ `primary-abstract` where the abstract states the number.
- **Legal texts:** `authoritative_unofficial` → `official_controlling_language` after an official-portal check.

### 10.3 Recording and lint
Every encoded value records URL, title, locator, tag, `verified_at`, and edition/version where one exists. Registry deltas use the native source fields and receipts. References use table columns.

`check_overlay.py` fails on:
- a missing tag, date or URL;
- an encoded `recalled` or `unreachable` value;
- a `secondary` number used as a check;
- a profile that doesn't validate;
- a generated registry that is stale or invalid.

**Staleness:** a value is demoted to advisory past `verified_at` + 12 months (clinical standards, legal texts) or + 6 months (venue notes). `edition_watch.md` lists standards with known cycles (GOLD/GINA yearly, AASM, TNM, WSPH, ESC PE expected 2027) and flags their references for re-check. There are no automatic web re-checks.

### 10.4 Verification backlog (input to slice S2)
- **Values to re-verify:** every value tagged recalled / snippet / unverified / citation-only in the research branches (normalise to the §10.1 tags first). These include:
  - GOLD FEV1 grade cut-offs, the CNAS protocol list, AQLQ MID, sweat-chloride thresholds, Fuchs criteria;
  - PPF decline thresholds, AASM hypopnoea rule, ESC PE risk classes, IPF 6MWD MCID, Epworth MCID, OSA driving order and IPF protocol texts, screening eligibility;
  - Romanian silicosis counts, ENSP edition, Eurobarometer 2024 RO figure, RSV policy, rehab reimbursement, CURB-65, Berlin bands, NIV pH threshold.
- **Venue gaps:** *Pneumologia* author instructions; CHEST abstract limit, APC and GenAI policy; AJRCCM reference style, checklists and fees; Thorax figures and checklist mandate; Respiratory Medicine 2024 snapshot; WoS status of the international journals.
- **Legal texts on legislatie.just.ro:** OUG 29/2022 consolidated, Law 46/2003, Law 190/2018, OMS 3390/2022, OMS 330/2023, Law 199/2023 article number, the CMR Code 2025.
- **Outcome per value:** primary → promote; secondary only → advisory; unreachable or contradicted → drop. Verification counts when an agent fetch records URL + date + quoted locator. A clinician can upgrade a value with a signed note.

## 11. Tests and evals

*From: Romanian eval cases for the overlay.*

### 11.1 Deterministic (pytest, `tests/`, run by `check_overlay.py` and CI)
- CNP guard: valid and invalid checksums, dates and county codes; no hits on eponyms or phone numbers.
- `check_venue_extras`: the ERS counting rule with penalties; heading list.
- `check_overlay` lint: one case per failure condition in §10.3; stale demotion.
- Generators: delta merges into the current upstream registry; digests re-pinned; checks pass; a RO context resolves and replays; the pathway trace and packet manifest build and validate (port the probe from `research/ro-hs-alt-registry`).
- Profile: validates; `select` emits a receipt.

Run with Python ≥3.10 plus `pyyaml` and `jsonschema`. The macOS system `python3` 3.9 fails core lints.

### 11.2 Model-behaviour (`plugin-evals/`, core plugin-eval format)
`NN-case/prompt.md` + `graders/*.md`, fictional data only. Each case loads `ACTIVATE.md`, and a `tool_used` grader checks it was read. Run with `claude plugin eval . --eval-dir overlays/ro-respiratory-medicine/plugin-evals --ablation none --model sonnet --judge-model opus --runs 1 --no-publish`.
1. Romanian author names: comma-below in generated text, publisher cedilla kept in quoted data, English output.
2. Retrospective-cohort ethics dialogue: routing question asked, no waiver offered, Art. 22 risk shown, missing approval graded Conditional, no refusal.
3. Direct identifiers pasted: stops once, no echo in the reply or files, asks for a redacted re-paste.
4. Routine-records COPD "GOLD E" cohort: RECORD asked, edition year asked, STROBE route unchanged.
5. Venue notes: the agent asks the scholar to confirm and doesn't write values itself; undeclared fields report NOT-CHECKED.
6. Fallback COPD-exacerbation RCT: CONSORT from core, ERS 2022 outcome set + MCIDs, no first-class add-ons.

The README records a dated verification section like core's.

## 12. Implementation slices

One slice per delegated task. Each is merged only when its acceptance check passes. No core file changes in any slice.

| # | Slice | Depends on | Acceptance |
|---|---|---|---|
| S1 | Skeleton: directory, `MANIFEST.json`, `check_overlay.py` (lint rules of §10.3 against empty/fixture data), `ro-overlay.yml` CI, glossary in place | — | CI green; the §11.1 lint tests pass |
| S2 | Verification pass: normalise tags, work the §10.4 backlog, emit verified data tables (one per reference area) | S1 | Every table passes `check_overlay`; a backlog report lists promoted/advisory/dropped per value |
| S3 | Field profile (§4) | S1 | Profile tests pass; digest in `MANIFEST.json` |
| S4 | Human-subjects delta + generator (§5.1–5.2) | S1, S2 (legal sources) | Generator tests pass; RO context resolves, replays, trace + manifest build |
| S5 | Review-criteria delta + generator (§5.3) with receipts | S1, S2 | `validate_registry` passes; rows with non-current sources resolve as advisory |
| S6 | Subdomain references, design add-ons, data sources, citations, reviewer prompts, edition watch (§6) | S2 | `check_overlay` green; every row tagged and dated |
| S7 | Venue notes, venue extras schema, `check_venue_extras.py` (§9) | S2 | Venue-extras tests pass; notes rows tagged and dated |
| S8 | Patient-data preamble section + `hooks/cnp_guard.py` (§8) | S1 | CNP tests pass; hook only installed on opt-in |
| S9 | `ACTIVATE.md` + `install.py` (§3.2), wiring S3–S8 | S3–S8 | Installer is idempotent (tested); preamble names every generated path |
| S10 | Plugin evals (§11.2) | S9 | All six pass at `--runs 1`; results recorded in README |
| S11 | `docs/UPSTREAM_ASKS.md` (§13) | — | Drafts written; **not filed** without Val's approval |

## 13. Upstream asks (draft only; filing needs Val's approval)

1. Registry layering (core + overlay files) for both JSON registries, instead of full-copy generation.
2. A consumer for research-workflow profiles (#742), plus `display_name` open to more locales; offer `respiratory_medicine` as the first shipped clinical profile.
3. Ship the reserved `clinical` domain evidence profile.
4. Character-limit abstracts (unit + counting rule) in `venue_profile.schema.json`.
5. AI-disclosure database rows for ERS, ATS, Elsevier, IJTLD and MDPI in `academic-paper/references/venue_disclosure_policies.md`.
6. Core reference fixes: CONSORT 2010 → 2025, SPIRIT 2025, CTIS/ISRCTN/ICTRP in the pre-registration guide, RECORD depth.
7. A generic ERS/ATS `field_society_standard` row and RECORD/STROME-ID `reporting_design_overlay` rows in the core review-criteria registry.
8. A `professional_body` `authority_level` value (today the CMR Code uses `national` + a note).
9. The `check_human_subjects_reference_migration.py` requirement-id scanner only recognises `us.`/`tw.`/`eu.gdpr.` prefixes. Ask for a registry-driven prefix list.

## 14. Definition of done (v1)

- All slices S1–S11 merged in the fork.
- `check_overlay.py` and the deterministic suite green in CI.
- The six plugin evals passed once with the Codex runner (`plugin-evals/run_codex.py`), recorded with date, Codex version and model.
- `UPSTREAM_ASKS.md` written.
- No diff against upstream outside `overlays/ro-respiratory-medicine/` and `.github/workflows/ro-overlay.yml`.

## 15. Open risks

- **Upstream Phase-2 loader** (locale packs, registry layering) may land with a different shape. The overlay then migrates and the generators are retired.
- **Registry digests rotate** with every upstream release, so user contexts must be re-pinned. Activation docs must say so.
- **Legal uncertainty stays visible, not solved:** no Romanian research consent waiver; the Art. 9(2)(j) basis is unclear; the legal basis of hospital ethics committees is unclear.
- **Fallback for the human-subjects registry** if a future upstream change breaks the generated copy: ship only the review-criteria copy and carry the ethics content in the preamble.
- **Two decisions were auto-approved without Val's live answer:** the eval set (§11) and the spec shape and slicing (§12), together with ruling the pilot clinician out of scope. Review these first.
