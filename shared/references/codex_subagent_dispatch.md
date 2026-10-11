# Codex subagent dispatch

Use Codex subagents for multi-agent steps when `multi_agent` is available. For each role:

1. Spawn a subagent and give it the matching role prompt file as its instructions. Include only that role's required input files, explicit user constraints, and the output contract.
2. Keep blind roles isolated. Start each reviewer without access to another reviewer's output, identity, or conclusions. Do not read or summarize one blind role's result into another role's context.
3. Collect every result after the blind calls finish. Preserve the role labels, validate outputs against the stated schema or handoff contract, then pass them to the designated synthesis or adjudication role.
4. Keep user decisions in the main session. A subagent recommendation cannot stand in for a user checkpoint.

## Sequential fallback

If Codex subagents are unavailable, use one role at a time. Before each blind role, reset the working context to that role's prompt and permitted source materials; do not carry prior role outputs into the next role. Collect outputs only after all blind roles finish. A single session cannot guarantee the same independence as separate subagent contexts; disclose that limitation in the report and label the reviews as sequential.
