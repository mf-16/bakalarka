import datetime

from prov.model import ProvDocument, ProvBundle, ProvAgent, ProvActivity, ProvEntity
import prov.graph

import bad_uri
import datetime_microseconds
import invalid_records
import java_serialization_problems
import prov_value
import provn_deserializer_not_implemented
import weird_character_as_identifier
import id_with_space
import create_main_document
import json_default_namespace
import prov_relation_without_id

from prov.model import ProvDocument
from prov.identifier import *
from prov.dot import prov_to_dot
from prov.graph import prov_to_graph



def project_planning_bundle(bundle: ProvBundle):
    ba = bundle.agent("BusinessAnalyst")
    cu = bundle.agent("Customer")
    pm = bundle.agent("ProjectManager")
    co = bundle.agent("Company",{"prov:location":"Brno, Czech Republic"})
    co.add_asserted_type("prov:Organization")

    rg = bundle.activity("ReqGathering",None,"2022-03-06T10:30:00")
    pp = bundle.activity("ProjPlanning","2021-12-06T09:00:00")

    rq = bundle.entity("Requirements")
    ppd = bundle.entity("ProjPlanDocument")

    bundle.actedOnBehalfOf(ba, co)
    bundle.actedOnBehalfOf(pm, co)
    bundle.wasAssociatedWith(rg,ba)
    bundle.wasAssociatedWith(rg,cu)
    bundle.wasAssociatedWith(pp,cu)
    bundle.wasAssociatedWith(pp,pm)
    bundle.wasGeneratedBy(ppd, pp)
    bundle.wasGeneratedBy(rq, rg)

def design_bundle(bundle : ProvBundle):
    uidsgnrs: ProvAgent = bundle.agent("UIUXDesigners")
    dba: ProvAgent = bundle.agent("DbArchitect")
    dl: ProvAgent = bundle.agent("DesignLead")

    uidsgn: ProvActivity = bundle.activity("UIUXDesign")
    dbd: ProvActivity = bundle.activity("DbDesign")
    dc: ProvActivity = bundle.activity("DesignCoordination")

    uia1: ProvEntity = bundle.entity("UIUXArtifacts1")
    uia2: ProvEntity = bundle.entity("UIUXArtifacts2")
    dbs: ProvEntity = bundle.entity("DbSchema")
    dt: ProvEntity = bundle.entity("DesignTools",{"prov:label": "Tools like Adobe XD or Figma"})


    rq : ProvEntity = bundle.entity("Requirements")
    rq.add_asserted_type("prov:Plan")

    #plan
    bundle.wasAssociatedWith(uidsgn,uidsgnrs,rq)
    bundle.wasAssociatedWith(dbd,dba)
    bundle.wasAssociatedWith(dc,dl)
    bundle.usage(uidsgn,dt,"2022-04-01T08:00:00")
    bundle.wasGeneratedBy(uia1,uidsgn)
    bundle.wasGeneratedBy(dbs,dbd)
    bundle.wasInformedBy(uidsgn, dc)
    bundle.wasInformedBy(dbd, dc)
    #revision
    derivation = bundle.wasDerivedFrom(uia2,uia1)
    derivation.add_asserted_type("prov:Revision")

def implementation_bundle(bundle: ProvBundle):
    sm = bundle.agent("ScrumMaster")
    dev = bundle.agent("Developers")
    devops = bundle.agent("DevOpsEngineers",other_attributes={"prov:type":'prov:SoftwareAgent'})

    wsc = bundle.activity("WritingSourceCode")
    up = bundle.activity("UpdatingPipeline")

    v1 = bundle.entity("Version1")
    v1.add_asserted_type("prov:Collection")
    vfs = bundle.entity("VersionForSomeone")
    wv = bundle.entity("WebVersion")
    mv = bundle.entity("MobileVersion")
    dv = bundle.entity("DesktopVersion")
    cicd1 = bundle.entity("CICDPipeline1")
    cicd2 = bundle.entity("CICDPipeline2")
    pl = bundle.entity("Plan")
    pl.add_asserted_type("prov:Plan")

    bundle.wasGeneratedBy(pl,None,"2022-06-01T19:20:00")
    bundle.wasAssociatedWith(wsc,dev,pl,None,{"prov:role":"dct:contributor"})
    bundle.wasAttributedTo(pl,sm)
    bundle.wasAttributedTo(cicd1,devops)
    bundle.wasGeneratedBy(v1,wsc)
    bundle.wasDerivedFrom(cicd2,cicd1)
    bundle.wasInvalidatedBy(cicd1,up)
    v1.hadMember(dv)
    v1.hadMember(mv)
    v1.hadMember(wv)
    bundle.specialization(vfs,v1)
    bundle.alternate(wv,dv)
    bundle.alternate(dv, mv)
    bundle.alternate(mv, wv)


