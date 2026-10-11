# Contributing to Academic Research Skills

Thank you for your interest in contributing. This document explains what kinds of contributions we accept and how to submit them.

---

## How to submit a contribution

ARS uses the standard **fork-and-PR** workflow. Fork the repo on GitHub, clone your fork, create a branch, make your changes, push to your fork, then open a PR against `Imbad0202/academic-research-skills`.

**Important**: You cannot push directly to this repo — you must fork it first and submit a PR from your fork.

---

## What we accept

### Community-maintained (fast merge)

These contributions can be merged quickly with minimal review:

- **Typo and formatting fixes** — spelling, broken links, markdown rendering issues
- **New examples** — pipeline output showcases, worked examples for specific disciplines
- **Translation improvements** — better phrasing in READMEs. Translations that touch operative instructions (agent definitions, IRON RULE text, integrity protocols, trigger keywords) are not fast-merge; they follow the review tier of the file they touch, even when presented as translation.

### Requires maintainer review

These need careful review because they affect system behavior:

- **Journal and field reference lists** — additions to `top_journals_by_field.md`, new discipline glossaries
- **Evaluation sets** — gold-standard papers for calibration mode, benchmark data
- **New reference files** — methodology guides, citation format references, domain-specific protocols
- **Bug and drift fixes** — version inconsistencies, broken cross-references, incorrect metadata
- **Mode changes** — new modes, trigger keyword changes, oversight level adjustments

### Requires maintainer approval + discussion

Open an issue first before submitting a PR for these:

- **Agent definition changes** — modifications to any file in `*/agents/*.md`
- **IRON RULE modifications** — any change to rules marked with the IRON RULE marker
- **Ethics and integrity rules** — changes to the failure mode checklist, integrity protocols, or ethics review
- **Handoff schema changes** — modifications to `shared/handoff_schemas.md`
- **New skills or modes** — additions to the pipeline

### Locale packs (community-maintained)

ARS ships one default locale: English plus Traditional Chinese (zh-TW), the pairing the bilingual abstract, the Chinese citation guide, the worked examples, and the PDF fonts assume. Support for another output locale is delivered as a **locale pack**, and every non-default pack is community-maintained, whether it lives under `locales/<locale>/` in this repository or in a sibling distribution. The maintainer owns the extension interface and the default behaviour; the maintainer does not translate, review, or support a pack's language content.

Until the locale mechanism lands (Phase 1 tracked in #862, design in #850), activation-layer contributions are still accepted on their own: a translated README under the existing README drift lints, and conservative, intent-specific trigger phrases under the #509 rules (no broad standalone words, routing smoke evidence, boundary fixtures under `tests/fixtures/issue_133_routing/`, and all four `description` fields kept under the Agent Skills 1,024-character limit).

A pack is accepted and stays listed as supported under these conditions:

- **Two named owners.** A primary owner and a distinct backup owner, both stated in the pack's manifest, who accept language review, locale-specific issues, and synchronisation with every ARS minor release. Locale-specific issues are redirected to them.
  - *Provisional applications.* A single-owner application may be recorded as provisional in a dedicated issue once the primary owner accepts these responsibilities there. A provisional application is not a supported pack. The first minor release after both the locale mechanism and that acceptance opens a 14-day window in which a distinct backup owner must accept the same responsibilities; the maintainer records the qualifying release and deadline in the issue. If the window closes without a backup, the application expires, and reapplication requires two accepted owners and current evidence. A supported pack that loses either owner leaves the supported list until two owners are again accepted.
- **Recorded currency.** The pack records the last upstream commit and release it was verified against, the capabilities it covers, and reproducible validation evidence. Within 14 days of each minor release the owners either update the pack or record a compatibility attestation for the new release.
- **Visible staleness.** CI fails visibly for a listed pack whose compatibility record is stale, whose tracked upstream dependencies changed, or whose mappings, assets, or required fixtures are missing or invalid. A missed deadline marks the pack stale and removes it from the supported list; this never delays a core release. Two consecutive missed minor releases, or the loss of both owners, allow the pack to be deprecated and unbundled. Reinstatement requires accepted ownership and current evidence.
- **Configuration and presentation only.** A pack supplies documented configuration and presentation assets: trigger phrases, the output-language pair, citation-guide mapping, example sets, fonts. It never replaces or overlays core `SKILL.md` files, agent definitions, IRON RULE text, integrity protocols, handoff schemas, modes, or oversight rules. A change that alters workflow semantics goes through normal maintainer review even when it arrives as translation.
- **Trigger discipline.** Trigger phrases follow the #509 rules above; a pack cannot widen a skill's activation with standalone words.

Third-party directory listings in `THIRD_PARTY.md` remain a separate, non-endorsement channel and do not confer supported-pack status.

---

## PR guidelines

- **One concern per PR** — don't mix unrelated changes
- **Describe what and why** — explain the motivation, not just the change
- **Reference issues** — if your PR addresses an open issue, link it
- **Test your changes** — if you're modifying agent definitions, try running the skill to confirm it works as expected
- **Keep READMEs in sync** — if your change affects user-facing documentation, update `README.md` and the relevant documentation under `docs/`

---

## Governance

### Maintainer

The repo is maintained by [Cheng-I Wu](https://github.com/Imbad0202) (HEEACT). The maintainer has final say on all merges.

### Decision principles

1. **Accuracy over completeness** — we'd rather have fewer, verified journal entries than a long unvetted list
2. **Human-in-the-loop always** — contributions that reduce human oversight or enable fully autonomous paper generation will be declined
3. **No detection evasion** — features designed to make AI-generated text harder to detect (as opposed to higher quality) are out of scope. See [Issue #3](https://github.com/Imbad0202/academic-research-skills/issues/3) for context.
4. **Discipline diversity welcome** — ARS defaults to higher education research but aims to be domain-agnostic. Discipline-specific modules are encouraged.

---

## Academic integrity policy

This repo is designed to be **assistive, not deceptive**. See [POSITIONING.md](POSITIONING.md) for the full design philosophy. Contributors must not add features designed to evade AI detection tools. If unsure, open an issue to discuss before submitting a PR.

---

## Credit

Contributors are credited in commit messages, CHANGELOG entries, and the Contributors section of the README. For significant contributions (new features, major reference files), we also add a mention in the relevant release notes.

## License

By contributing, you agree that your contributions will be licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). See [POSITIONING.md](POSITIONING.md) for usage terms.

## When adding a new skill

Read [`shared/ground_truth_isolation_pattern.md`](shared/ground_truth_isolation_pattern.md) before writing the SKILL.md. It explains the three-layer model behind the `data_access_level` and `task_type` frontmatter fields and lists the do/don't rules for handling evaluation rubrics, gold labels, and answer keys.
