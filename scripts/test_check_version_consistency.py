import json
from pathlib import Path

from scripts.check_version_consistency import check


def fixture(root: Path) -> None:
    (root / ".codex-plugin").mkdir()
    (root / "skills/demo").mkdir(parents=True)
    (root / "AGENTS.md").write_text(
        "- **Suite version**: 1.2.3\n| `demo` v1.0.0 | x | y |\n| `academic-pipeline` v1.2.3 | x | y |\n",
        encoding="utf-8",
    )
    (root / ".codex-plugin/plugin.json").write_text(json.dumps({"version": "1.2.3"}))
    (root / "skills/demo/SKILL.md").write_text(
        '---\nmetadata:\n  version: "1.0.0"\n---\n', encoding="utf-8"
    )


def test_versions_match(tmp_path: Path) -> None:
    fixture(tmp_path)
    assert check(tmp_path) == []


def test_plugin_drift_is_reported(tmp_path: Path) -> None:
    fixture(tmp_path)
    (tmp_path / ".codex-plugin/plugin.json").write_text('{"version":"9.9.9"}')
    assert any("plugin.json" in error for error in check(tmp_path))