def testing_bundle(bundle: ProvBundle):
    qal = bundle.agent("QALead")
    tstr = bundle.agent("Tester")
    at = bundle.agent("AutomationTester")

    tplanning = bundle.activity("TestPlanning","2022-11-01T10:30:00","2022-11-10T10:30:00",other_attributes={"prov:location":"Conference Room, Company"})
    wt = bundle.activity("WritingTests")
    tr = bundle.activity("TestReview")

    tp = bundle.entity("TestPlan")
    tp.add_asserted_type("prov:Plan")
    sys = bundle.entity("System")
    usys = bundle.entity("UpdatedSystem")
    ts = bundle.entity("TestSuite")

    bundle.wasAssociatedWith(tplanning,qal)
    bundle.wasAssociatedWith(wt,tstr,tp,other_attributes={"prov:role":"Manual Tester"})
    bundle.wasAssociatedWith(wt, at,tp,other_attributes={"prov:role":"Automation Test Engineer"})
    bundle.wasAssociatedWith(tr, qal)
    bundle.wasAttributedTo(tp,qal)
    bundle.wasGeneratedBy(tp,tplanning)
    bundle.wasGeneratedBy(ts,wt,"2022-12-13T20:01:00")
    bundle.wasGeneratedBy(usys,tr)
    bundle.wasDerivedFrom(usys,sys)
    bundle.usage(wt,sys)
    bundle.wasInformedBy(tr,wt)


def deployment_bundle(bundle: ProvBundle):
    dm = bundle.agent("DeploymentManager")
    dba = bundle.agent("DBAdmin")
    sa = bundle.agent("ServerAdmin")
    dt = bundle.agent("DeploymentTeam")
    u = bundle.agent("User")

    dplning = bundle.activity("DeploymentPlanning")
    es = bundle.activity("EnvironmentSetup")
    ut = bundle.activity("UserTraining")
    dex = bundle.activity("DeploymentExecution")

    dplan = bundle.entity("DeploymentPlan")
    ug = bundle.entity("UserGuides",{"dct:description":"User guides simplify software adoption with essential instructions."})
    denv = bundle.entity("DeploymentEnvironment")
    denv.add_asserted_type("prov:Collection")
    s = bundle.entity("Server")
    db = bundle.entity("DB")
    os = bundle.entity("OS")
    denv.hadMember(s)
    denv.hadMember(db)
    denv.hadMember(os)

    bundle.wasAssociatedWith(dplning,dm)
    bundle.wasAssociatedWith(es,sa)
    bundle.wasAssociatedWith(es,dba)
    bundle.wasAssociatedWith(ut, dt)
    bundle.wasAssociatedWith(ut,u)
    bundle.wasAttributedTo(s,sa)
    bundle.wasAttributedTo(db, dba)
    bundle.wasAttributedTo(ug, dt,other_attributes={"prov:label" : "responsible for writing user guides"})
    bundle.usage(ut,ug)
    bundle.usage(es,denv)
    bundle.usage(dex, denv)
    bundle.wasGeneratedBy(dplan,dplning)
    bundle.wasStartedBy(dex,dplan)
    bundle.wasEndedBy(dex, dplan)
    bundle.wasInformedBy(dex,es)


