from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "install.py"
BEGIN = "<!-- ro-respiratory-overlay:begin v0.1.0 -->"
END = "<!-- ro-respiratory-overlay:end -->"


def run(project: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), str(project), *args],
        capture_output=True,
        text=True,
        check=True,
    )


def test_fresh_install_contains_block_and_absolute_paths(tmp_path: Path) -> None:
    project = tmp_path / "project"
    run(project)
    content = (project / "CLAUDE.md").read_text()
    assert BEGIN in content and END in content
    assert str(ROOT) in content
    assert "{OVERLAY_ROOT}" not in content


def test_preserves_existing_bytes_and_rerun_is_identical(tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()
    original = b"# Existing\r\n\r\nkeep these bytes\xff\n"
    (project / "CLAUDE.md").write_bytes(original)
    run(project)
    first = (project / "CLAUDE.md").read_bytes()
    assert first.startswith(original + b"\n")
    run(project)
    assert (project / "CLAUDE.md").read_bytes() == first


def test_agents_only_updated_when_it_exists(tmp_path: Path) -> None:
    project = tmp_path / "project"
    run(project)
    assert not (project / "AGENTS.md").exists()
    agents = project / "AGENTS.md"
    agents.write_bytes(b"other runtime\n")
    run(project)
    assert BEGIN in agents.read_text()


def test_hook_is_not_installed_by_default(tmp_path: Path) -> None:
    project = tmp_path / "project"
    run(project)
    assert not (project / ".claude/settings.json").exists()


def test_opt_in_merges_hooks_without_duplicates(tmp_path: Path) -> None:
    project = tmp_path / "project"
    settings = project / ".claude/settings.json"
    settings.parent.mkdir(parents=True)
    original = {
        "other": True,
        "hooks": {
            "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "echo keep"}]}],
            "PreToolUse": [{"matcher": "Write", "hooks": [{"type": "command", "command": "echo write"}]}],
        },
    }
    settings.write_text(json.dumps(original))
    run(project, "--with-cnp-hook")
    first = json.loads(settings.read_text())
    run(project, "--with-cnp-hook")
    second = json.loads(settings.read_text())
    assert second == first
    assert second["other"] is True
    assert "echo keep" in json.dumps(second)
    assert "echo write" in json.dumps(second)
    assert sum("cnp_guard.py" in json.dumps(e) for e in second["hooks"]["UserPromptSubmit"]) == 1
    assert sum("cnp_guard.py" in json.dumps(e) for e in second["hooks"]["PreToolUse"]) == 1


@pytest.mark.parametrize("original", [b"", b"# Original\n", b"# Original without newline"])
def test_uninstall_restores_original_bytes(tmp_path: Path, original: bytes) -> None:
    project = tmp_path / "project"
    project.mkdir()
    target = project / "CLAUDE.md"
    if original:
        target.write_bytes(original)
    run(project, "--with-cnp-hook")
    run(project, "--uninstall")
    assert target.read_bytes() == original
    assert json.loads((project / ".claude/settings.json").read_text()) == {}


def test_uninstall_preserves_other_hooks(tmp_path: Path) -> None:
    project = tmp_path / "project"
    settings = project / ".claude/settings.json"
    settings.parent.mkdir(parents=True)
    settings.write_text(json.dumps({"hooks": {"UserPromptSubmit": [{"hooks": [{"type": "command", "command": "echo keep"}]}]}}))
    run(project, "--with-cnp-hook")
    run(project, "--uninstall")
    data = json.loads(settings.read_text())
    assert "echo keep" in json.dumps(data)
    assert "cnp_guard.py" not in json.dumps(data)


def test_dry_run_writes_nothing(tmp_path: Path) -> None:
    project = tmp_path / "project"
    result = run(project, "--with-cnp-hook", "--dry-run")
    assert "Would update" in result.stdout
    assert not project.exists()


def test_patient_data_is_included_verbatim() -> None:
    activation = (ROOT / "ACTIVATE.md").read_text()
    patient = (ROOT / "activation/patient_data.md").read_text().rstrip("\n")
    assert patient in activation


def test_preamble_paths_exist_except_parallel_review_registry() -> None:
    activation = (ROOT / "ACTIVATE.md").read_text()
    paths = re.findall(r"\{OVERLAY_ROOT\}/([A-Za-z0-9_./-]+)", activation)
    assert "registries/generated/review_criteria_registry.json" in paths
    missing = [path for path in paths if path != "registries/generated/review_criteria_registry.json" and not (ROOT / path).exists()]
    assert not missing


def test_preamble_avoids_prohibited_terms() -> None:
    activation = (ROOT / "ACTIVATE.md").read_text().lower()
    assert "locale pack" not in activation
    assert " pack " not in activation


def test_custom_claude_path_cannot_escape_project(tmp_path: Path) -> None:
    project = tmp_path / "project"
    outside = tmp_path / "outside.md"
    result = subprocess.run(
        [sys.executable, str(INSTALLER), str(project), "--claude-md", str(outside)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert not outside.exists()
