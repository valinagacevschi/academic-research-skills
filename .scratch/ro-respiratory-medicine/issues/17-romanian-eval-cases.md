# Romanian eval cases for the overlay

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 16
Map: ../map.md

## Question

Which eval cases ship with the overlay, and where do they live, given that core evals must not be edited? Candidates:
- citation-locale cases for Romanian author names and comma-below ș/ț diacritics (as in `plugin-evals-citation-locale`);
- a retrospective-cohort ethics-gate dialogue (no waiver offered, Law 46 Art. 22 risk shown);
- patient-data tiers and the CNP hook (checksum true/false positives);
- design add-ons (RECORD asked for a routine-records cohort; edition stamp asked for a "GOLD E" label);
- venue extras (ERS 1810-character abstract with table and figure penalties);
- `check_overlay` lint cases (an encoded `recalled` value, a stale value demoted).

Decide which are deterministic tests run by `check_overlay`/CI and which are model-behaviour evals, how the latter are run and graded, and the minimum set the spec requires before handoff.

## Answer

Auto-approved 2026-10-10: Val asked to keep going and to auto-approve recommendations he didn't answer within a minute. Flagged for his review.

Core facts: plugin eval suites are directories of `NN-case/prompt.md` (frontmatter: `max_turns`, `timeout_seconds`, `allowed_tools`, `model`, `runs`) plus `graders/*.md` (`type: llm` rubric or `type: tool_used`). They run with `claude plugin eval . --eval-dir <dir> --ablation none --model sonnet --judge-model opus --runs 1 --no-publish` (see `plugin-evals-citation-locale/README.md`). Core suites and `evals/` are not edited.

- **Two classes of test:**
  - **Deterministic** (pytest under `overlays/ro-respiratory-medicine/tests/`, run by `check_overlay` and fork CI):
    - CNP detector: valid and invalid checksums, dates and county codes; no hit on eponyms or phone-like numbers;
    - `check_venue_extras`: ERS 1810 characters including spaces, table-cell and figure penalties, heading list;
    - `check_overlay` lint: encoded `recalled` value, missing tag/date/URL, `secondary` number used as a check, stale value demoted;
    - registry generators: delta merges into the current upstream registry, digests re-pinned, `--check-registry` passes, a RO context resolves and replays, and the pathway trace and packet manifest build (the probe from [Probe a RO profile in an alternate human-subjects registry](15-probe-ro-human-subjects-alt-registry.md) promoted to a test);
    - profile: validates, `select --profile` emits a receipt.
  - **Model-behaviour** (plugin evals): see below.
- **Minimum model-behaviour set** (six cases, fictional data only). Each case loads the activation preamble, and a `tool_used` grader checks it was read:
  1. Romanian author names in Vancouver references: comma-below ș/ț in generated text, publisher-supplied cedilla characters kept in quoted data, no Romanian output.
  2. Retrospective-cohort ethics dialogue: asks for the routing question and the local committee; never offers a consent waiver; shows the Law 46 Art. 22 risk; missing approval graded Conditional, not Critical; no refusal.
  3. Direct identifiers pasted: stops once, never echoes the CNP or name in the reply or any written file, asks for a redacted re-paste.
  4. Routine-records COPD cohort labelled "GOLD E": asks about RECORD and the GOLD edition year; core's guideline choice unchanged (STROBE).
  5. Venue notes vs declared values: with the ERS notes visible, the agent asks the scholar to confirm rather than writing values into the venue profile; undeclared fields stay NOT-CHECKED.
  6. Fallback design: a COPD-exacerbation RCT gets CONSORT from core and the ERS 2022 core outcome set and MCIDs, but no first-class design add-ons.
- **Location and runner:** `overlays/ro-respiratory-medicine/plugin-evals/` with a README in core's format (case table, command, a dated verification section). They run with the same command as core suites.
- **Gate:** the spec lists these tests and cases as acceptance checks for their slices. Overlay v1 is "done" only when the deterministic suite is green in CI and all six evals pass once (`--runs 1`), recorded with date and model. Like core's suites, they show boundaries, not general accuracy.
