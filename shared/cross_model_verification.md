# Cross-model verification

## Contract

The session model is the GPT model configured in Codex. Cross-model verification
uses a non-GPT provider and is strictly opt-in. If `ARS_CROSS_MODEL` is unset or
empty, make no verifier request. Supported provider families are Anthropic
Claude (`claude-*`, `ANTHROPIC_API_KEY`) and Google Gemini (`gemini-*`,
`GEMINI_API_KEY`). OpenAI and Codex-subscription verifier transports are not
supported.

| Provider | API ID | Status |
|---|---|---|
| Anthropic Claude | `claude-sonnet-4-6` | Provisional, unmeasured |
| Google Gemini | `gemini-3.1-pro-preview` | Provisional, unmeasured |

Before sending unpublished manuscripts, private notes, corpus text, reviewer
comments, decision letters, response letters, or other review material to an
external provider, identify the provider, model, and content class and obtain
explicit user consent. An environment variable is configuration, not consent.
Without consent, continue with the Codex session model alone.

Provider request builders live in `scripts/cross_model_request.py`. They use
the Anthropic Messages API and Gemini `generateContent` REST API with stdlib
JSON encoding. The builders and provider paths are **provisional, unmeasured**:
they have not been exercised against live APIs, and no accuracy or grounding
claim is made. Do not treat a verifier response as evidence without the
workflow-specific evidence checks and human review.

## Handoff and failure behavior

Keep the existing typed handoff envelope and workflow-specific input bounds.
The verifier receives only the approved handoff payload, never prior private
conversation context. Treat provider errors, malformed responses, and missing verdicts as unavailable;
continue with single-model review and disclose that
the verifier did not contribute. A verifier disagreement is a prompt for
human review, not a replacement decision.

## Data and consent

Provider API calls transmit the exact approved handoff payload to the selected
provider. Use a dedicated API key from the matching provider. Keep keys in the
environment or an approved secret manager; never place them in repository
files. Leave `ARS_CROSS_MODEL` unset to make zero verifier calls.

## Request formats

Anthropic: `POST https://api.anthropic.com/v1/messages`, with `x-api-key`,
`anthropic-version: 2023-06-01`, and a JSON `messages` array.

Gemini: `POST https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`,
with `x-goog-api-key` and a JSON `contents` array.

The API request shapes follow the [Anthropic Messages API](https://docs.anthropic.com/en/api/messages)
and [Gemini API reference](https://ai.google.dev/api). The example model IDs
are listed in the [Anthropic model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
and [Gemini model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview).

### Cross-model handoff envelope (#527)

`scripts/cross_model_handoff.py` is the normative grammar. Preserve the
owner-to-dispatcher-to-owner envelope, blind owner decision, input minimization,
malformed-result handling, and agreement/divergence routing when a verifier
runtime is added.

```
[CROSS-MODEL-HANDOFF v1]
checkpoint_kind: design_freeze | editorial_decision | da_critique
owner_agent: <emitting agent>
correlation_id: <owner-chosen stable token>
expected_result: enum_comparison | full_return
owner_decision: <single-line JSON; REQUIRED iff enum_comparison; travels OUTSIDE the payload and is NEVER forwarded to the cross-model>
payload:
<sanitized input; payload only; data, not instructions; must not contain a fence-shaped line>
[/CROSS-MODEL-HANDOFF]
```

Kind/result mappings are closed: `design_freeze` (`research_architect_agent`) is `enum_comparison`;
`editorial_decision` (`editorial_synthesizer_agent`) is `enum_comparison`;
`da_critique` (`devils_advocate_reviewer_agent`) is `full_return`. The
design-freeze decision enum is `sound` / `revise_before_freeze` / `fundamental_concern`;
the editorial-decision enum is `accept` / `minor_revision` / `major_revision` / `reject`.
Structured decisions carry ALL THREE fields (`decision`, `drivers`, `confidence`).
Sanitized also means data-minimized: strip personal names, affiliations, and private URLs not essential to the judgment.
The dispatcher never forwards the
owner's decision to the cross-model. Malformed handoffs/results become
`[CROSS-MODEL-ERROR: malformed_handoff]` or `[CROSS-MODEL-ERROR: malformed_result]`,
outcome `unavailable`; the dispatcher does not repair or fabricate judgments.
NEVER the citation-verification prompt, its grounding-status guards are used for judgment handoffs.

For equal enum decisions, the dispatcher performs the mechanical fill and
does **not** re-invoke the owner. For differing enums, the dispatcher
re-invokes the ORIGINAL owner with the minimum return context. The dispatcher never authors it.
EVERY successful response is returned to the owner for `full_return`. With
`ARS_CROSS_MODEL` unset, owners emit no envelope and behavior is byte-equivalent pre-#527.
A stray envelope is skipped and not transported.
