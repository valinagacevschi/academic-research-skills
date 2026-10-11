#!/usr/bin/env python3
"""Install the Romanian respiratory-medicine overlay preamble in one project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))["overlay_version"]
BEGIN = f"<!-- ro-respiratory-overlay:begin v{VERSION} -->"
END = "<!-- ro-respiratory-overlay:end -->"
BLOCK_RE = re.compile(
    rb"<!-- ro-respiratory-overlay:begin v[^\r\n]+ -->.*?<!-- ro-respiratory-overlay:end -->",
    re.DOTALL,
)


def _block() -> bytes:
    body = (ROOT / "ACTIVATE.md").read_text(encoding="utf-8").replace(
        "{OVERLAY_ROOT}", str(ROOT)
    ).replace("\r\n", "\n").strip("\n")
    return f"{BEGIN}\n{body}\n{END}".encode("utf-8")


def _with_block(original: bytes, block: bytes) -> bytes:
    found = BLOCK_RE.search(original)
    if found:
        return original[: found.start()] + block + original[found.end() :]
    if not original:
        return block + b"\n"
    # One separator newline belongs to the managed block and is removed on uninstall.
    return original + b"\n" + block + b"\n"


def _without_block(original: bytes) -> bytes:
    found = BLOCK_RE.search(original)
    if not found:
        return original
    start, end = found.span()
    if start and original[start - 1 : start] == b"\n":
        start -= 1
    if end < len(original) and original[end : end + 1] == b"\n":
        end += 1
    return original[:start] + original[end:]


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
    parser.add_argument("--with-cnp-hook", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    project = args.project_dir.resolve()
    transform = _without_block if args.uninstall else lambda raw: _with_block(raw, _block())
    actions: list[str] = []
    for path in (_safe_target(project, Path("AGENTS.md")),):
        if args.uninstall and not path.exists():
            continue
        changed, _ = _change(path, transform, args.dry_run)
        if changed:
            actions.append(f"{'Would update' if args.dry_run else 'Updated'} {path}")
        else:
            actions.append(f"Unchanged {path}")

    if args.with_cnp_hook or args.uninstall:
        settings = _safe_target(project, Path(".codex/hooks.json"))
        if settings.exists() or args.with_cnp_hook:
            changed, _ = _change(settings, lambda raw: _merge_hooks(raw, args.uninstall), args.dry_run)
            if changed:
                actions.append(f"{'Would update' if args.dry_run else 'Updated'} {settings}")
            else:
                actions.append(f"Unchanged {settings}")
    if not actions:
        actions.append("No changes")
    print("\n".join(actions))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"install.py: {exc}", file=sys.stderr)
        raise SystemExit(2)
