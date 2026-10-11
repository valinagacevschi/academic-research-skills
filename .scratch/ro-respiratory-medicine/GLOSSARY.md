# Glossary: Romanian respiratory-medicine adaptation

**Overlay**
A set of files that sits beside ARS core, changes no core file, and takes effect only in projects where it has been activated. It carries field and Romanian context (a field profile, registry additions, venue and format templates), not language assets.
_Avoid_: locale pack, pack (upstream reserves "locale pack" for Phase-2 `locales/<locale>/` language and presentation assets)

**Activation preamble**
The instruction block a user adds to a project so that an ARS session uses the overlay's registries, profile and templates.
_Avoid_: wrapper, plugin

**Upstream ask**
A change that would help the overlay but belongs in core, so it is offered to upstream as a separate track and never made in the fork.
_Avoid_: core fix (in the fork)

**First-class design**
A study design for which the overlay adds respiratory-specific companion guidelines, measurement standards, data-source notes and reviewer prompts on top of the reporting guideline core ARS chooses.
_Avoid_: supported design, overlay route

**Fallback design**
A study design that gets core's reporting guideline unchanged, plus only the respiratory content that applies to every design.

**Subdomain reference**
The overlay's file of edition-stamped definitions, outcome sets and minimal clinically important differences for one area of pulmonology (e.g. airways disease, sleep). It applies to every study design.
_Avoid_: subdomain pack

**Aggregate data**
Summary results (tables, counts, estimates, model outputs) from which no single patient can be read off.

**Line-level data**
Data with one row per patient and no direct identifiers. It is still personal health data, not anonymous.
_Avoid_: anonymised data (unless anonymisation has actually been established)

**Direct identifier**
A value that names or singles out a patient on its own: name, CNP, address, phone, full date of birth or admission, hospital record number, identifiable image.

**Venue notes**
The overlay's sourced, dated record of what each supported venue's author instructions say. The scholar reads it and declares the values they confirm; it is never a declared venue profile itself.
_Avoid_: venue profile (that term means the scholar's declaration)

**Venue extras**
Scholar-declared venue rules that core's venue profile can't hold, such as character-limit abstracts, required abstract headings and highlights.

**Venue-status check**
An advisory, dated check of a target venue's current indexing and its scope fit with the manuscript, made against registries and never against the journal's own claims.

**Evidence tag**
How the overlay knows a value: `primary-full-text`, `primary-abstract`, `secondary`, `recalled` or `unreachable`. Only the two primary tags count as fact.
_Avoid_: confidence, citation-only, snippet (folded into `secondary`)

**Verification backlog**
The list of values found during research that are not yet primary-sourced, kept for the first implementation slice to verify, keep as advisory, or drop.
