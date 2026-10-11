from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "install.py"
BEGIN = "<!-- ro-respiratory-overlay:begin v0.1.0 -->"
END = "<!-- ro-respiratory-overlay:end -->"

def run(project: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(INSTALLER), str(project), *args], capture_output=True, text=True, check=True)

def test_fresh_install_creates_agents_only(tmp_path: Path) -> None:
    project=tmp_path / "project"; run(project)
    content=(project / "AGENTS.md").read_text()
    assert BEGIN in content and END in content and str(ROOT) in content

def test_existing_agents_bytes_are_preserved_and_rerun_is_stable(tmp_path: Path) -> None:
    project=tmp_path / "project"; project.mkdir(); agents=project / "AGENTS.md"
    original=b"# Existing\r\nkeep bytes\xff\n"; agents.write_bytes(original)
    run(project); first=agents.read_bytes(); assert first.startswith(original+b"\n")
    run(project); assert agents.read_bytes()==first

def test_cnp_hook_opt_in_merges_and_is_idempotent(tmp_path: Path) -> None:
    project=tmp_path / "project"; config=project / ".codex/hooks.json"
    config.parent.mkdir(parents=True); config.write_text(json.dumps({"other":True,"hooks":{"Stop":[{"hooks":[{"type":"command","command":"echo keep"}]}]}}))
    run(project,"--with-cnp-hook"); first=json.loads(config.read_text())
    run(project,"--with-cnp-hook"); second=json.loads(config.read_text())
    assert second==first and second["other"] is True
    assert "echo keep" in json.dumps(second)
    assert "UserPromptSubmit" in second["hooks"] and "PreToolUse" in second["hooks"]
    assert "cnp_guard.py" in json.dumps(second)

def test_uninstall_removes_only_overlay_and_hook_entries(tmp_path: Path) -> None:
    project=tmp_path / "project"; run(project,"--with-cnp-hook")
    run(project,"--uninstall")
    assert not (project / "AGENTS.md").exists()
    assert json.loads((project / ".codex/hooks.json").read_text()) == {}

def test_uninstall_preserves_other_hooks(tmp_path: Path) -> None:
    project=tmp_path / "project"; run(project,"--with-cnp-hook")
    config=project / ".codex/hooks.json"; data=json.loads(config.read_text())
    data["hooks"]["Stop"]=[{"hooks":[{"type":"command","command":"echo keep"}]}]
    config.write_text(json.dumps(data)); run(project,"--uninstall")
    assert "echo keep" in config.read_text() and "cnp_guard.py" not in config.read_text()
