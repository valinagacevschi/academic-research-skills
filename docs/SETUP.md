# Setup

## 1 · Install the plugin (once per computer)

You need the **Codex** desktop app or CLI, signed in with your ChatGPT account.

```bash
git clone https://github.com/valinagacevschi/academic-research-skills.git ~/academic-research-skills
codex plugin marketplace add ~/academic-research-skills
codex plugin add academic-research-skills@ars
```

The five tools (`$deep-research`, `$sr-screener`, `$academic-paper`, `$academic-paper-reviewer`, `$academic-pipeline`) are now available in every Codex project.

**Update later:**

```bash
cd ~/academic-research-skills && git pull
codex plugin marketplace upgrade ars
```

## 2 · Turn on the Romanian respiratory layer (once per project)

```bash
python3 ~/academic-research-skills/overlays/ro-respiratory-medicine/install.py ~/path/to/my-study
```

This adds a short instruction block to the project's `AGENTS.md`, which Codex reads automatically. Remove it with `--uninstall`.

Then open `~/path/to/my-study` as a project in the Codex app, and start a new chat.

## 3 · Optional extras

| You want | Install |
|---|---|
| Word (DOCX) output | [Pandoc](https://pandoc.org/installing.html) |
| PDF output | Pandoc + [Tectonic](https://tectonic-typesetting.github.io/) |
| Script-backed checks (screening, PRISMA counts, reference resolvers) | Python 3.11+ |

Markdown output works without any of these.

## Optional: second-model verification

A different AI family re-checks references and claims independently. It is off unless you turn it on. Material is sent to the provider only after you agree in the chat.

```bash
export ARS_CROSS_MODEL="claude-sonnet-4-6"       # or: gemini-3.1-pro-preview
export ANTHROPIC_API_KEY="..."                    # or: GEMINI_API_KEY
```

Do not use it on unpublished manuscripts or patient material unless your institution allows sending them to that provider.

## What leaves your computer

| What | Where it goes | When |
|---|---|---|
| Your chat and files you share | OpenAI (Codex) | Always, as with any Codex use |
| Reference titles and DOIs | Crossref, OpenAlex, Semantic Scholar, arXiv | Reference checks |
| References and claims | Anthropic or Google | Only if second-model verification is on and you agree |

Patient identifiers should never be pasted. The respiratory layer stops if you do, see [How it works](HOW_IT_WORKS.md#what-the-romanian-respiratory-layer-adds).

## Trouble?

| Problem | Fix |
|---|---|
| `$deep-research` not recognised | Run `codex plugin list` and check `academic-research-skills` is installed, then restart Codex |
| Respiratory rules not applied | Check the project's `AGENTS.md` contains the overlay block; re-run `install.py` |
| No DOCX or PDF | Install Pandoc (and Tectonic for PDF) |
