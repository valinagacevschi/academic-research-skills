# Romanian scientific-language resources

Type: research
Status: resolved
Map: ../map.md

## Question

What resources and conventions govern scientific Romanian in medicine? Cover: whether a Romanian MeSH or DeCS translation exists, Romanian medical terminology references (DEX, medical dictionaries, Romanian ICD-10 / ICD-11 translations), the comma-below diacritics ș/ț vs cedilla ş/ţ (Unicode, and how journals and PubMed handle them), conventions for Romanian author names in citations and indexing (diacritics stripped?), and the citation styles Romanian medical journals use (Vancouver variants). Output informs `ro-en` output-language-pair registry entries and citation-locale evals.

## Answer

- **No Romanian MeSH or DeCS exists**, so Romanian keywords can only be translations of English MeSH terms.
- **Classifications:** Romania codes with ICD-10-AM (3rd ed., OMS 1027/2010); there's no released Romanian ICD-11, MedDRA Romanian is still in development, and SNOMED CT has no Romanian translation. The EDQM standard drug-form terms exist in Romanian.
- **ș/ț:** DOOM2 and Unicode both require the comma-below forms (U+0218–021B), and normalization never folds cedilla into comma. PubMed keeps the publisher's characters (RJME uses only the cedilla; RJIM mixes both), and its search ignores diacritics.
- **Citations:** NLM *Citing Medicine* drops diacritics from author names. Romanian journals all use Vancouver variants that differ in detail (brackets, et-al threshold, capitalised surnames, DOI/PMID required or forbidden).
- **Implications:** `ro-en` would be the first pair where both languages are Latin-script, so script can't tell the abstracts apart. Generated text should always use comma forms, while quoted reference data keeps the publisher's characters. The findings file proposes a registry entry, writing and citation rules, and six eval cases.
- **Unverified:** *Pneumologia*'s reference style and the number of the Romanian character-set standard.

Findings: branch `research/romanian-scientific-language` (commit `e617161`), file `research/romanian-scientific-language.md` (worktree `/Users/val/dev/ars-research/romanian-scientific-language`).
