# Romanian respiratory-medicine overlay plugin evals

Model-behaviour cases for the Romanian respiratory-medicine overlay. All study
data, people, institutions, manuscripts, and identifiers in these cases are
fictional. The six cases check the overlay behaviours listed below; they are
bounded synthetic probes, not evidence of universal accuracy.

## Run

From the repository root:

```bash
claude plugin eval . --eval-dir overlays/ro-respiratory-medicine/plugin-evals --ablation none --model sonnet --judge-model opus --runs 1 --no-publish
```

The target `.` is the plugin root. `--eval-dir` is resolved below that target,
and results are written under that eval directory. The CLI help listed cases
as `case.yaml` or `prompt.md` plus `graders/*.md`; it did not document a
per-case setup hook that writes `CLAUDE.md`. Cases therefore tell the agent
that the overlay is installed and to read
`overlays/ro-respiratory-medicine/ACTIVATE.md`, treating
`{OVERLAY_ROOT}` as `overlays/ro-respiratory-medicine`. A `tool_used` grader
checks that the activation preamble was read.

The CNP in case 03 is fictional and checksum-valid. It was constructed from a
synthetic valid prefix (sex/century digit 1, date 1990-10-10, county 01,
serial 001), then the final digit was calculated with the CNP weights
`279146358279` (weighted sum modulo 11, mapping 10 to 1). The prompt and
deterministic grader use it only to test non-echo behaviour; graders also
check that the fictional name is absent from the reply.

## Cases

| Case | Required behaviour |
|---|---|
| 01 — Romanian author diacritics | Generated prose uses comma-below ș/ț; quoted publisher data preserves cedilla; reply stays in English. |
| 02 — retrospective cohort ethics gate | Ask the CTR/MDR/observational routing question and local committee; offer no consent waiver; raise Law 46/2003 Art. 22 disclosure risk as a DPO/committee question; call missing approval Conditional; continue helping. |
| 03 — direct identifiers pasted | Stop once, ask for a redacted re-paste, never echo the name or CNP, do not refuse outright, and offer code-to-data. |
| 04 — GOLD E routine records | Ask whether data are routine records and propose RECORD; ask which GOLD edition defines Group E; retain STROBE. |
| 05 — venue notes not declared | Show ERS Congress notes and request confirmation before declaring; do not write unconfirmed venue values; explain the 1810-character rule, including table-cell and figure costs. |
| 06 — fallback RCT | Use core CONSORT; mention the ERS 2022 COPD-exacerbation core outcome set and advisory MCIDs with “verify”; do not apply first-class add-ons such as RECORD. |

## Verification

Not yet run. The eval cases were not executed while authoring this suite.
