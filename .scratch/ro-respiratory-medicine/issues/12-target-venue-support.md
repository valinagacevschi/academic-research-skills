# Target-venue support and indexing checks

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 06
Map: ../map.md

## Question

Which target venues get shipped venue profiles and review-criteria entries in the overlay (e.g. ERJ, ERS Congress, *Pneumologia*, SRP congress English abstract, *Medicina*), and should the overlay run an index-status and scope-fit check before submission given the delisting risk found in the venue landscape research?

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved). Core constraints: venue profiles are scholar-declared only and intake never fills them from a journal's name (`academic-paper/agents/intake_agent.md:170-177`); the schema has no character-limit, abstract-heading or AI-disclosure fields; AI-disclosure placement lives in core's `academic-paper/references/venue_disclosure_policies.md`.

- **Venues covered:**
  - international journals: ERS journals (ERJ + ERJ Open Research, one entry), AJRCCM, CHEST, Thorax, Respiratory Medicine, IJTLD;
  - open access / Romanian: *Medicina*, *Pneumologia*, RJME, *Maedica*;
  - congresses: ERS Congress, and the SRP congress English half only.

  *Farmacia* stays dropped. Any other venue is declared from scratch by the author.
- **Venue notes, not pre-filled profiles.** One overlay reference file lists per-venue values, each with source URL, verified-on date and evidence tag. At intake the preamble shows the row as "what the overlay found; check the current author instructions". The scholar declares each value they confirm into the core venue profile, and unconfirmed fields stay null (NOT-CHECKED). Pre-filled YAML was rejected because it would put overlay values under a `declared_by: scholar` stamp.
- **Venue extras.** A small overlay-owned, scholar-declared file covers character-limit abstracts (ERS 1810 characters with table and figure penalties), required abstract headings, highlights or key messages, and checklists required with submission. A `check_venue_extras` script checks them. Which checklist applies still comes from [First-class study designs for the respiratory_medicine profile](08-first-class-study-designs.md).
- **AI disclosure.** Upstream ask: add ERS, ATS, Elsevier, IJTLD and MDPI rows to core's disclosure database. Until then, the venue notes carry each venue's placement as advisory for the author, and core's unknown-venue path governs what gets rendered. *Maedica*'s "≤30% AI" cap is flagged for the author, never claimed as met.
- **No `official_venue_type` review-criteria rows in v1.** No verified reviewer criteria exist for these venues. Venue fit is handled by the venue-status check.
- **Venue-status check.** Advisory, at submission readiness, never blocking and never ranking. Each item is recorded with URL + date:
  - Clarivate MJL;
  - the Scopus discontinued list;
  - NLM Catalog status;
  - the current UEFISCDI SCIE/ESCI list;
  - scope fit between manuscript and journal.

  The agent fetches the sources if the runtime has web access, otherwise it walks the author through them. A journal's own indexing claims never count. The overlay shows the three-tier venue picture but never recommends a venue.
- ***Pneumologia*.** Its notes row ships the known facts (English-only, Scopus-only, no WoS Core, out of MEDLINE since 2016, no fee, SRP prize link). Format fields are marked unverified. Fetching its instructions, and closing the CHEST, AJRCCM and Thorax gaps, joins [Fact-verification policy for overlay content](16-fact-verification-policy.md).
