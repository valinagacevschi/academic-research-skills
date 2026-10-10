#!/usr/bin/env bash
# Stage the overlay into the eval sandbox workspace (the current directory).
# Runs only with `claude plugin eval --scaffold`. plugin-evals/ and tests/ are
# excluded so the agent cannot read graders or fixtures.
set -euo pipefail
overlay_root="$(cd "$(dirname "$0")/.." && pwd)"
dest="overlays/ro-respiratory-medicine"
mkdir -p "$dest"
tar -C "$overlay_root" --exclude ./plugin-evals --exclude ./tests --exclude '__pycache__' -cf - . | tar -C "$dest" -xf -
test -f "$dest/ACTIVATE.md"
