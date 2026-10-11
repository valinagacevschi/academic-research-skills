# Session model and reasoning effort

ARS uses the GPT model configured for the current Codex session. Skills and subagents do not select another session model or apply Sonnet/Opus/Haiku-style tiers.

For complex synthesis, high-stakes review, adjudication, or systematic screening, use high reasoning effort when Codex exposes that setting. Routine extraction and formatting can use the session's normal effort. The skill may recommend effort for a role, but it must not change the configured model.

For independent cross-model verification, use the separately configured non-GPT verifier only when `ARS_CROSS_MODEL=1` is explicitly enabled. See [`cross_model_verification.md`](cross_model_verification.md).
