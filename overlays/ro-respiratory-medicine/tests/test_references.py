from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from check_overlay import effective_use, load_rows  # noqa: E402
from tools.render_references import render  # noqa: E402


def test_renderer_is_deterministic_and_check_passes() -> None:
    first = render(date(2026, 10, 10))
    second = render(date(2026, 10, 10))
    assert first == second
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/render_references.py"), "--check"],
        cwd=ROOT.parents[2], capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_handwritten_value_ids_exist() -> None:
    rows, errors = load_rows(ROOT)
    assert errors == []
    valid = {row["value_id"] for row in rows}
    for name in ("design_addons.md", "reviewer_prompts.md"):
        content = (ROOT / "references" / name).read_text(encoding="utf-8")
        citations = set(re.findall(r"`([a-z][a-z0-9_.-]+)`", content))
        assert citations <= valid, f"{name}: unknown ids {sorted(citations - valid)}"


def test_nonlegal_rows_appear_in_exactly_one_rendered_file() -> None:
    rows, _ = load_rows(ROOT)
    files = render(date(2026, 10, 10))
    for row in rows:
        if row["value_id"].startswith("ro."):
            continue
        occurrences = sum(content.count(f"`{row['value_id']}`") for content in files.values())
        assert occurrences == 1, (row["value_id"], occurrences)


def test_advisory_and_stale_rows_show_verify_caveat() -> None:
    rows, _ = load_rows(ROOT)
    advisory = next(row for row in rows if effective_use(row, date(2026, 10, 10)) == "advisory")
    rendered = "\n".join(render(date(2026, 10, 10)).values())
    assert f"`{advisory['value_id']}`" in rendered and "**Verify:** advisory" in rendered
    stale = next(row for row in rows if row["use"] != "advisory")
    assert effective_use(stale, date(2030, 1, 1)) == "advisory"
    files = render(date(2030, 1, 1))
    assert any(f"`{stale['value_id']}`" in text and "**Verify:** advisory" in text for text in files.values())


def test_handwritten_numeric_text_is_cited_or_a_year_or_section() -> None:
    for name in ("design_addons.md", "reviewer_prompts.md", "edition_watch.md"):
        for line in (ROOT / "references" / name).read_text(encoding="utf-8").splitlines():
            if re.search(r"\d", line):
                assert "`" in line or re.search(r"(?:§\s*\d|\b(?:19|20)\d{2}\b)", line), (name, line)

