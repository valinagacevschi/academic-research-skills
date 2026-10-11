from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "install.py"


def run(project: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(INSTALLER), str(project), *args], capture_output=True, text=True, check=True)


def test_install_adds_only_the_hook(tmp_path: Path) -> None:
    project = tmp_path / "project"
    run(project)
    assert not (project / "AGENTS.md").exists()
    data = json.loads((project / ".codex/hooks.json").read_text())
    assert "UserPromptSubmit" in data["hooks"] and "PreToolUse" in data["hooks"]
    assert "cnp_guard.py" in json.dumps(data)


def test_hook_merge_is_idempotent_and_keeps_other_config(tmp_path: Path) -> None:
    project = tmp_path / "project"; config = project / ".codex/hooks.json"
    config.parent.mkdir(parents=True)
    config.write_text(json.dumps({"other": True, "hooks": {"Stop": [{"hooks": [{"type": "command", "command": "echo keep"}]}]}}))
    run(project); first = json.loads(config.read_text())
    run(project); second = json.loads(config.read_text())
    assert second == first and second["other"] is True
    assert "echo keep" in json.dumps(second)


def test_uninstall_removes_only_the_hook(tmp_path: Path) -> None:
    project = tmp_path / "project"; run(project)
    config = project / ".codex/hooks.json"; data = json.loads(config.read_text())
    data["hooks"]["Stop"] = [{"hooks": [{"type": "command", "command": "echo keep"}]}]
    config.write_text(json.dumps(data)); run(project, "--uninstall")
    text = config.read_text()
    assert "echo keep" in text and "cnp_guard.py" not in text


def test_uninstall_without_config_is_a_no_op(tmp_path: Path) -> None:
    project = tmp_path / "project"; project.mkdir()
    assert "No changes" in run(project, "--uninstall").stdout
