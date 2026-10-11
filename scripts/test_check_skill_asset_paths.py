from __future__ import annotations

import shutil
from pathlib import Path

from check_skill_asset_paths import check


def _root(tmp_path: Path) -> Path:
    (tmp_path / "shared").mkdir()
    (tmp_path / "scripts").mkdir()
    (tmp_path / "shared" / "ok.md").write_text("ok")
    (tmp_path / "scripts" / "root.py").write_text("pass")
    for name in ("deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline", "sr-screener"):
        (tmp_path / name / "scripts").mkdir(parents=True)
        (tmp_path / name / "scripts" / "local.py").write_text("pass")
        (tmp_path / name / "SKILL.md").write_text("`shared/ok.md` `scripts/root.py` `scripts/local.py`")
    return tmp_path


def test_checkout_paths_resolve(tmp_path: Path) -> None:
    assert check(_root(tmp_path)) == []


def test_missing_shared_asset_fails(tmp_path: Path) -> None:
    root = _root(tmp_path)
    (root / "shared" / "ok.md").unlink()
    errors = check(root)
    assert len(errors) == 5
    assert all("shared/ok.md" in error for error in errors)


def test_installed_plugin_copy_paths_resolve(tmp_path: Path) -> None:
    source = _root(tmp_path)
    plugin = tmp_path / "plugin"
    plugin.mkdir()
    shutil.copytree(source / "shared", plugin / "shared")
    shutil.copytree(source / "scripts", plugin / "scripts")
    (plugin / "skills").mkdir()
    for name in ("deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline", "sr-screener"):
        shutil.copytree(source / name, plugin / "skills" / name)
    assert check(plugin) == []
