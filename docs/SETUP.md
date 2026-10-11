# ARS Setup

Use the Codex plugin to make the five ARS skills available across projects. Link individual skills into `.agents/skills/` when you need only a project or user install.

## Install the Codex plugin

### Method: Install as a Codex plugin

From the CLI, add the marketplace and install the plugin:

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

In the Codex desktop app, open the plugin manager, add the `ars` marketplace, and install `academic-research-skills`. The plugin cache contains real copies of the skills plus the shared references and root scripts they use.

## Project skills

### Method: Project skills

Clone the repository, set `ARS_REPO` to its path, then add symlinks to the project:

```sh
ARS_REPO=/path/to/academic-research-skills
mkdir -p .agents/skills
for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline sr-screener; do
  ln -s "$ARS_REPO/$skill" ".agents/skills/$skill"
done
```

## User skills

### Method: User skills

Put the same symlinks in `~/.agents/skills/` for user-wide access. Keep the repository clone available: each skill resolves `shared/...` and root `scripts/...` by walking up to the ARS root; its own `scripts/...` paths resolve from the skill directory.

## Optional Python tools

The prompts need no extra runtime. Install Python 3.10 or newer for script-backed workflows and repository checks. `openpyxl` is optional and enables Excel output from `sr-screener`.

## Document output

Markdown needs no extra software. Install Pandoc for DOCX conversion. PDF output also needs a LaTeX engine such as Tectonic; see its [installation guide](https://tectonic-typesetting.github.io/en-US/install.html).

## Project preferences

Put project-specific standing preferences in that project's `AGENTS.md`. ARS does not load preferences from a global ARS configuration file; keeping search and inclusion criteria with the project makes them visible during review.

The optional deep-research reading probe is enabled with
`ARS_SOCRATIC_READING_PROBE=1`; it is off by default. See the
deep-research skill's reading-probe instructions.

## Cross-model verification (optional)

Cross-model verification is implemented as an opt-in stdlib API call. It is provisional and unmeasured; no live API validation is claimed. The session model remains the configured Codex GPT model. A verifier call sends the selected reference and context to the external provider, so obtain explicit per-session user consent before sending unpublished content. Leave `ARS_CROSS_MODEL` unset to disable it. See [Cross-model verification](../shared/cross_model_verification.md) for the contract.

The model IDs and provider behavior remain provisional and unmeasured. Invoke
the CLI only after consent, with one reference per call:

```sh
# Choose one provider; leave ARS_CROSS_MODEL unset to disable verification.
export ARS_CROSS_MODEL="claude-sonnet-4-6"
export ANTHROPIC_API_KEY="<your-anthropic-api-key>"
# Or:
# export ARS_CROSS_MODEL="gemini-3.1-pro-preview"
# export GEMINI_API_KEY="<your-gemini-api-key>"
```

```sh
printf '%s' '{"reference":"Doe, J. (2024). Example. doi:10.1234/example","context":"supports claim X"}' | python scripts/cross_model_verify.py --consent
```

The JSON output records the actual provider and model. Transport failures,
malformed responses, and safety blocks return `unavailable` without a verdict.

## Control availability

Plugin, project-skill, and user-skill installs have different boundaries. See [Control availability](CONTROL_AVAILABILITY.md) before relying on a control.
For external API endpoints and data sent, see [Data flows](DATA_FLOWS.md).
