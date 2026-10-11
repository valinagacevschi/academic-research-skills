# ARS Setup

Use the Codex plugin to make the five ARS skills available across projects. Link individual skills into `.agents/skills/` when you need only a project or user install.

## Install the Codex plugin

From the CLI, add the marketplace and install the plugin:

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

In the Codex desktop app, open the plugin manager, add the `ars` marketplace, and install `academic-research-skills`. The plugin cache contains real copies of the skills plus the shared references and root scripts they use.

## Project skills

Clone the repository, set `ARS_REPO` to its path, then add symlinks to the project:

```sh
ARS_REPO=/path/to/academic-research-skills
mkdir -p .agents/skills
for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline sr-screener; do
  ln -s "$ARS_REPO/$skill" ".agents/skills/$skill"
done
```

For user-wide access, put the same symlinks in `~/.agents/skills/`. Keep the repository clone available: each skill resolves `shared/...` and root `scripts/...` by walking up to the ARS root; its own `scripts/...` paths resolve from the skill directory.

## Optional Python tools

The prompts need no extra runtime. Install Python 3.10 or newer for script-backed workflows and repository checks. `openpyxl` is optional and enables Excel output from `sr-screener`.

## Document output

Markdown needs no extra software. Install Pandoc for DOCX conversion. PDF output also needs a LaTeX engine such as Tectonic; see its [installation guide](https://tectonic-typesetting.github.io/en-US/install.html).

## Project preferences

Put project-specific standing preferences in that project's `AGENTS.md`. ARS does not load preferences from a global ARS configuration file; keeping search and inclusion criteria with the project makes them visible during review.

## Cross-model verification (optional)

Cross-model verification is off by default. It requires explicit opt-in and a non-GPT provider API key. See [Cross-model verification](../shared/cross_model_verification.md) for provider and data-flow details.

## Control availability

Plugin, project-skill, and user-skill installs have different boundaries. See [Control availability](CONTROL_AVAILABILITY.md) before relying on a control.
