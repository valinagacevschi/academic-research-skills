"""Mocked HTTP contract tests; no provider network calls."""
import json
import unittest
from unittest.mock import Mock
from urllib.error import HTTPError

from cross_model_request import (
    TIMEOUT_SECONDS, VerificationResult, anthropic_request, dispatch_handoff,
    gemini_request, verify_reference,
)

REFERENCE = {"reference": "Doe, J. (2024). Example. Journal. doi:10.1234/example", "context": "claim"}
ANTHROPIC_ENV = {"ARS_CROSS_MODEL": "claude-test", "ANTHROPIC_API_KEY": "synthetic"}
GEMINI_ENV = {"ARS_CROSS_MODEL": "gemini-test", "GEMINI_API_KEY": "synthetic"}


class Response:
    def __init__(self, body): self.body = json.dumps(body).encode()
    def __enter__(self): return self
    def __exit__(self, *_): return False
    def read(self, size): return self.body


def anthropic_body(verdict="VERIFIED", *, refusal=False, search=True, source=True):
    content = []
    if search:
        content += [
            {"type": "server_tool_use", "name": "web_search", "id": "s"},
            {"type": "web_search_tool_result", "tool_use_id": "s", "content": (
                [{"type": "web_search_result", "url": "https://example.org/paper"}] if source else [])},
        ]
    content.append({"type": "text", "text": json.dumps({"verdict": verdict, "detail": "matched", "source_urls": []})})
    return {"stop_reason": "refusal" if refusal else "end_turn", "content": content}


def gemini_body(verdict="VERIFIED", *, blocked=False, grounded=True, source=True):
    candidate = {"content": {"parts": [{"text": json.dumps({"verdict": verdict, "detail": "matched", "source_urls": []})}]}}
    if grounded:
        candidate["groundingMetadata"] = {
            "webSearchQueries": ["reference"],
            "groundingChunks": ([{"web": {"uri": "https://example.org/paper"}}] if source else []),
        }
    return {"promptFeedback": {"blockReason": "SAFETY"} if blocked else {}, "candidates": [candidate]}


