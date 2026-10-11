import json
import unittest

from cross_model_request import anthropic_request, gemini_request


class ProviderRequestTests(unittest.TestCase):
    def test_anthropic_messages_request(self):
        request = anthropic_request("claude-example", "synthetic", "check this")
        self.assertEqual(request.url, "https://api.anthropic.com/v1/messages")
        self.assertEqual(request.headers["x-api-key"], "synthetic")
        self.assertEqual(request.headers["anthropic-version"], "2023-06-01")
        self.assertEqual(json.loads(request.body), {
            "model": "claude-example", "max_tokens": 2048,
            "messages": [{"role": "user", "content": "check this"}],
        })

    def test_gemini_generate_content_request(self):
        request = gemini_request("gemini-example", "synthetic", "check this")
        self.assertTrue(request.url.endswith("/models/gemini-example:generateContent"))
        self.assertEqual(request.headers["x-goog-api-key"], "synthetic")
        self.assertEqual(json.loads(request.body), {
            "contents": [{"role": "user", "parts": [{"text": "check this"}]}],
        })

    def test_rejects_wrong_provider_model_or_missing_key(self):
        with self.assertRaises(ValueError):
            anthropic_request("gpt-example", "key", "prompt")
        with self.assertRaises(ValueError):
            gemini_request("claude-example", "key", "prompt")
        with self.assertRaises(ValueError):
            anthropic_request("claude-example", "", "prompt")
        with self.assertRaises(ValueError):
            gemini_request("gemini-example", "", "prompt")


if __name__ == "__main__":
    unittest.main()
