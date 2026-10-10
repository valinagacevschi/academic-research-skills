"""Probe: alternate human-subjects registry carrying a placeholder RO review_ethics profile."""
import copy, json, sys
from pathlib import Path
sys.path.insert(0, "scripts")
from resolve_human_subjects_authority import digest

root = Path(".")
out = Path("research/probe")
reg = json.loads((root / "shared/human_subjects_authority_registry.json").read_text())
alt = copy.deepcopy(reg)
alt["registry_id"] = "human-subjects-authority-ro-respiratory-overlay"
alt["registry_version"] = reg["registry_version"] + "-ro.1"

alt["fact_definitions"].append({
    "fact_id": "scope.ro_research_ethics",
    "value_type": "boolean",
    "allowed_values": None,
    "description": "User declaration that Romanian research-ethics review (local ethics committee) is an identified review authority for the activity.",
})
tw = next(p for p in reg["profiles"] if p["profile_id"].startswith("tw."))
ro_src_ids = []
for sid in tw["source_ids"]:
    src = copy.deepcopy(next(s for s in reg["sources"] if s["source_id"] == sid))
    src["source_id"] = sid.replace("tw.moj.hsra", "ro.placeholder.ethics")
    src["title"] = "PLACEHOLDER Romanian ethics-review source (probe only): " + src["title"]
    src["source_language"] = "ro"
    alt["sources"].append(src)
    ro_src_ids.append(src["source_id"])
ro = json.loads(json.dumps(tw).replace("tw.moj.hsra", "ro.placeholder.ethics").replace("scope.tw_hsra", "scope.ro_research_ethics").replace("tw.hsra", "ro.ethics"))
ro.update({
    "profile_id": "ro.placeholder.research-ethics",
    "profile_version": "2026-10-10",
    "title": "PLACEHOLDER Romanian research-ethics review profile (probe only)",
    "source_ids": ro_src_ids,
})
def _ro_lang(v):
    if isinstance(v, dict):
        if "source_language" in v: v["source_language"] = "ro"
        for x in v.values(): _ro_lang(x)
    elif isinstance(v, list):
        for x in v: _ro_lang(x)
_ro_lang(ro["requirements"])
ro.pop("profile_digest")
ro["profile_digest"] = digest(ro)
alt["profiles"].append(ro)
(out / "alt_registry.json").write_text(json.dumps(alt, indent=2, ensure_ascii=False) + "\n")

ctx = json.loads((root / "scripts/fixtures/human_subjects_authority/tw-gdpr-two-axis.json").read_text())
ctx = json.loads(json.dumps(ctx).replace("scope.tw_hsra", "scope.ro_research_ethics"))
ctx["context_record_id"] = "probe.ro-gdpr-observational"
sel = next(s for s in ctx["selected_profiles"] if s["axis"] == "review_ethics")
sel.update({"profile_id": ro["profile_id"], "profile_version": ro["profile_version"],
            "profile_digest": ro["profile_digest"], "authority_scope_ids": ro["authority_scope_ids"]})
ref = ctx["display_precedence"][0]["ordered_authorities"][0]
ref.update({"authority_id": ro["profile_id"], "authority_version": ro["profile_version"], "authority_digest": ro["profile_digest"]})
(out / "ro_context.json").write_text(json.dumps(ctx, indent=2, ensure_ascii=False) + "\n")
print("built", ro["profile_id"], ro["profile_digest"])
