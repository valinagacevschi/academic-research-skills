# Romanian respiratory-medicine overlay

This Overlay adds Romanian respiratory-medicine context to ARS through a field profile, registry additions, and sourced Subdomain references. It leaves ARS core files unchanged and applies only after activation. See the [specification](docs/SPEC.md) and [glossary](docs/GLOSSARY.md).

## Local checks

Run the linter and tests with Python 3.12 and the project check dependencies:

```sh
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' --with pytest python overlays/ro-respiratory-medicine/check_overlay.py
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' --with pytest python -m pytest overlays/ro-respiratory-medicine/tests -q
```

## Slice status

| Slice | Status |
|---|---|
| S1 — Skeleton and checks | Done |
| S2 — Evidence verification | Pending |
| S3 — Field profile | Pending |
| S4 — Human-subjects registry | Pending |
| S5 — Review-criteria registry | Pending |
| S6 — Subdomain references and methodology notes | Pending |
| S7 — Venue notes and extras | Pending |
| S8 — Patient-data guidance and CNP hook | Pending |
| S9 — Activation preamble and installer | Pending |
| S10 — Model-behaviour evals | Pending |
| S11 — Upstream asks | Pending |
