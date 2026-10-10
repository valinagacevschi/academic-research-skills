# Fact-verification policy for overlay content

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 08
Map: ../map.md

## Question

What may the overlay encode as a fact, and what verification pass must the rest go through before the spec is handed off? The research tickets tag values as *abstract-read*, *citation-only*, *recalled* or *unverified*, and some primary sources couldn't be reached (legislatie.just.ro, insp.gov.ro, several journal sites). Decide:
- the encoding rule per evidence tag (encode as fact, encode as advisory with a caveat, or leave out);
- how each value records its tag and source in the subdomain references and the registry deltas;
- whether a verification-pass task runs before the spec or as the first implementation slice. It would re-fetch unreachable sources, read full texts for the open values in the closed subdomain tickets, get the *Pneumologia* author instructions, and close the CHEST, AJRCCM and Thorax gaps from [Target-venue support and indexing checks](12-target-venue-support.md);
- how values go stale: the freshness and edition-recheck cadence, given that `check_overlay` already tracks upstream drift.

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved). It aligns with core's source vocabulary: `freshness` current/stale/unverified/superseded with `verified_at`, `authenticity_status`, and the rule that any review-criteria source that isn't `current` is advisory only.

- **One evidence-tag vocabulary** (see [GLOSSARY](../GLOSSARY.md)): `primary-full-text`, `primary-abstract`, `secondary` (third party, search snippet or citing paper), `recalled` (model memory), `unreachable`. It replaces the mixed tags in the research branches. Mapping onto core: both primary tags → `freshness: current` with `verified_at`; `secondary` → `unverified`; `recalled` and `unreachable` are never encoded.
- **Encoding rule:**
  - both primary tags → encoded as fact and may drive checks at the grades already decided;
  - `secondary` → advisory only, with a visible "verify" caveat, never a check;
  - `recalled` / `unreachable` → not encoded, put on the verification backlog.

  Numeric thresholds (MCIDs, cut-offs, limits) need at least `primary-abstract` where the abstract states the number. Legal texts are `authoritative_unofficial` until checked on the official portal, then `official_controlling_language`.
- **How evidence is recorded:**
  - every encoded value carries source URL, title, locator, evidence tag, `verified_at`, and edition or version where one exists;
  - registry deltas use the native source fields (and receipts for review-criteria rows);
  - subdomain references and venue notes use the same fields as table columns;
  - `check_overlay` fails on a missing tag, date or URL, on any encoded `recalled` or `unreachable` value, and on any `secondary` number used as a check.
- **Verification pass = the first implementation slice**, run by an agent alone. No decision on the map depends on an unverified value. The spec carries the **verification backlog**: every `recalled` / `secondary` / `unreachable` value in the research branches, plus the *Pneumologia*, CHEST, AJRCCM and Thorax gaps and the official legal portal checks.

  What happens to a value in the pass: verified to primary → promoted; found only in a secondary source → stays advisory; still unreachable or contradicted → dropped. A verification counts when an agent fetch records URL, date and the quoted locator. A clinician can upgrade a value with a signed note.
- **Staleness:** age-based demotion to advisory past `verified_at` + window:
  - 12 months for clinical standards and legal texts;
  - 6 months for venue notes;
  - indexing status is never cached (the venue-status check fetches it live).

  An edition-watch list (GOLD/GINA yearly, AASM, TNM, WSPH, ESC PE expected 2027) flags subdomain references for re-check. There are no automatic web re-checks: the lint only demotes and flags, and re-verifying is a human-triggered agent task.
