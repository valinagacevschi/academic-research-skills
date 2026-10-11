import json
from pathlib import Path
d = Path("research/probe")
alt = json.loads((d / "alt_registry.json").read_text())
ro = next(p for p in alt["profiles"] if p["profile_id"].startswith("ro."))
res = json.loads((d / "resolved.json").read_text())
raw = Path("scripts/fixtures/review_pathway_rule_trace/tw-candidates-request.json").read_text()
raw = raw.replace("tw.mohw.human-subjects-research-act", ro["profile_id"]).replace("tw.hsra", "ro.ethics")
req = json.loads(raw)
req["trace_request_id"] = "probe.ro-candidate-pathways"
req["context_pointer"] = res["context_pointer"]
req["registry_pointer"] = res["registry_pointer"]
req["resolved_digest"] = res["resolved_digest"]
def fix(v):
    if isinstance(v, dict):
        if v.get("profile_id") == ro["profile_id"]:
            v["profile_version"] = ro["profile_version"]; v["profile_digest"] = ro["profile_digest"]
        for x in v.values(): fix(x)
    elif isinstance(v, list):
        for x in v: fix(x)
fix(req)
(d / "ro_request.json").write_text(json.dumps(req, indent=2) + "\n")
