# Session model and reasoning effort

ARS uses the GPT model configured for the current Codex session. Skills and subagents do not select another session model or apply provider-specific tiers.

For complex synthesis, high-stakes review, adjudication, or systematic screening, use high reasoning effort when Codex exposes that setting. Routine extraction and formatting can use the session's normal effort. The skill may recommend effort for a role, but it must not change the configured model.

For independent cross-model verification, set `ARS_CROSS_MODEL` to a non-GPT verifier model ID and provide the matching API key. Leave it unset to disable verification. See [`cross_model_verification.md`](cross_model_verification.md).
