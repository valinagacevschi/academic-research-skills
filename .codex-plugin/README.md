# Academic Research Skills for Codex

Install the plugin to use ARS skills across Codex projects. The plugin bundles real skill directories under `skills/` because Codex's plugin cache copies the tree and drops symlinks. Shared references and root scripts ship alongside those skills.

## Codex CLI

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

## Codex desktop app

Open the plugin manager, add the `ars` marketplace, then install `academic-research-skills`. The installed plugin exposes the same five skills as the CLI.

## Project or user skills

For a project-specific install, clone the repository and symlink the skill folders into `.agents/skills/`. To make them available across projects, use `~/.agents/skills/` instead. Set `ARS_REPO` to the clone path in the commands below:

```sh
mkdir -p .agents/skills
for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline sr-screener; do
  ln -s "$ARS_REPO/$skill" ".agents/skills/$skill"
done
```

Each skill locates the ARS root by walking upward from its resolved directory to the directory containing `shared/` and root `scripts/`. Its own `scripts/` directory stays relative to the skill.

See [setup](../docs/SETUP.md) and [control availability](../docs/CONTROL_AVAILABILITY.md) for requirements and install-channel limits.
