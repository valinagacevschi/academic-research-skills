# Quick Start (Codex)

Get from zero to your first AI-assisted research in 3 steps.

## Step 1: Install ARS

Install the plugin for use across projects:

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

For a project-only setup, link the five skill directories into `.agents/skills/`. See [setup options](docs/SETUP.md).

## Step 2: Launch

```bash
codex
```

## Step 3: Start researching

Ask Codex to use the relevant skill and mode. For example: “Use `deep-research` in Socratic mode to help me frame this idea.”

### Example: Guided research (Socratic mode)

```
You: "I have a vague idea about AI's impact on higher education quality assurance,
      but I'm not sure how to frame the research question. Can you guide me?"
```

Codex will use Socratic mode — asking questions to help you clarify your thinking, not giving you answers directly. After 5-15 rounds of dialogue, you'll have a focused research question and methodology direction.

### Example: Write a paper

```
You: "Help me write a paper about the impact of declining birth rates
      on private universities in Taiwan"
```

### Example: Review an existing paper

```
You: "Review this paper" (then paste or attach the paper)
```

### Example: Full pipeline (research → write → review → revise → publish)

```
You: "I want to produce a complete research paper about how agentic AI
      is reshaping student learning outcome measurement"
```

This triggers the full 10-stage pipeline, which stops at every stage for your confirmation. Token use and cost depend on your Codex model and account or API plan; see [docs/PERFORMANCE.md](docs/PERFORMANCE.md) for workload estimates. Expect the collaborative work to span hours to days, depending on how closely you review each stage.

## Which mode should I use?

| I want to... | Use this |
|-------------|----------|
| Explore a vague idea | `deep-research` socratic mode — just describe your interest |
| Get a quick literature summary | `deep-research` quick mode |
| Do a systematic review (PRISMA) | `deep-research` systematic-review mode |
| Write a paper from scratch | `academic-paper` full mode |
| Plan a paper chapter by chapter | `academic-paper` plan mode |
| Get my paper reviewed | `academic-paper-reviewer` full mode |
| Go from question to finished paper, confirming each stage | `academic-pipeline` — say "I want a complete research paper" |

## What's next?

- [Full README](README.md) — all features, modes, installation options, and changelog
- [Pipeline showcase](examples/showcase/) — real artifacts from a complete pipeline run
