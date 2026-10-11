#!/usr/bin/env python3
"""Optionally install the CNP guard hook in one Codex project.

The overlay instructions load automatically through the plugin's skills; this
script only adds (or removes) the hard CNP block as a project Codex hook.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def _hook_command() -> str:
    return f"python3 {ROOT / 'hooks/cnp_guard.py'}"


def _merge_hooks(raw: bytes, uninstall: bool) -> bytes:
    data = json.loads(raw.decode("utf-8")) if raw.strip() else {}
    if not isinstance(data, dict):
        raise ValueError(".codex/hooks.json must contain a JSON object")
    if uninstall and not isinstance(data.get("hooks"), dict):
        return raw
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError(".codex/hooks.json hooks must be a JSON object")
    command = _hook_command()
    wanted = {
        "UserPromptSubmit": {"hooks": [{"type": "command", "command": command}]},
        "PreToolUse": {
            "matcher": "Read",
            "hooks": [{"type": "command", "command": command}],
        },
    }
    for event, entry in wanted.items():
        entries = hooks.setdefault(event, [])
        if not isinstance(entries, list):
            raise ValueError(f".codex/hooks.json hooks.{event} must be an array")
        if uninstall:
            kept = []
            for existing in entries:
                if not isinstance(existing, dict):
                    kept.append(existing)
                    continue
                nested = existing.get("hooks")
                if not isinstance(nested, list):
                    kept.append(existing)
                    continue
                remaining = [h for h in nested if not (isinstance(h, dict) and h.get("command") == command)]
                if remaining:
                    clone = dict(existing)
                    clone["hooks"] = remaining
                    kept.append(clone)
                elif not any(isinstance(h, dict) and h.get("command") == command for h in nested):
                    kept.append(existing)
            hooks[event] = kept
            if not kept:
                hooks.pop(event, None)
        else:
            # Remove stale/duplicate copies of this command, then add canonical entries.
            stripped = []
            for existing in entries:
                if isinstance(existing, dict) and isinstance(existing.get("hooks"), list):
                    nested = [h for h in existing["hooks"] if not (isinstance(h, dict) and h.get("command") == command)]
                    if nested:
                        clone = dict(existing)
                        clone["hooks"] = nested
                        stripped.append(clone)
                else:
                    stripped.append(existing)
            hooks[event] = stripped + [entry]
    if uninstall and not hooks:
        data.pop("hooks", None)
    return (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def _safe_target(project: Path, candidate: Path) -> Path:
    target = candidate if candidate.is_absolute() else project / candidate
    target = target.resolve()
    if not target.is_relative_to(project.resolve()):
        raise ValueError(f"target must be inside project directory: {target}")
    return target


def _change(path: Path, transform, dry_run: bool) -> tuple[bool, bytes]:
    before = path.read_bytes() if path.exists() else b""
    after = transform(before)
    changed = after != before or not path.exists()
    if changed and not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(after)
    return changed, after


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--uninstall", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    project = args.project_dir.resolve()
    settings = _safe_target(project, Path(".codex/hooks.json"))
    if args.uninstall and not settings.exists():
        print("No changes")
        return 0
    changed, _ = _change(settings, lambda raw: _merge_hooks(raw, args.uninstall), args.dry_run)
    verb = "Would update" if args.dry_run else "Updated"
    print(f"{verb} {settings}" if changed else f"Unchanged {settings}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"install.py: {exc}", file=sys.stderr)
        raise SystemExit(2)
