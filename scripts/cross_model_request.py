"""Stdlib request builders for the opt-in non-GPT ARS verifier.

These builders are intentionally offline and provisional. They construct
provider HTTP requests but do not send content or claim response validation.
"""
from __future__ import annotations

from dataclasses import dataclass
import json


@dataclass(frozen=True)
class HttpRequest:
    url: str
    headers: dict[str, str]
    body: bytes


def _json(body: dict[str, object]) -> bytes:
    return json.dumps(body, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def anthropic_request(model: str, api_key: str, prompt: str) -> HttpRequest:
    if not model.startswith("claude-"):
        raise ValueError("Anthropic verifier model must use the claude- prefix")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY is required")
    return HttpRequest(
        url="https://api.anthropic.com/v1/messages",
        headers={
            "content-type": "application/json",
            "anthropic-version": "2023-06-01",
            "x-api-key": api_key,
        },
        body=_json({
            "model": model,
            "max_tokens": 2048,
            "messages": [{"role": "user", "content": prompt}],
        }),
    )


def gemini_request(model: str, api_key: str, prompt: str) -> HttpRequest:
    if not model.startswith("gemini-"):
        raise ValueError("Gemini verifier model must use the gemini- prefix")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is required")
    return HttpRequest(
        url=f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        headers={"content-type": "application/json", "x-goog-api-key": api_key},
        body=_json({
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        }),
    )
