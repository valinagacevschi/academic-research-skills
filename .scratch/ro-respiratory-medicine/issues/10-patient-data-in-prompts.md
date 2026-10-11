# Patient data in prompts

Type: grilling
Status: resolved
Assignee: val (Hermes session, 2026-10-10)
Blocked by: 01
Map: ../map.md

## Question

What is the overlay's stance when a clinician pastes clinical or patient-level data into the session: required de-identification, a warning, refusal, or local-only processing? How does that map to GDPR Art. 9, Law 190/2018, and Law 46/2003 confidentiality?

## Answer

Resolved by grilling with Val, 2026-10-10 (all recommendations approved). Core has no policy for patient data pasted into a session (`shared/references/irb_terminology_glossary.md` only defines the terms). The overlay handles this with the activation preamble and an optional hook, and makes no registry change.

- **Tiers** (see [GLOSSARY](../GLOSSARY.md)): **aggregate**; **line-level** (pseudonymised one-row-per-patient data, still Art. 9 health data); **direct identifiers** (name, CNP, address, phone, full dates of birth or admission, hospital record/FO numbers, identifiable images).
- **Response per tier:**
  - **Direct identifiers:** the agent stops once (not a refusal). It never echoes them or writes them to workspace files, asks the user to redact and re-paste, and reminds them the transcript already holds them.
  - **Line-level:** a one-time warning per session, then continue only after the user confirms their controller/DPO allows sending the data to the model provider.
  - **Aggregate:** no action.
- **Code-to-data instead of local-only processing.** The overlay can't route the session to a local model. The preamble steers line-level analysis into scripts that ARS writes and the user runs locally, so only aggregate results come back into the session. A local or EU-hosted model is mentioned as the user's own choice.
- **Optional CNP hook.** An opt-in Claude Code `UserPromptSubmit` + `PreToolUse(Read)` script blocks when it finds a checksum-valid CNP (13 digits, checksum, valid date and county code). The installer adds it only on consent. There's no heuristic detection of names or addresses, because eponyms and author names would cause false positives. Other runtimes rely on the preamble alone.
- **Legal framing.** Presented as questions for the controller/DPO, never as a ruling:
  - GDPR Art. 9(2) condition for health data;
  - Art. 28 processor agreement with the model provider, and Chapter V transfer if the provider is outside the EU;
  - Law 190/2018 Art. 4 restrictions on the CNP;
  - Law 46/2003 Arts. 21–22 confidentiality.

  No change to the `ro.*` profiles, because session hygiene isn't a study requirement.
- **Case reports and images:**
  - narrative allowed without direct identifiers, with dates as relative intervals, age in years, and rare details generalised;
  - never paste identifiable images; anonymised CT or bronchoscopy images are fine with DICOM metadata stripped;
  - consent is checked by the manuscript checks in [Romanian ethics-gate behaviour](09-romanian-ethics-gate.md) (CARE consent, Law 46 Art. 20).
