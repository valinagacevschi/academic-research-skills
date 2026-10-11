# CNP guard

`cnp_guard.py` is an opt-in Claude Code hook that detects checksum-valid Romanian CNPs in submitted prompts and files opened with `Read`. On detection it blocks the event and asks for a redacted re-send; its message masks the number. It fails open on malformed input and unreadable, binary, or over-5-MB files.

The guard checks CNP structure, dates, county codes, and checksum only. It does not detect names, addresses, other identifiers, or health data without a valid CNP. It cannot remove information already held in a session transcript or by a model provider. Other runtimes rely on the patient-data preamble only.

Add this to `.claude/settings.json` to enable both events:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          { "type": "command", "command": "python3 /path/to/overlays/ro-respiratory-medicine/hooks/cnp_guard.py" }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          { "type": "command", "command": "python3 /path/to/overlays/ro-respiratory-medicine/hooks/cnp_guard.py" }
        ]
      }
    ]
  }
}
```
