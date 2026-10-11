# Codex-only conversion progress

- Branch: `codex-only`, based on `main`; no push.
- Phase 1: complete, committed as `9361590`.
- Phase 2: complete. Codex subagent dispatch canonicalized, model tiering removed, sr-screener emits prompt files for Codex subagents, semantic locks updated. Targeted checks passed (116 tests).
- Phase 3: complete, committed as `7a784df`. Isolated plugin install confirmed cache copies; real skill directories and root discovery are in place.
- Phase 4: complete, committed as `b693c95`. Codex `PreToolUse` lacks a subagent role field, so ARS cannot enforce role-specific write scopes. Removed guard code and documented the residual gap. Focused tests/lints passed.
- Phase 5: committed as `26b0ced` at the explicitly permitted reduced scope. Rewrote the contract for non-GPT Anthropic/Gemini verification, added tested stdlib request builders, and removed the Codex-subscription transport and its dedicated checks. Runtime dispatch, response parsing, source/grounding validation, and live provider verification remain undone; current docs say the runtime is unavailable.
- Final full suite: run once as requested; it reported `70 failed, 9641 passed, 3 skipped, 115 errors`. Failures were stale Claude/JavaScript test expectations, deleted OpenAI-compat normalizer tests, stale command surface checks, and cross-model contract details dropped during the first rewrite. Follow-up restores those contracts, updates tests to Codex prompt files, and removes the obsolete normalizer test; targeted suites now pass (388 tests plus related lints). Full suite not rerun.
