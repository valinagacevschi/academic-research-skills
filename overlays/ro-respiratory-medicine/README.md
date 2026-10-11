# Respiratory medicine for Codex

Adds Romanian respiratory-medicine context to ARS: GOLD and ERS/ATS guidance, Romanian ethics and data rules, reporting guidance, and pulmonary subdomain references. It is for research and manuscript work, not clinical decisions.

Read the [ARS workflow overview](../../docs/HOW_IT_WORKS.md).

## Install in a project

From the ARS repository, run:

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project
```

This adds the overlay instructions to that project's `AGENTS.md`. To also stop submitted prompts and file reads containing a checksum-valid Romanian personal numeric code (CNP), install the optional Codex hook:

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project --with-cnp-hook
```

The hook is added to `.codex/hooks.json`. It reports a masked value and asks for redaction. It does not remove data already present in a transcript.

Remove the overlay instructions and its hook entries with:

```sh
python3 overlays/ro-respiratory-medicine/install.py /path/to/project --uninstall
```

## Verify

```sh
python3 overlays/ro-respiratory-medicine/check_overlay.py
python3 -m pytest overlays/ro-respiratory-medicine/tests -q
```
