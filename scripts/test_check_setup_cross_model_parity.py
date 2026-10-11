"""Unit tests for non-GPT verifier setup parity."""
import unittest
from pathlib import Path

from tests.test_helpers import load_module_from_path, run_script

SCRIPT = Path(__file__).resolve().parent / "check_setup_cross_model_parity.py"
EN_OK = 'export ARS_CROSS_MODEL="claude-sonnet-4-6"\n# or: export ARS_CROSS_MODEL="gemini-3.1-pro-preview"\n'
ZH_OK = EN_OK
CANONICAL_OK = (
    "| Provider | API ID | Status |\n|---|---|---|\n"
    "| Anthropic | `claude-sonnet-4-6` | Provisional |\n"
    "| Google | `gemini-3.1-pro-preview` | Provisional |\n"
)


def _load_module():
    return load_module_from_path("check_setup_cross_model_parity", SCRIPT)


class SetupCrossModelParityTests(unittest.TestCase):
    def test_repo_baseline_passes(self):
        result = run_script(SCRIPT)
        self.assertEqual(result.returncode, 0, msg=f"stderr: {result.stderr}")

    def test_clean_fixture_passes(self):
        self.assertEqual(_load_module().check(EN_OK, ZH_OK, CANONICAL_OK), [])

    def test_en_zh_drift_fails(self):
        errors = _load_module().check(EN_OK, 'export ARS_CROSS_MODEL="gemini-3.1-pro-preview"\n', CANONICAL_OK)
        self.assertTrue(any("drift" in e for e in errors))

    def test_unknown_provider_id_fails(self):
        bad = 'export ARS_CROSS_MODEL="gpt-6-astra"\n'
        errors = _load_module().check(bad, bad, CANONICAL_OK)
        self.assertTrue(any("gpt-6-astra" in e and "not in" in e for e in errors))

    def test_missing_model_table_fails_closed(self):
        errors = _load_module().check(EN_OK, ZH_OK, "prose only")
        self.assertTrue(any("parser went stale" in e for e in errors))

    def test_zero_examples_fails_closed(self):
        errors = _load_module().check("no examples", ZH_OK, CANONICAL_OK)
        self.assertTrue(any("Fail-closed" in e for e in errors))

    def test_commented_examples_are_extracted(self):
        self.assertEqual(
            _load_module().extract_ids(EN_OK),
            ["claude-sonnet-4-6", "gemini-3.1-pro-preview"],
        )


if __name__ == "__main__":
    unittest.main()
