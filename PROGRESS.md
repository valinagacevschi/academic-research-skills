# Codex-only conversion progress

- Branch: `codex-only`, based on `main`; no push.
- Phase 1: complete, committed as `9361590`.
- Phase 2: complete. Codex subagent dispatch canonicalized, model tiering removed, sr-screener emits prompt files for Codex subagents, semantic locks updated. Targeted checks passed (116 tests).
- Phase 3: plugin experiment completed in isolated `CODEX_HOME`: plugin cache is a copy; `skills/` symlinks were dropped; `shared/` was copied at plugin root. Implementing root discovery and real skill directories remains.
- Phase 4: Codex `hooks` stable. Official `PreToolUse` supports blocking `apply_patch`/Edit/Write and Bash with `permissionDecision: deny`; port and test the scope guard.
- Phase 5: pending.
