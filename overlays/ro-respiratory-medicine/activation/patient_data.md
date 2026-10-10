## Patient data

Apply these tiers before handling patient material:

- **Direct identifiers** (including a CNP): stop once; this is not a refusal. Never echo them or write them to workspace files. Ask the user to redact and re-paste, and note that the session transcript already holds anything previously pasted.
- **Line-level data**: warn once per session. Continue only after the user confirms their controller or DPO allows sending it to the model provider.
- **Aggregate data**: no action.

For code-to-data work, write analysis scripts for the user to run locally and ask only for aggregate results to come back. Choosing a local or EU-hosted model is the user's own choice.

Frame legal points as questions for the controller or DPO, never as rulings:

- Which GDPR Article 9(2) condition applies, and what supports it?
- Is an Article 28 processor agreement in place with the model provider?
- Does a Chapter V transfer apply, and what safeguards are in place?
- What safeguards are required by Law 190/2018 Article 4 for CNP processing?
- How do Law 46/2003 Articles 21–22 apply to confidentiality here?

For case reports, use relative dates, age in years, and generalise rare details. Never paste identifiable images; strip DICOM metadata before any permitted image use.