class CrossModelRuntimeTests(unittest.TestCase):
    def run_body(self, env, body):
        opener = Mock(return_value=Response(body))
        result = verify_reference(REFERENCE, environ=env, opener=opener, sleeper=Mock())
        opener.assert_called_once()
        self.assertEqual(opener.call_args.kwargs["timeout"], TIMEOUT_SECONDS)
        return result

    def test_provider_builders_enable_grounded_search(self):
        self.assertEqual(json.loads(anthropic_request("claude-x", "k", "p").body)["tools"][0]["type"], "web_search_20250305")
        self.assertEqual(json.loads(gemini_request("gemini-x", "k", "p").body)["tools"], [{"google_search": {}}])

    def test_success_for_both_providers_records_actual_provider_and_model(self):
        a = self.run_body(ANTHROPIC_ENV, anthropic_body())
        g = self.run_body(GEMINI_ENV, gemini_body())
        for result, provider, model in ((a, "anthropic", "claude-test"), (g, "gemini", "gemini-test")):
            self.assertEqual((result.status, result.verdict), ("complete", "VERIFIED"))
            self.assertEqual((result.provider, result.model), (provider, model))
            self.assertEqual(result.sources, ("https://example.org/paper",))
            self.assertEqual(result.audit_record()["provider"], provider)

    def test_verdicts_are_closed_and_verified_requires_source(self):
        result = self.run_body(ANTHROPIC_ENV, anthropic_body("VERIFIED", source=False))
        self.assertEqual(result.verdict, "NOT_SEARCHED")
        malformed = self.run_body(GEMINI_ENV, gemini_body("invented"))
        self.assertEqual((malformed.status, malformed.verdict), ("unavailable", None))

    def test_refusal_and_safety_blocks_are_not_verdicts(self):
        a = self.run_body(ANTHROPIC_ENV, anthropic_body(refusal=True))
        g = self.run_body(GEMINI_ENV, gemini_body(blocked=True))
        self.assertEqual((a.status, a.verdict, a.detail), ("unavailable", None, "safety_refusal"))
        self.assertEqual((g.status, g.verdict, g.detail), ("unavailable", None, "safety_block"))

    def test_timeout_retries_then_returns_unavailable(self):
        opener = Mock(side_effect=TimeoutError())
        sleep = Mock()
        result = verify_reference(REFERENCE, environ=GEMINI_ENV, opener=opener, sleeper=sleep)
        self.assertEqual((result.status, result.verdict, result.detail), ("unavailable", None, "transport_failure"))
        self.assertEqual(opener.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_http_4xx_does_not_retry_and_5xx_is_bounded(self):
        bad_request = HTTPError("url", 400, "bad request", {}, None)
        opener = Mock(side_effect=bad_request)
        result = verify_reference(REFERENCE, environ=ANTHROPIC_ENV, opener=opener, sleeper=Mock())
        self.assertEqual((result.status, result.verdict, result.detail), ("unavailable", None, "http_400"))
        self.assertEqual(opener.call_count, 1)
        server_error = HTTPError("url", 503, "unavailable", {}, None)
        opener = Mock(side_effect=server_error)
        result = verify_reference(REFERENCE, environ=GEMINI_ENV, opener=opener, sleeper=Mock())
        self.assertEqual((result.status, result.verdict, result.detail), ("unavailable", None, "http_503"))
        self.assertEqual(opener.call_count, 3)

    def test_malformed_json_and_missing_grounding_fail_safely(self):
        malformed = self.run_body(ANTHROPIC_ENV, {"content": "bad"})
        ungrounded = self.run_body(GEMINI_ENV, gemini_body(grounded=False))
        self.assertEqual((malformed.status, malformed.verdict), ("unavailable", None))
        self.assertEqual((ungrounded.status, ungrounded.verdict, ungrounded.detail),
                         ("unavailable", None, "search_not_invoked"))

    def test_unset_is_off_and_unknown_models_are_unavailable(self):
        self.assertEqual(verify_reference(REFERENCE, environ={}).status, "not_configured")
        result = verify_reference(REFERENCE, environ={"ARS_CROSS_MODEL": "gpt-test"})
        self.assertEqual((result.status, result.verdict), ("unavailable", None))

    def test_handoff_dispatch_blinds_owner_decision_and_uses_existing_router(self):
        envelope = "\n".join([
            "[CROSS-MODEL-HANDOFF v1]", "checkpoint_kind: design_freeze",
            "owner_agent: research_architect_agent", "correlation_id: test-1",
            "expected_result: enum_comparison",
            'owner_decision: {"decision":"sound","drivers":[],"confidence":"high"}',
            "payload:", "RQ design payload", "[/CROSS-MODEL-HANDOFF]",
        ])
        body = anthropic_body()
        body["content"] = [{"type": "text", "text": json.dumps({
            "decision": "sound", "drivers": ["scope is coherent"], "confidence": "high"
        })}]
        captured = {}
        def opener(request, timeout):
            captured["body"] = request.data.decode()
            return Response(body)
        result = dispatch_handoff(envelope, consent=True, environ=ANTHROPIC_ENV,
                                  opener=opener, sleeper=Mock())
        self.assertEqual((result.status, result.outcome, result.provider, result.model),
                         ("complete", "agreement_fill_no_reinvoke", "anthropic", "claude-test"))
        self.assertIn("RQ design payload", captured["body"])
        self.assertNotIn('"decision":"sound"', captured["body"])

    def test_handoff_transport_failure_routes_unavailable_and_requires_consent(self):
        envelope = "\n".join([
            "[CROSS-MODEL-HANDOFF v1]", "checkpoint_kind: da_critique",
            "owner_agent: devils_advocate_reviewer_agent", "correlation_id: test-2",
            "expected_result: full_return", "payload:", "review data",
            "[/CROSS-MODEL-HANDOFF]",
        ])
        opener = Mock()
        result = dispatch_handoff(envelope, consent=False, environ=ANTHROPIC_ENV, opener=opener)
        opener.assert_not_called()
        self.assertEqual((result.status, result.outcome), ("consent_required", "unavailable"))


if __name__ == "__main__":
    unittest.main()
