# Optional Codex CNP hook

`install.py --with-cnp-hook` adds `UserPromptSubmit` and `PreToolUse` for `Read` to the project's `.codex/hooks.json`. The guard checks submitted prompts and readable text files for checksum-valid Romanian CNPs.

On detection, it stops the prompt or read and asks for a redacted copy. The notice masks the identifier. It fails open on malformed hook input and unreadable, binary, or over-5-MB files.

Codex must trust the project hook before running it. This hook cannot remove data already present in a transcript.
