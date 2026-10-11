#!/usr/bin/env python3
"""Verify one reference using the configured, consented non-GPT provider.

Reads one JSON object from stdin: {"reference": "...", "context": "..."}.
Prints a JSON verdict/provenance record. No credentials are read from files.
"""
from __future__ import annotations

import json
import argparse
import sys

from cross_model_request import verify_reference


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--consent", action="store_true",
                        help="confirm that the user approved sending this reference to the configured provider")
    args = parser.parse_args()
    if not args.consent:
        print(json.dumps({"status": "consent_required", "verdict": None,
                          "detail": "explicit per-session consent is required"}))
        return 2
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict):
            raise ValueError("input must be a JSON object")
        result = verify_reference(request)
    except (json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "unavailable", "verdict": None,
                          "detail": f"invalid_input: {exc}"}))
        return 2
    print(json.dumps(result.audit_record(), ensure_ascii=False))
    return 0 if result.status in {"complete", "not_configured"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
