import copy, json, subprocess, sys
from pathlib import Path

import check_overlay
from registries import build_registries

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[1]
PYTHON=[sys.executable]
REG=ROOT/'registries/generated/human_subjects_authority_registry.json'

def test_build_is_deterministic_and_validates():
    first=build_registries.rendered(build_registries.build_human_subjects())
    assert first==build_registries.rendered(build_registries.build_human_subjects())
    result=subprocess.run(PYTHON+[str(REPO/'scripts/resolve_human_subjects_authority.py'),'--registry',str(REG),'--check-registry'],capture_output=True,text=True)
    assert result.returncode==0, result.stderr
    assert build_registries.main(['--check'])==0

def test_delta_waiver_routes_are_closed_to_authority_or_not_applicable():
    delta=json.loads((ROOT/'registries/human_subjects.delta.json').read_text())
    assert all(r['waiver_or_exception_route']['state'] in {'external_authority_required','not_applicable'} for p in delta['profiles'] for r in p['requirements'])

def test_delta_anchor_without_row_and_stale_generated_file_fail(tmp_path):
    import shutil
    shutil.copytree(ROOT,tmp_path/'overlay',ignore=shutil.ignore_patterns('__pycache__'))
    overlay=tmp_path/'overlay'; delta=json.loads((overlay/'registries/human_subjects.delta.json').read_text())
    delta['profiles'][0]['requirements'][0]['authority_anchor']['provision']='Art. 99'; next(s for s in delta['sources'] if s['source_id']=='ro.oug-29-2022')['allowed_provisions'].append('Art. 99')
    (overlay/'registries/human_subjects.delta.json').write_text(json.dumps(delta))
    errors=check_overlay.check_human_subjects_registry(overlay,REPO)
    assert errors and 'stale' in errors[0]
    # Isolate anchor validation by updating the copied generated artifact from the changed delta.
    from registries import build_registries as builder
    builder_root=builder.ROOT
    try:
        builder.ROOT=overlay
        fresh=builder.rendered(builder.build_human_subjects(core_path=REPO/'shared/human_subjects_authority_registry.json',delta_path=overlay/'registries/human_subjects.delta.json'))
        (overlay/'registries/generated/human_subjects_authority_registry.json').write_text(fresh)
    finally:
        builder.ROOT=builder_root
    errors=check_overlay.check_human_subjects_registry(overlay,REPO)
    assert errors and 'no legal_ro.json anchor row' in errors[0]

