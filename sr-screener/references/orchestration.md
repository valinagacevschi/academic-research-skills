# Screening orchestration in Codex

For multi-agent screening, use Codex subagents and follow [the canonical dispatch procedure](../../shared/references/codex_subagent_dispatch.md). Give each reviewer its role prompt from `agents/screening_reviewer_agent.md`, plus only its required batch, protocol, and output contract. Keep Reviewer A and B blind to each other's results; adjudication receives the conflict set after both return.

`build_workflow.py --emit-prompts` prepares one prompt file per role call and an `index.json`; it does not invoke agents. Dispatch those prompts as Codex subagents, then save returned JSON using the labels in the index and merge with `merge_decisions.py --from`. If subagents are unavailable, run roles sequentially with the context reset and reduced-independence disclosure required by the canonical procedure.

For small sets, `quick` mode is single-reviewer triage, not independent double screening.
