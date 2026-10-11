# Extent of Romanian-language output

Type: grilling
Status: resolved
Blocked by: 02, 05
Map: ../map.md

## Question

How much Romanian should ARS produce: only the Romanian half of a `ro-en` abstract pair, full Romanian-language manuscripts for Romanian venues, or both? What does that mean for the writing-quality checks and style calibration in Romanian?

## Answer

Decided with Val (HITL):

- **All ARS output is English.** Papers are always written in English, and ARS never generates Romanian: no `ro-en` output-language pair and no Romanian abstracts.
- **Venues that require Romanian:** the SRP congress stays a target, but ARS supports only its English abstract; the author writes the Romanian half by hand. *Farmacia* is dropped from the targets.
- **Conversation language:** clinicians may talk to ARS in Romanian, but the overlay adds no Romanian trigger phrases (those would be a core `SKILL.md` edit).
- **Consequence:** the `ro` locale pack and the language-pair loader are no longer needed. The findings from [Romanian scientific-language resources](05-romanian-scientific-language.md) still apply to citations only (Romanian author names and diacritics, Vancouver variants); its Romanian-keyword and abstract-pair parts are moot.
