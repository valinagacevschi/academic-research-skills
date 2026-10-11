#!/usr/bin/env python3
"""Check shared/ and scripts/ paths cited in skill instructions resolve in ARS."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILL_NAMES = ("deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline", "sr-screener")
ASSET_RE = re.compile(r"(?<![\w./-])(shared|scripts)/[A-Za-z0-9_.*<>/-]+")


def _ars_root(skill_dir: Path) -> Path | None:
    for candidate in (skill_dir, *skill_dir.parents):
        if (candidate / "shared").is_dir() and (candidate / "scripts").is_dir():
            return candidate
    return None


def _exists(path: Path) -> bool:
    if "*" in str(path):
        return any(path.parent.glob(path.name))
    return path.exists()


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for name in SKILL_NAMES:
        candidates = (root / name / "SKILL.md", root / "skills" / name / "SKILL.md")
        skill_file = next((path for path in candidates if path.is_file()), candidates[0])
        if not skill_file.is_file():
            errors.append(f"{skill_file}: missing")
            continue
        skill_dir = skill_file.parent.resolve()
        ars_root = _ars_root(skill_dir)
        if ars_root is None:
            errors.append(f"{skill_file}: cannot find ARS root (ancestor with shared/ and scripts/)")
            continue
        text = skill_file.read_text(encoding="utf-8")
        for code in re.findall(r"`([^`]+)`", text):
            for match in ASSET_RE.finditer(code):
                cited = match.group(0).rstrip(".,:;")
                if cited.startswith("shared/"):
                    candidates = [ars_root / cited]
                else:
                    candidates = [ars_root / cited, skill_dir / cited]
                if not any(_exists(path) for path in candidates):
                    errors.append(f"{skill_file}: cited path {cited!r} does not exist under ARS root or skill directory")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check(args.repo_root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("check_skill_asset_paths: all cited shared/ and scripts/ paths resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
