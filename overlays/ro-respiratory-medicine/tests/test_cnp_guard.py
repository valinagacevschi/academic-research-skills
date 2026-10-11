import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "hooks/cnp_guard.py"
sys.path.insert(0, str(ROOT / "hooks"))
import cnp_guard


WEIGHTS = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)


def make_cnp(series=1, year=90, month=1, day=2, county="01", serial="001"):
    first_twelve = f"{series}{year:02d}{month:02d}{day:02d}{county}{serial}"
    assert len(first_twelve) == 12
    checksum = sum(int(digit) * weight for digit, weight in zip(first_twelve, WEIGHTS)) % 11
    if checksum == 10:
        checksum = 1
    return first_twelve + str(checksum)


@pytest.mark.parametrize("series", [1, 2, 5, 6, 7, 9])
def test_valid_series(series):
    assert cnp_guard.find_cnps(make_cnp(series=series, year=4)) == [make_cnp(series=series, year=4)]


@pytest.mark.parametrize("value", [
    make_cnp()[:-1] + str((int(make_cnp()[-1]) + 1) % 10),
    make_cnp(month=13),
    make_cnp(month=2, day=30),
    make_cnp(county="53"),
])
def test_invalid_cnp_components(value):
    assert cnp_guard.find_cnps(value) == []


def test_14_digit_run_is_not_candidate():
    assert cnp_guard.find_cnps("0" + make_cnp() + "0") == []


def test_phone_like_run_with_bad_checksum_is_not_candidate():
    phone_like = make_cnp()[:-1] + str((int(make_cnp()[-1]) + 1) % 10)
    assert cnp_guard.find_cnps(f"Call {phone_like}") == []


def test_eponyms_and_plain_clinical_prose():
    assert cnp_guard.find_cnps("Wegener granulomatosis, FEV1 62%, patient improved after treatment.") == []


def run_hook(payload):
    return subprocess.run([sys.executable, str(SCRIPT)], input=payload, text=True, capture_output=True)


def test_detection_masks_cnp_in_process_output():
    value = make_cnp()
    result = run_hook(json.dumps({"hook_event_name": "UserPromptSubmit", "prompt": f"Patient CNP {value}"}))
    assert result.returncode == 2
    assert value not in result.stdout + result.stderr
    assert f"{value[0]}••••••••••••" in result.stderr
    assert "redact and re-send" in result.stderr
    assert "transcript and provider" in result.stderr
    assert "previously pasted" in result.stderr


def test_read_tool_path_scans_utf8_file(tmp_path):
    value = make_cnp()
    target = tmp_path / "clinical.txt"
    target.write_text(f"record {value}", encoding="utf-8")
    result = run_hook(json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Read", "tool_input": {"file_path": str(target)}}))
    assert result.returncode == 2
    assert value not in result.stdout + result.stderr
    assert "clinical.txt" in result.stderr
    assert str(target) not in result.stderr
    assert "1 valid CNP" in result.stderr
    assert f"{value[0]}••••••••••••" in result.stderr
    assert "was not read" in result.stderr
    assert "redact the file" in result.stderr
    assert "de-identified copy" in result.stderr
    assert "aggregate results" in result.stderr
    assert "previously pasted" not in result.stderr


def test_oversized_read_file_allows(tmp_path):
    target = tmp_path / "large.txt"
    with target.open("wb") as stream:
        stream.truncate(5 * 1024 * 1024 + 1)
    result = run_hook(json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Read", "tool_input": {"file_path": str(target)}}))
    assert result.returncode == 0
    assert result.stdout == result.stderr == ""


def test_binary_read_file_allows(tmp_path):
    target = tmp_path / "binary.bin"
    target.write_bytes(b"\x00" + make_cnp().encode())
    result = run_hook(json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Read", "tool_input": {"file_path": str(target)}}))
    assert result.returncode == 0
    assert result.stdout == result.stderr == ""


def test_malformed_stdin_fails_open_with_one_stderr_line():
    result = run_hook("{")
    assert result.returncode == 0
    assert result.stdout == ""
    assert len(result.stderr.splitlines()) == 1
