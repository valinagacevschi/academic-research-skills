<!-- 2026-10-11: removed the duplicated release history. Kept the skill table, routing core, routing rules, and version pins. -->
# Academic Research Skills (ARS)

Codex skills for research, writing, peer review, and pipeline orchestration. Use the Codex session model and Codex subagents; dispatch via `shared/references/codex_subagent_dispatch.md`.

## Skills Overview

| Skill | Purpose | Key Modes |
|-------|---------|-----------|
| `deep-research` v2.12.1 | 13-agent research team | full, quick, socratic, review, lit-review, three-way-scan, fact-check, systematic-review |
| `academic-paper` v3.3.1 | 12-agent paper writing | full, plan, outline-only, revision, revision-coach, abstract-only, lit-review, format-convert, citation-check, disclosure, rebuttal-audit |
| `academic-paper-reviewer` v1.11.1 | Multi-perspective paper review (5 reviewers + optional cross-model DA critique) | full, re-review, quick, methodology-focus, guided, calibration |
| `academic-pipeline` v3.23.0 | Full pipeline orchestrator | (coordinates all above) |
| `sr-screener` v1.0.0 | Protocol-driven study screening (2 blinded AI reviewers + adjudicator) | protocol, quick, pilot, ta-screen, ft-screen, adjudicate, audit, report |


## Routing Discipline (v3.9.2)

This section runs before Routing Rules. After it settles on a skill, the rules below apply inside that skill.

<!-- routing-core:begin -->
**Step 0 — Escape hatch check (before any classification):** If the user's first message begins with `[direct-mode]` (case-insensitive byte-0 token, optionally preceded by whitespace/newlines that are stripped on parse), record this fact, strip the prefix and surrounding whitespace from the message, and skip directly to **Step 1 explicit-intent handling** on the stripped content. The literal `[direct-mode]` is NOT passed through to the dispatched agent. If the stripped message itself has no clear skill named, Step 1 falls through to Step 3 clarification (the escape hatch bypasses cross-phase clarification (Step 2), not all routing). When the token is honored and the named agent or skill needs inputs the message does not supply, read that agent's or skill's file and ask for what it requires, in its terms. Without the byte-0 token, naming an agent is not explicit intent: such a message goes through Steps 1-3 like any other, so cross-phase materials still get Step 2 clarification.

Otherwise, classify the user's input:

1. **Explicit clear intent** — user invokes a specific skill by name with its mode (for example `$academic-paper lit-review`), or uses an unambiguous trigger keyword that maps to a single skill (e.g., "lit-review this", "review my paper", "draft an abstract"):
   → Route directly; no clarification, no orchestrator detour.
   → The request stays explicit when the mode's usual input is absent or a word in it has other everyday senses. A revision request with no reviewer comments is revision mode's "feel certain sections need improvement" case, and "revisar artículo" is the reviewer's trigger. Route to that mode and let the mode handle what is missing; do not reopen the choice of workflow.

2. **Cross-phase materials detected** — user provides artifacts spanning ≥ 2 pipeline phases without naming a specific skill (e.g., pre-written abstract + pre-collected literature; full draft + reviewer comments + bibliography):
   → **Clarify**. Do NOT auto-route to a single-phase agent. List candidate workflows as a-d options in markdown body (NOT via AskUserQuestion tool). See `shared/references/intent_clarification_protocol.md` for the message template.
   → Reason: clarification is the safest action when materials don't unambiguously identify intent. (v3.10 active conductor (#134) will handle this via structured intake; v3.9.2 asks.)

3. **Ambiguous intent, no materials** — user provides no artifacts and no clear request:
   → Clarify per `shared/references/intent_clarification_protocol.md`.

**Screening boundary (sr-screener):** a request to screen records the user already has (database exports, pasted abstracts, full-text PDFs) against a review's eligibility criteria, or to build a screening protocol, pilot the screening, adjudicate screening conflicts, audit exclusions, or report the selection counts, routes to `sr-screener`. A request to write a literature review, or to run a systematic review, meta-analysis, or PRISMA report, does not route to `sr-screener`. Screening starts only when the user asks for it: `deep-research` `systematic-review` mode may mention `sr-screener`, but never hands over to it automatically.

**Anti-pattern (caused #133):** Receiving ambiguous cross-phase materials and silently auto-routing to a single-phase agent based on which phase the materials "look closest to." This bypasses orchestrator-level reconciliation and lets the subagent inherit the full ambiguity without independent oversight.
<!-- routing-core:end -->

## Routing Rules

1. **Pipeline vs one skill.** `academic-pipeline` runs research, writing, integrity, review, revision, and finalization. A single job (research, writing, or review only) goes to that skill.
2. **Research vs writing.** `deep-research` investigates and fact-checks. `academic-paper` writes the paper. An unclear question uses `deep-research` socratic. Thinking through structure uses `academic-paper` plan. Learning from a review uses `academic-paper-reviewer` guided; a standard report uses full.
3. **Rebuttal vs revision.** `academic-paper rebuttal-audit` only when the user supplies both reviewer comments and an existing rebuttal draft. It checks that draft and generates nothing, emits no Schema 11, and marks nothing verified. Comments alone go to `revision-coach`. If both might be present, ask.
4. **Committee correspondence.** Use the `revision-coach` committee variant only when the user names a real committee or institutional review office. Formal tone does not establish that authority. Load `academic-paper/references/committee_correspondence_protocol.md`, preserve the source, and emit its concern tracker. Do not emit reviewer priority, severity, Schema 11, a determination, or a resolution claim.
5. **Screening vs systematic review.** Records the user already has, or a request to protocol, pilot, adjudicate, audit, or report selection counts, go to `sr-screener`. Writing the review (question, search, synthesis, PRISMA report) goes to `deep-research` `systematic-review`. A bare "systematic review" or "PRISMA" stays there. Flow numbers for a finished screening go to `sr-screener` `report`. Other skills read its `literature_corpus[]` and do not re-screen it. `systematic-review` never hands over to `sr-screener` on its own.

## Key Rules

- Cite claims. Rank evidence (meta-analyses, then RCTs, cohorts, case reports, expert opinion). Disclose contradictions with that ranking. Disclose AI use in every report.
- Match the user's language (Traditional Chinese or English).
- A review panel may include a blind and separately executed Devil's Advocate critique. These execution facts are not a binary independence claim. Keep the consent gate and blind handoff in `shared/cross_model_verification.md`.

## Pipeline

`deep-research` (socratic/full) → `academic-paper` (plan/full) → integrity (Stage 2.5) → `academic-paper-reviewer` (full/guided) → `academic-paper` (revision) → `academic-paper-reviewer` (re-review, max 2) → integrity (Stage 4.5) → `academic-paper` (format-convert) → process summary and AI self-reflection.

## Handoffs

- **deep-research → academic-paper:** RQ Brief, Methodology Blueprint, Annotated Bibliography, Synthesis Report, INSIGHT Collection.
- **academic-paper → academic-paper-reviewer:** full paper. `field_analyst_agent` detects the domain and configures reviewers.
- **academic-paper-reviewer → academic-paper revision:** Editorial Decision Letter, Revision Roadmap, per-reviewer comments.
- **systematic review:** protocol, database exports, and full texts in; `*_literature_corpus.yaml`, PRISMA 2020 counts, methods draft, exclusion reasons, and screening log out.

## Version Info

- **Suite version**: 3.23.0