def test_ro_retrospective_context_resolves_and_replays(tmp_path):
    registry=json.loads(REG.read_text())
    context=json.loads((REPO/'scripts/fixtures/human_subjects_authority/tw-gdpr-two-axis.json').read_text())
    context['context_record_id']='fixture.ro-retrospective-records'
    context['applicability_as_of']='2026-10-10'
    defs={f['fact_id']:f for f in registry['fact_definitions']}
    for row in context['declared_facts']:
        if row['fact_id']=='scope.tw_hsra': row['fact_id']='scope.ro_patient_rights'
    additions=['professional.ro_cmr_member','activity.retrospective_records_only','scope.ro_law_190','data.ro_cnp_processed']
    for fact_id in additions:
        context['declared_facts'].append({'fact_id':fact_id,'value_type':'boolean','state':'declared','value':fact_id!='data.ro_cnp_processed','provenance':'author_declared'})
    ro_review=[p for p in registry['profiles'] if p['profile_id'] in {'ro.parliament.law-46-2003.patient-rights-research','ro.cmr.deontology-code-2025'}]
    law190=next(p for p in registry['profiles'] if p['profile_id']=='ro.parliament.law-190-2018.research-bounded')
    gdpr=next(p for p in registry['profiles'] if p['profile_id']=='eu.gdpr.research-core-bounded')
    selected=[]; precedence=[]
    for p in [*ro_review,gdpr,law190]:
        selected.append({'axis':p['axis'],'profile_id':p['profile_id'],'profile_version':p['profile_version'],'profile_digest':p['profile_digest'],'authority_scope_ids':p['authority_scope_ids']})
    for axis,ps in [('review_ethics',ro_review),('data_protection',[gdpr,law190])]:
        precedence.append({'axis':axis,'purpose':'display_only_no_suppression','ordered_authorities':[{'authority_kind':'profile','axis':axis,'authority_id':p['profile_id'],'authority_version':p['profile_version'],'authority_digest':p['profile_digest']} for p in ps]})
    context['selected_profiles']=selected; context['display_precedence']=precedence
    context['scope_dimensions']['review_jurisdictions']=['scope.ro_patient_rights']; context['scope_dimensions']['study_types'].append('activity.retrospective_records_only')
    cp=tmp_path/'context.json'; cp.write_text(json.dumps(context))
    resolved=tmp_path/'resolved.json'
    cmd=PYTHON+[str(REPO/'scripts/resolve_human_subjects_authority.py'),'--context',str(cp),'--registry',str(REG),'--output',str(resolved)]
    result=subprocess.run(cmd,capture_output=True,text=True); assert result.returncode==0,result.stderr
    result=subprocess.run(PYTHON+[str(REPO/'scripts/resolve_human_subjects_authority.py'),'--context',str(cp),'--registry',str(REG),'--check-resolved',str(resolved)],capture_output=True,text=True); assert result.returncode==0,result.stderr
    core=REPO/'shared/human_subjects_authority_registry.json'
    result=subprocess.run(PYTHON+[str(REPO/'scripts/resolve_human_subjects_authority.py'),'--context',str(cp),'--registry',str(core)],capture_output=True,text=True); assert result.returncode!=0
    # Exercise the pointer-bound review trace and packet-manifest builders.
    import hashlib, shutil
    ro_profile=ro_review[0]
    trace_request=json.loads((REPO/'scripts/fixtures/review_pathway_rule_trace/tw-candidates-request.json').read_text())
    trace_request['trace_request_id']='fixture.ro-candidate-pathways'
    trace_request['context_pointer']=json.loads(resolved.read_text())['context_pointer']
    trace_request['registry_pointer']=json.loads(resolved.read_text())['registry_pointer']
    trace_request['resolved_digest']=json.loads(resolved.read_text())['resolved_digest']
    templates={c['profile_ref']['axis']:c for c in trace_request['candidate_pathways']}
    trace_request['candidate_pathways']=[]
    for selected in selected:
        p=next(p for p in registry['profiles'] if p['profile_id']==selected['profile_id'])
        candidate=copy.deepcopy(templates[p['axis']])
        candidate['candidate_id']='candidate.'+p['profile_id']
        candidate['profile_ref'].update(profile_id=p['profile_id'],profile_version=p['profile_version'],profile_digest=p['profile_digest'])
        candidate['predicate_requirement_ids']=sorted(r['requirement_id'] for r in p['requirements'])
        trace_request['candidate_pathways'].append(candidate)
    trace_request['candidate_pathways'].sort(key=lambda c:c['candidate_id'])
    trace_req=tmp_path/'trace-request.json'; trace_req.write_text(json.dumps(trace_request))
    trace=tmp_path/'trace.json'
    base_cmd=PYTHON+[str(REPO/'scripts/build_review_pathway_rule_trace.py')]
    result=subprocess.run(base_cmd+['build','--request',str(trace_req),'--context',str(cp),'--registry',str(REG),'--resolved',str(resolved),'--output',str(trace)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    result=subprocess.run(base_cmd+['validate','--request',str(trace_req),'--context',str(cp),'--registry',str(REG),'--resolved',str(resolved),'--trace',str(trace)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr

    inventory=json.loads((REPO/'scripts/fixtures/submission_packet_manifest/base_inventory.json').read_text())
    artifact=inventory['artifacts'][1]
    requirement=ro_profile['requirements'][0]
    artifact['evidence_bindings']=[{'requirement_id':requirement['requirement_id'],'evidence_id':requirement['evidence_expected'][0]['evidence_id']}]
    inventory['artifacts']=[artifact]
    packet=tmp_path/'packet'; packet.mkdir()
    content=(REPO/'scripts/fixtures/submission_packet_manifest/packet/tw-consent-materials.txt').read_bytes()
    (packet/artifact['relative_path']).write_bytes(content)
    artifact['declared_sha256']=hashlib.sha256(content).hexdigest(); artifact['declared_size_bytes']=len(content)
    inv=tmp_path/'inventory.json'; inv.write_text(json.dumps(inventory))
    manifest=tmp_path/'manifest.json'
    packet_cmd=PYTHON+[str(REPO/'scripts/build_submission_packet_manifest.py')]
    result=subprocess.run(packet_cmd+['build','--inventory',str(inv),'--packet-root',str(packet),'--context',str(cp),'--registry',str(REG),'--resolved',str(resolved),'--output',str(manifest)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    result=subprocess.run(packet_cmd+['validate','--manifest',str(manifest),'--inventory',str(inv),'--packet-root',str(packet),'--context',str(cp),'--registry',str(REG),'--resolved',str(resolved)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr


def test_research_consent_and_oms3390_requirements_are_anchored():
    delta=json.loads((ROOT/'registries/human_subjects.delta.json').read_text())
    profiles={p['profile_id']:p for p in delta['profiles']}
    law=profiles['ro.parliament.law-46-2003.patient-rights-research']
    consent=next(r for r in law['requirements'] if r['requirement_id']=='ro.patient-rights.research-consent')
    assert consent['obligation_kind']=='require'
    assert consent['authority_anchor']['provision']=='Art. 19'
    assert consent['waiver_or_exception_route']['state']=='external_authority_required'
    assert 'participant_information' in consent['consumer_scopes']
    ctr=profiles['ro.ms.ctr-national-implementation']
    requirements={r['requirement_id']:r for r in ctr['requirements']}
    assert requirements['ro.ctr.clinical-consent-taker']['obligation_kind']=='require'
    assert requirements['ro.ctr.clinical-consent-taker']['authority_anchor']['provision']=='Norms Art. 15(1)'
    assert requirements['ro.ctr.pi-qualification']['obligation_kind']=='condition'
    assert requirements['ro.ctr.pi-qualification']['authority_anchor']['provision']=='Norms Art. 16(2)'
    assert 'ro.oms-3390-2022' in ctr['source_ids']


def test_all_profiles_and_requirements_use_their_scope_fact():
    delta=json.loads((ROOT/'registries/human_subjects.delta.json').read_text())
    expected={
        'ro.ms.ctr-national-implementation':'scope.ro_ctr_national',
        'ro.ms.mdr-clinical-investigation':'scope.ro_mdr_investigation',
        'ro.parliament.law-46-2003.patient-rights-research':'scope.ro_patient_rights',
        'ro.parliament.law-190-2018.research-bounded':'scope.ro_law_190',
        'ro.cmr.deontology-code-2025':'professional.ro_cmr_member',
    }
    for profile in delta['profiles']:
        fact=expected[profile['profile_id']]
        for item in [profile,*profile['requirements']]:
            predicate=item['applies_if']
            if profile['profile_id']=='ro.parliament.law-46-2003.patient-rights-research':
                assert predicate=={'op':'all','operands':[{'op':'fact_equals','fact_id':'activity.human_subjects','value':True},{'op':'fact_equals','fact_id':fact,'value':True}]}
            else:
                assert predicate=={'op':'fact_equals','fact_id':fact,'value':True}
    law=next(p for p in delta['profiles'] if p['profile_id']=='ro.parliament.law-46-2003.patient-rights-research')
    assert {'ro.patient-rights.research-consent','ro.patient-rights.confidentiality','ro.patient-rights.disclosure'} <= {r['requirement_id'] for r in law['requirements']}
    from scripts.resolve_human_subjects_authority import evaluate_predicate
    prospective_facts={
        'activity.human_subjects': {'state':'declared','value':True},
        'scope.ro_patient_rights': {'state':'declared','value':True},
        'activity.retrospective_records_only': {'state':'declared','value':False},
    }
    for requirement in law['requirements']:
        if requirement['requirement_id'] in {'ro.patient-rights.research-consent','ro.patient-rights.confidentiality','ro.patient-rights.disclosure'}:
            assert evaluate_predicate(requirement['applies_if'],prospective_facts)[0]=='true'


def test_verified_fact_check_rows_must_be_anchored_or_gap_explained(tmp_path):
    import shutil
    overlay=tmp_path/'overlay'; shutil.copytree(ROOT,overlay,ignore=shutil.ignore_patterns('__pycache__'))
    from datetime import date
    assert check_overlay.check_verified_row_coverage(overlay,date(2026,10,10))==[]
    delta_path=overlay/'registries/human_subjects.delta.json'
    delta=json.loads(delta_path.read_text())
    row_id='ro.patient-rights-research-consent'
    law=next(p for p in delta['profiles'] if p['profile_id']=='ro.parliament.law-46-2003.patient-rights-research')
    law['requirements']=[r for r in law['requirements'] if r['requirement_id']!='ro.patient-rights.research-consent']
    delta_path.write_text(json.dumps(delta))
    errors=check_overlay.check_verified_row_coverage(overlay,date(2026,10,10))
    assert any(row_id in error and 'not anchored' in error for error in errors)
    delta['known_gaps'].append(f'{row_id}: statutory meaning needs additional review.')
    delta_path.write_text(json.dumps(delta))
    assert check_overlay.check_verified_row_coverage(overlay,date(2026,10,10))==[]
