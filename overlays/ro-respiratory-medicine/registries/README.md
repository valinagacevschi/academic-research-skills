# Registry generation

Run from the repository root:

```sh
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' python overlays/ro-respiratory-medicine/registries/build_registries.py
```

Use `--check` in CI to rebuild both registries in memory and fail if either committed generated registry is stale. The builder appends the overlay deltas to the current core registries, preserves every core row, and validates each generated registry with its core validator.

User context records pin human-subjects profile digests. Re-pin selected profiles and display precedence after any rebuild. Registry releases also change the registry digest, so older resolved artifacts fail replay after an upstream registry bump; regenerate and replay the artifacts against the current registry.

## Human-subjects delta

Draft requirements omitted for lack of verified anchors: CTR excluded populations and Article 37(4) results publication; and Law 190/2018 Article 9(2)(j) lawful basis. OMS 3390/2022 anchors the consent-taker and principal-investigator requirements. The delta-level `known_gaps` also records verified rows retained as evidence but not modeled as separate requirements. Law 46/2003 Art. 19 requires research consent; the statute provides no research exception. Anonymisation practice is not a legal waiver, and Art. 22 disclosure risk for in-house pseudonymised data remains unresolved.

## Review-criteria delta

`review_criteria.delta.json` adds ATS/ERS respiratory measurement, RECORD, STROME-ID, and supported Romanian manuscript-statement criteria. Each criterion source URI must match a `data/` row. Receipts in `review_criteria_sources/` follow the core mutable-web receipt contract, record retrieval metadata, and bind criterion IDs to the quoted locator and source note from the corresponding verified data row.

All six Romanian manuscript-statement checks use `advisory_only`. In the core resolver a result is blocking-eligible only when its source freshness is `current` **and** its policy is `blocking_allowed`; advisory-only pointers cannot support Critical/Major blocking findings in the consumer protocol. The policy also keeps missing manuscript statements Conditional at most, consistent with SPEC §7.1. Romanian legal sources use `field_society_standard` because the closed authority classes have no national-law class; this is a classification for routing, not a claim that a professional society issued the law. Their rows remain advisory.

The ERS/ATS measurement criterion is advisory and cites the spirometry row as its primary source. Its combined statement names spirometry 2019, DLCO 2017, interpretation 2022, and race-neutral GLI; separate source receipts bind the other standards to their methodology rows. Lung volumes, FeNO, and field-walking standards are not included in this criterion because the requested S5 criterion is limited to the named standards. STROME-ID is represented; TB diagnostic criteria are omitted because S5 supplies no corresponding reviewer criterion/source requirement.

The EU CT-number check is omitted: `ro.ctis-evaluation` verifies that decisions are transmitted through CTIS but does not establish that a manuscript must state the EU CT number. The consent/anonymisation criterion is limited to the cited research-consent rule; no separate verified source row establishes a general journal-statement format. The ethics criterion is limited to CNBMDM's ethical analysis and opinions; the exact committee-name, approval-number, and date formatting remains a reviewer prompt. The CMR conflict row addresses identification and elimination of conflicts affecting medical decisions, not journal disclosure formatting, so the disclosure check is advisory and its format is not asserted as a legal rule.
