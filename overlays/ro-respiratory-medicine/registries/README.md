# Registry generation

Run from the repository root:

```sh
uv run --no-project --python 3.12 --with pyyaml --with 'jsonschema[format]' python overlays/ro-respiratory-medicine/registries/build_registries.py
```

Use `--check` in CI to rebuild in memory and fail if the committed generated registry is stale. The builder reads the current core human-subjects registry, appends this overlay delta and validates the result with core `--check-registry`.

User context records pin profile digests. Re-pin selected profiles and display precedence after any rebuild. Registry releases also change the registry digest, so older resolved artifacts fail replay after an upstream registry bump; regenerate and replay the artifacts against the current registry.

Draft requirements omitted for lack of verified anchors: CTR excluded populations and Article 37(4) results publication; and Law 190/2018 Article 9(2)(j) lawful basis. OMS 3390/2022 anchors the consent-taker and principal-investigator requirements. The delta-level `known_gaps` also records verified rows retained as evidence but not modeled as separate requirements. Law 46/2003 Art. 19 requires research consent; the statute provides no research exception. Anonymisation practice is not a legal waiver, and Art. 22 disclosure risk for in-house pseudonymised data remains unresolved.
