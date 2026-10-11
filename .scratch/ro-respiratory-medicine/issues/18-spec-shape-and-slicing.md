# Spec shape and slicing into implementation tickets

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 17
Map: ../map.md

## Question

What does the hand-off spec look like, and how is it sliced for delegated implementation (Codex)? Covers:
- the spec's structure and where it lives (in this fork, outside `overlays/`?);
- how it gathers every decision on the map (overlay layout, activation, profile, registry deltas, design add-ons, ethics gate, patient data, venues, fact verification, evals) without restating the tickets;
- the upstream-asks list as its own section;
- the order of implementation slices, with the verification pass first;
- each slice's acceptance check (which `check_overlay` / lint / eval must pass);
- what "done" means for the overlay v1.

## Answer

Auto-approved 2026-10-10: Val asked to keep going and to auto-approve unanswered recommendations. Flagged for his review.

- **Location.** `overlays/ro-respiratory-medicine/docs/SPEC.md`, with the glossary copied to `overlays/ro-respiratory-medicine/docs/GLOSSARY.md`. Everything the fork adds stays under one directory, plus one additive CI workflow, so upstream merges never conflict. `dev/design/` is upstream's namespace, so the spec doesn't go there.
- **Self-contained.** This map and its tickets live in an untracked `.scratch/` directory, so the spec states each decision as a requirement. Each section names the ticket it came from for provenance only. Facts behind the decisions point to the `research/*` branches by commit.
- **Structure:**
  1. Destination and scope (in/out, upstream baseline commit)
  2. Vocabulary
  3. Overlay layout and activation
  4. Field profile
  5. Registry deltas and generators
  6. Design add-ons and subdomain references
  7. Ethics gate
  8. Patient data
  9. Venues
  10. Fact verification
  11. Tests and evals
  12. Implementation slices with acceptance checks
  13. Upstream asks
  14. Definition of done
  15. Open risks
- **Slices, in order:**
  - S1 skeleton + `check_overlay` + CI;
  - S2 verification pass (builds the verified data tables);
  - S3 field profile;
  - S4 human-subjects delta + generator;
  - S5 review-criteria delta + generator;
  - S6 subdomain references, design add-ons and reviewer prompts;
  - S7 venue notes, venue extras and `check_venue_extras`;
  - S8 patient-data preamble section + CNP hook;
  - S9 activation preamble + installer;
  - S10 plugin evals;
  - S11 upstream-asks drafts.

  S1 comes before the verification pass so its output is linted from the start. Content slices S4–S7 depend on S2. Each slice names its acceptance check.
- **Upstream asks** are drafted as issue texts in the spec. Filing them upstream needs Val's approval.
- **Done:** all slices merged in the fork; `check_overlay` and the deterministic suite green in CI; the six plugin evals passed once and recorded; the upstream-asks drafts written.
- **Pilot-clinician fog** is ruled out of scope (no clinician confirmed; auto-approved, flagged). It would return as a fresh effort.
