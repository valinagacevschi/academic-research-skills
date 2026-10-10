#!/usr/bin/env python3
"""Build overlay registries from the current core registries and local deltas."""
from __future__ import annotations
import argparse, copy, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
sys.path.insert(0,str(REPO))
from scripts.resolve_human_subjects_authority import digest
from scripts.resolve_review_target_context import validate_registry as validate_review_criteria
CORE=REPO/'shared/human_subjects_authority_registry.json'
DELTA=ROOT/'registries/human_subjects.delta.json'
OUTPUT=ROOT/'registries/generated/human_subjects_authority_registry.json'
REVIEW_CORE=REPO/'shared/review_criteria_registry.json'
REVIEW_DELTA=ROOT/'registries/review_criteria.delta.json'
REVIEW_OUTPUT=ROOT/'registries/generated/review_criteria_registry.json'
def build_human_subjects(core_path: Path=CORE, delta_path: Path=DELTA) -> dict:
 core=json.loads(core_path.read_text(encoding='utf-8')); delta=json.loads(delta_path.read_text(encoding='utf-8'))
 result=copy.deepcopy(core); result['registry_id']='human-subjects-authority-ro-respiratory-overlay'; result['registry_version']=core['registry_version']+'-ro.1'; result['as_of']=max(s['verified_at'] for s in delta['sources'])
 for key in ('fact_definitions','sources','profiles','overlays'):
  result[key].extend(copy.deepcopy(delta[key]))
 for profile in result['profiles'][len(core['profiles']):]:
  profile.pop('profile_digest',None); profile['profile_digest']=digest(profile)
 return result
def rendered(result: dict) -> str: return json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def build_review_criteria(core_path: Path=REVIEW_CORE, delta_path: Path=REVIEW_DELTA) -> dict:
 core=json.loads(core_path.read_text(encoding='utf-8')); delta=json.loads(delta_path.read_text(encoding='utf-8'))
 result=copy.deepcopy(core); result['registry_id']='review-criteria-ro-respiratory-overlay'; result['registry_version']=core['registry_version']+'-ro.1'; result['as_of']=max(row['source']['verified_at'] for row in delta['criteria'])
 for row in delta['criteria']:
  result['authority_classes'][row['authority_class']].append(row['criterion_id'])
 result['criteria'].extend(copy.deepcopy(delta['criteria']))
 return result
def validate(path: Path) -> None:
 cmd=['uv','run','--no-project','--python','3.12','--with','pyyaml','--with','jsonschema[format]','python',str(REPO/'scripts/resolve_human_subjects_authority.py'),'--registry',str(path),'--check-registry']
 subprocess.run(cmd,check=True,cwd=REPO)
def main(argv=None) -> int:
 parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--check',action='store_true'); args=parser.parse_args(argv)
 value=rendered(build_human_subjects()); review_value=rendered(build_review_criteria())
 if args.check:
  stale=[]
  if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8')!=value: stale.append(OUTPUT)
  if not REVIEW_OUTPUT.exists() or REVIEW_OUTPUT.read_text(encoding='utf-8')!=review_value: stale.append(REVIEW_OUTPUT)
  if stale:
   for path in stale: print(f'STALE: {path} differs from a fresh build',file=sys.stderr)
   return 1
  validate(OUTPUT); validate_review_criteria(json.loads(REVIEW_OUTPUT.read_text(encoding='utf-8'))); return 0
 OUTPUT.parent.mkdir(parents=True,exist_ok=True); OUTPUT.write_text(value,encoding='utf-8'); REVIEW_OUTPUT.write_text(review_value,encoding='utf-8'); validate(OUTPUT); validate_review_criteria(json.loads(review_value)); return 0
if __name__=='__main__': raise SystemExit(main())
