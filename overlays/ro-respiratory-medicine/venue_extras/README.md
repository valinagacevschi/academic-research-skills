# Venue extras

Venue extras hold scholar-declared venue rules that the core venue profile cannot represent, such as character-based abstract limits, required abstract headings, submission extras, and checklist reminders. The core profile remains the home for word limits and its other supported fields; extras hold only what core cannot.

Every extras file must say `declared_by: scholar`. The scholar supplies each value. The overlay never ships a filled extras file for a real venue; `example.venue_extras.yaml` uses an obviously fictional venue.

Run the checker with a YAML or JSON extras file and a Markdown or text manuscript:

```sh
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' --with pytest python overlays/ro-respiratory-medicine/venue_extras/check_venue_extras.py \
  --extras overlays/ro-respiratory-medicine/venue_extras/example.venue_extras.yaml \
  --manuscript manuscript.md
```

The checker uses the core verifier's Markdown abstract extraction. Core does not extract manuscript text from DOCX, so DOCX checks are reported as not checked. Checklist entries are reminders, never pass/fail results. The ERS Congress counting rule is used only when its primary evidence row is present; each figure consumes 277 characters of the allowance, and each table cell adds one character.

Character-limit support in the core venue profile is upstream ask #4 in [`docs/UPSTREAM_ASKS.md`](../docs/UPSTREAM_ASKS.md). Once core supports that field, the corresponding extras and checker workaround can be retired.
