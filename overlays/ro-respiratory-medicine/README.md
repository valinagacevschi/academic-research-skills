# Romanian respiratory-medicine layer

Adds Romanian respiratory-medicine context to every ARS tool: GOLD and ERS/ATS guidance, Romanian ethics and data-protection rules, reporting guidance, venue notes and pulmonary subdomain references. It is for research and manuscript work, not clinical decisions.

**It is on by default.** Each skill reads [`ACTIVATE.md`](ACTIVATE.md) from the installed plugin before its first reply. Nothing to install per project. See [How it works](../../docs/HOW_IT_WORKS.md).

## Optional: hard CNP block

The instructions already stop when a CNP is pasted. For a hard block that also covers file reads, add the Codex hook to a project (needs a clone of this repository):

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project            # add
python3 overlays/ro-respiratory-medicine/install.py /path/to/project --uninstall # remove
```

The hook goes into the project's `.codex/hooks.json`. Codex asks you to trust it once. It reports a masked value and asks for redaction; it cannot remove data already in a transcript.

## Verify

```sh
python3 overlays/ro-respiratory-medicine/check_overlay.py
python3 -m pytest overlays/ro-respiratory-medicine/tests -q
python3 overlays/ro-respiratory-medicine/plugin-evals/run_codex.py   # six doctor-scenario tests, uses Codex
```
