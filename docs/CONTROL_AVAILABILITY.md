# Control Availability by Install Channel

ARS is a Codex-only skill suite. Install it as a Codex plugin for normal use, or expose the skill folders through a project or user skills directory.

## Install channels

| Channel | Setup | Scope |
|---|---|---|
| Codex plugin | [Plugin setup](SETUP.md#method-install-as-a-codex-plugin) | User-level install, available across Codex projects |
| Project skills | [Project skills setup](SETUP.md#method-project-skills) | One project |
| User skills | [User skills setup](SETUP.md#method-user-skills) | All projects for one user |

## Availability matrix

| Capability | Plugin | Project skills | User skills |
|---|---|---|---|
| Five ARS skills | Active | Active | Active |
| Codex subagents | Active when enabled; otherwise use the documented sequential fallback | Same | Same |
| Cross-model verification | Runtime unavailable; provider request builders are provisional and unmeasured | Same | Same |
| Write-scope guard | Unavailable on Codex: `PreToolUse` can block writes, but its documented payload has no subagent role field, which ARS needs for per-role scopes ([Codex Hooks](https://learn.chatgpt.com/docs/hooks)) | Same | Same |

Codex plugins are installed in a local cache. Skill guidance must resolve its bundled `shared/` and `scripts/` paths from the installed plugin tree; it must not depend on the current project's root.
