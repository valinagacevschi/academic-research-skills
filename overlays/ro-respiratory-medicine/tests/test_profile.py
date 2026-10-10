import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

import check_overlay as check

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
sys.path.insert(0, str(REPO_ROOT))

from scripts.research_workflow_profile import (
    TASK_FAMILIES,
    canonical_bytes,
    load_profile,
    validate_profile,
    validate_selection_receipt,
)


def test_profile_validates_and_has_declared_stages_and_authorities():
    profile = load_profile(ROOT / "profile/respiratory_medicine.json")
    validate_profile(profile)
    assert set(profile["stage_map"]) == set(TASK_FAMILIES)
    assert all(value == {"state": "applicable"} for value in profile["stage_map"].values())
    assert {point["task_family"] for point in profile["authority_points"]} == {
        "methodology", "retrieval", "drafting", "review", "integrity_check"
    }


def test_build_is_idempotent(tmp_path):
    builder = ROOT / "profile/build_profile.py"
    subprocess.run([sys.executable, str(builder)], check=True)
    paths = [ROOT / "profile/respiratory_medicine.json", ROOT / "MANIFEST.json"]
    before = [path.read_bytes() for path in paths]
    subprocess.run([sys.executable, str(builder)], check=True)
    assert [path.read_bytes() for path in paths] == before


def test_selection_cli_receipt_is_accepted():
    receipt = subprocess.run(
        [
            sys.executable, str(REPO_ROOT / "scripts/research_workflow_profile.py"),
            "select", "--profile", str(ROOT / "profile/respiratory_medicine.json"),
            "--selected-by", "user_explicit", "--ars-suite-version", "3.23.0",
            "--selected-at", "2026-10-10T12:00:00Z",
        ],
        check=True, capture_output=True, text=True,
    )
    validate_selection_receipt(json.loads(receipt.stdout))


@pytest.mark.parametrize("mutation", ["manifest", "profile"])
def test_check_overlay_fails_on_digest_mismatch_or_tampered_bytes(tmp_path, mutation):
    overlay = tmp_path / "ro-respiratory-medicine"
    shutil.copytree(ROOT, overlay)
    profile_path = overlay / "profile/respiratory_medicine.json"
    manifest_path = overlay / "MANIFEST.json"
    if mutation == "manifest":
        manifest = json.loads(manifest_path.read_text())
        manifest["profile_content_sha256"] = "0" * 64
        manifest_path.write_bytes(canonical_bytes(manifest) + b"\n")
    else:
        profile_path.write_bytes(profile_path.read_bytes() + b" ")
    errors = check.check_profile(overlay, REPO_ROOT)
    assert errors