def maintenance_phase(bundle : ProvBundle):
    dt = bundle.agent("DeveloperTeam")
    ld = bundle.agent("LeadDeveloper")
    u = bundle.agent("User")
    st = bundle.agent("SupportTeam")

    resi = bundle.activity("ResolvingIssues")
    repi = bundle.activity("ReportingIssues")
    ud = bundle.activity("UpdateDeployment")
    gi = bundle.activity("GatheringIssues")

    p = bundle.entity("Patch")
    uv = bundle.entity("UpdatedVersion",{"prov:value":"1.1.3"})
    ov = bundle.entity("OldVersion",{"prov:value":"1.1.2"})
    ir = bundle.entity("IssueReport")

    bundle.wasAssociatedWith(resi,dt)
    bundle.wasAssociatedWith(ud,ld)
    bundle.wasAssociatedWith(repi,u)
    bundle.wasAssociatedWith(gi,st)
    bundle.wasGeneratedBy(ir,gi)
    bundle.wasGeneratedBy(p,resi)
    bundle.usage(ud,uv)
    bundle.usage(resi,ir)
    bundle.wasInformedBy(gi,repi)
    bundle.wasInvalidatedBy(ov,ud)
    bundle.wasInfluencedBy(uv,p)
    bundle.wasAttributedTo(ir,st)

def create_document(doc):
    doc.set_default_namespace("https://example.org/")
    doc.add_namespace("dct", "http://purl.org/dc/terms/")
    # bundles
    ppb: ProvBundle = doc.bundle("ProjectPlanningPhase")
    bun1 = doc.entity("ProjectPlanningPhase")
    bun1.add_asserted_type("prov:Bundle")

    dsgb: ProvBundle = doc.bundle("DesignPhase")
    bun2 = doc.entity("DesignPhase")
    bun2.add_asserted_type("prov:Bundle")

    ib: ProvBundle = doc.bundle("ImplementationPhase")
    bun3 = doc.entity("ImplementationPhase")
    bun3.add_asserted_type("prov:Bundle")

    tb: ProvBundle = doc.bundle("TestingPhase")
    bun4 = doc.entity("TestingPhase")
    bun4.add_asserted_type("prov:Bundle")

    depb: ProvBundle = doc.bundle("DeploymentPhase")
    bun5 = doc.entity("DeploymentPhase")
    bun5.add_asserted_type("prov:Bundle")

    mb: ProvBundle = doc.bundle("MaintenancePhase")
    bun6 = doc.entity("MaintenancePhase")
    bun6.add_asserted_type("prov:Bundle")

    mf = doc.agent("MatusFormanek")
    doc.wasAttributedTo(bun1,mf)
    doc.wasAttributedTo(bun2, mf)
    doc.wasAttributedTo(bun3, mf)
    doc.wasAttributedTo(bun4, mf)
    doc.wasAttributedTo(bun5, mf)
    doc.wasAttributedTo(bun6, mf)

    project_planning_bundle(ppb)
    design_bundle(dsgb)
    implementation_bundle(ib)
    testing_bundle(tb)
    deployment_bundle(depb)
    maintenance_phase(mb)


if __name__ == "__main__":
    doc = ProvDocument()
    # doc = doc.deserialize("../data/temp.json")
    # print(doc.get_provn())
    doc.set_default_namespace("https://example.com")
    doc.add_namespace("ex","https://example.org")
    e = doc.entity("ex:e")
    ac = doc.activity("ex:ac")
    doc.wasGeneratedBy(e,ac)

    doc.serialize("../data/temp.rdf",format="rdf")

    # b1 = doc.bundle("b1")
    # b1.entity("ex:1")
    # b2 = doc.bundle("ex:b2")
    # b2.set_default_namespace("https://example.com")
    # b2.entity("2")
    # b3 = doc.bundle("ex:b3")
    # b3.add_namespace("ok", "https://example.org")
    # b3.add_namespace("ex", "https://example.org")
    # b3.entity("ok:3")
    # doc.serialize(r"../../java-prov/data/temp.json", format="json",indent=2)
    # print(doc.get_provn())


    #bad_uri.perform()
    #provn_deserializer_not_implemented.perform()
    #weird_character_as_identifier.perform()
    #id_with_space.perform()
    #datetime_microseconds.perform()
    #invalid_records.perform()
    #prov_value.perform()
    #java_serialization_problems.perform()
    #create_main_document.perform()
    #json_default_namespace.perform()
    #prov_relation_without_id.perform()