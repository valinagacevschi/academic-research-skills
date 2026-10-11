from pathlib import Path
from tempfile import TemporaryDirectory
from scripts import check_spec_consistency as csc


def test_rendered_relative_link_check_reports_missing_target() -> None:
    old_root = csc.ROOT
    try:
        with TemporaryDirectory() as directory:
            csc.ROOT = Path(directory)
            (csc.ROOT / "docs").mkdir()
            (csc.ROOT / "docs/PAGE.md").write_text("[broken](MISSING.md)\n", encoding="utf-8")
            csc.ERRORS.clear()
            csc.check_relative_markdown_links("docs/PAGE.md")
            assert any("MISSING.md" in error for error in csc.ERRORS)
    finally:
        csc.ROOT = old_root
        csc.ERRORS.clear()


def test_rendered_relative_link_check_ignores_code_and_comments() -> None:
    old_root = csc.ROOT
    try:
        with TemporaryDirectory() as directory:
            csc.ROOT = Path(directory)
            (csc.ROOT / "docs").mkdir()
            (csc.ROOT / "docs/PAGE.md").write_text(
                "`[code](MISSING.md)`\n<!-- [comment](MISSING.md) -->\n```md\n[code](MISSING.md)\n```\n",
                encoding="utf-8",
            )
            csc.ERRORS.clear()
            csc.check_relative_markdown_links("docs/PAGE.md")
            assert csc.ERRORS == []
    finally:
        csc.ROOT = old_root
        csc.ERRORS.clear()
