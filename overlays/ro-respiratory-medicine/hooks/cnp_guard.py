#!/usr/bin/env python3
"""Optional Codex guard for Romanian personal numeric codes (CNPs)."""

from __future__ import annotations

import json
import re
import sys
from calendar import monthrange
from pathlib import Path
from typing import Any

MAX_FILE_BYTES = 5 * 1024 * 1024
WEIGHTS = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
COUNTY_CODES = {f"{number:02d}" for number in range(1, 53)} | {"70"}
# The official portal's county-code table lists codes 01-42, but does not
# establish the full CNP range. Retain 01-52 and 70 per the slice specification.
# Source: https://legislatie.just.ro/Public/DetaliiDocument/254121 (accessed 2026-10-10).
CNPS = re.compile(r"(?<![0-9])[0-9]{13}(?![0-9])")


def _valid_cnp(value: str) -> bool:
    digits = [int(char) for char in value]
    series, month, day, county = digits[0], int(value[3:5]), int(value[5:7]), value[7:9]
    if series not in range(1, 10) or month not in range(1, 13) or county not in COUNTY_CODES:
        return False

    years = {
        1: (1900,), 2: (1900,), 3: (1800,), 4: (1800,),
        5: (2000,), 6: (2000,), 7: (1900, 2000), 8: (1900, 2000), 9: (1900, 2000),
    }[series]
    if not any(1 <= day <= monthrange(century + int(value[1:3]), month)[1] for century in years):
        return False

    checksum = sum(digit * weight for digit, weight in zip(digits[:12], WEIGHTS)) % 11
    if checksum == 10:
        checksum = 1
    return checksum == digits[12]


def find_cnps(text: str) -> list[str]:
    """Return valid CNP candidates in text, in order of appearance."""
    return [match.group() for match in CNPS.finditer(text) if _valid_cnp(match.group())]


def _read_file(file_path: Any) -> str | None:
    if not isinstance(file_path, str):
        return None
    try:
        path = Path(file_path)
        if path.stat().st_size > MAX_FILE_BYTES:
            return None
        data = path.read_bytes()
    except (OSError, ValueError):
        return None
    if len(data) > MAX_FILE_BYTES or b"\0" in data:
        return None
    return data.decode("utf-8", errors="ignore")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError):
        print("CNP guard: malformed hook JSON; allowing this event.", file=sys.stderr)
        return 0
    if not isinstance(payload, dict):
        print("CNP guard: malformed hook JSON; allowing this event.", file=sys.stderr)
        return 0

    event = payload.get("hook_event_name")
    read_path = None
    if event == "UserPromptSubmit":
        content = payload.get("prompt", "")
    elif event == "PreToolUse" and isinstance(payload.get("tool_input"), dict) and payload.get("tool_name") == "Read":
        read_path = payload["tool_input"].get("file_path")
        content = _read_file(read_path)
    else:
        return 0
    if not isinstance(content, str):
        return 0

    found = find_cnps(content)
    if not found:
        return 0
    first = found[0][0]
    count = len(found)
    plural = "s" if count != 1 else ""
    if event == "PreToolUse":
        basename = Path(read_path).name
        message = (
            f"File {basename} contains {count} valid CNP{plural} ({first}••••••••••••). "
            "It was not read. Please redact the file or use a de-identified copy (or aggregate results) instead."
        )
    else:
        message = (
            f"CNP guard found {count} valid CNP{plural} ({first}••••••••••••). "
            "Please redact and re-send. The session transcript and provider may already hold anything previously pasted."
        )
    print(message, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
