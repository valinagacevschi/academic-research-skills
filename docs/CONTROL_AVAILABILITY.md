# Control Availability by Install Channel

ARS is a Codex-only skill suite. Install it as a Codex plugin for normal use, or expose the skill folders through a project or user skills directory.

## Install channels

| Channel | Setup | Scope |
|---|---|---|
| Codex plugin | [Plugin setup](SETUP.md#install-as-a-codex-plugin) | User-level install, available across Codex projects |
| Project skills | [Project skills setup](SETUP.md#project-skills-symlink) | One project |
| User skills | [User skills setup](SETUP.md#user-skills-symlink) | All projects for one user |

## Availability matrix

| Capability | Plugin | Project skills | User skills |
|---|---|---|---|
| Five ARS skills | Active | Active | Active |
| Codex subagents | Active when enabled; otherwise use the documented sequential fallback | Same | Same |
| Cross-model verification | Opt-in with `ARS_CROSS_MODEL=1` and a supported non-GPT API key | Same | Same |
| Write-scope guard | See [Risk Register](RISK_REGISTER.md) | See [Risk Register](RISK_REGISTER.md) | See [Risk Register](RISK_REGISTER.md) |

Codex plugins are installed in a local cache. Skill guidance must resolve its bundled `shared/` and `scripts/` paths from the installed plugin tree; it must not depend on the current project's root.
