#!/usr/bin/env python3
"""Keep suite and skill version metadata aligned without release notes."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

VERSION = re.compile(r"^\d+\.\d+\.\d+(?:\.\d+)?$")


def check(root: Path) -> list[str]:
    errors: list[str] = []
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    match = re.search(r"^\s*- \*\*Suite version\*\*: ([^\s]+)", agents, re.M)
    if not match or not VERSION.fullmatch(match.group(1)):
        return ["AGENTS.md: missing or invalid suite version"]
    suite = match.group(1)
    plugin = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("version") != suite:
        errors.append(f".codex-plugin/plugin.json: version {plugin.get('version')!r} != {suite}")
    package_path = root / "package.json"
    if package_path.exists():
        package = json.loads(package_path.read_text(encoding="utf-8"))
        if package.get("version") and package["version"] != suite:
            errors.append(f"package.json: version {package['version']!r} != {suite}")
    listed = dict(re.findall(r"^\| `([^`]+)` v([^ |]+) \|", agents, re.M))
    if listed.get("academic-pipeline") != suite:
        errors.append("AGENTS.md: academic-pipeline version must equal suite version")
    for skill_md in sorted((root / "skills").glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        fm = re.search(r"^metadata:\s*\n(?:(?!\S).)*?^\s+version:\s*['\"]?([^'\"\s]+)", text, re.M)
        if not fm:
            errors.append(f"{skill_md.relative_to(root)}: missing metadata.version")
            continue
        version = fm.group(1)
        if not VERSION.fullmatch(version):
            errors.append(f"{skill_md.relative_to(root)}: invalid version {version!r}")
        elif skill_md.parent.name in listed and listed[skill_md.parent.name] != version:
            errors.append(f"AGENTS.md: {skill_md.parent.name} version {listed[skill_md.parent.name]} != SKILL.md {version}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    errors = check(args.path)
    if errors:
        print("Version consistency check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Version consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
