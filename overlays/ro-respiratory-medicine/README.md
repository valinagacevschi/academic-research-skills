# Romanian respiratory-medicine overlay

This Overlay adds Romanian respiratory-medicine context to ARS through a field profile, registry additions, and sourced Subdomain references. It leaves ARS core files unchanged and applies only after activation. See the [specification](docs/SPEC.md) and [glossary](docs/GLOSSARY.md).

## Local checks

Run the linter and tests with Python 3.12 and the project check dependencies:

```sh
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' --with pytest python overlays/ro-respiratory-medicine/check_overlay.py
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' --with pytest python -m pytest overlays/ro-respiratory-medicine/tests -q
```

## Use it in a project

Install the activation preamble in a project's `CLAUDE.md` (and in an existing `AGENTS.md`):

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project
```

To enable the optional Claude Code CNP guard, add `--with-cnp-hook`. Uninstall the overlay's instruction blocks and hook entries with `--uninstall`:

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project --with-cnp-hook
python3 overlays/ro-respiratory-medicine/install.py /path/to/project --uninstall
```

## Slice status

| Slice | Status |
|---|---|
| S1 — Skeleton and checks | Done |
| S2 — Evidence verification | Done |
| S3 — Field profile | Done |
| S4 — Human-subjects registry | Done |
| S5 — Review-criteria registry | Done |
| S6 — Subdomain references and methodology notes | Done |
| S7 — Venue notes and extras | Done |
| S8 — Patient-data guidance and CNP hook | Done |
| S9 — Activation preamble and installer | Done |
| S10 — Model-behaviour evals | Done (Codex run of record, 6/6) |
| S11 — Upstream asks | Done |
