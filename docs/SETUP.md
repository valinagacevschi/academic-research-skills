# ARS Setup

ARS runs in Codex. Install the plugin for use across projects, or link individual skills into a project or user skills directory. The core prompts need no Python; optional script-backed checks do.

## Minimum setup

1. Install Codex and sign in.
2. Install ARS using one of the options below.
3. Start a Codex session and ask it to use an ARS skill and mode.

## Install as a Codex plugin

From the Codex CLI, add the repository marketplace and install the plugin:

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

In the Codex desktop app, open the plugin directory, add the `ars` marketplace, and install Academic Research Skills. The plugin cache includes the bundled skills and shared references, so the skills work from other projects.

## Project skills symlink

Clone the repository, then link the skills into the project where you use Codex:

```sh
mkdir -p .agents/skills
for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline sr-screener; do
  ln -s /path/to/academic-research-skills/$skill .agents/skills/$skill
done
```

## User skills symlink

Use the same links under `~/.agents/skills/` to make ARS available across your projects.

## Optional Python tools

The prompt workflows work without Python. Install Python 3.10 or newer if you want to run the repository's local validation scripts or optional script-backed features.

## Document output

Markdown output needs no extra software. Install Pandoc for DOCX conversion. PDF output also needs a LaTeX engine such as Tectonic; see its [installation guide](https://tectonic-typesetting.github.io/en-US/install.html).

## Project preferences

Put project-specific standing preferences in that project's `AGENTS.md`. ARS does not load preferences from a global ARS configuration file; keeping search and inclusion criteria with the project makes them visible during review.

## Cross-model verification (optional)

Cross-model verification is off by default. It requires explicit opt-in and a non-GPT provider API key. See [Cross-model verification](../shared/cross_model_verification.md) for the current provider and data-flow details.

## Control availability

The plugin and project/user skill installs have different boundaries. See [Control availability](CONTROL_AVAILABILITY.md) before relying on a control.
