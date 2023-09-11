import datetime

from prov.model import ProvDocument, ProvBundle, ProvAgent, ProvActivity, ProvEntity
import prov.graph

import bad_uri
import datetime_microseconds
import invalid_records
import prov_value
import provn_deserializer_not_implemented
import weird_character_as_identifier
import id_with_space

from prov.model import ProvDocument
from prov.dot import prov_to_dot


def project_planning_bundle(document: ProvDocument):
    ppp_bundle = document.bundle("ProjectPlanningPhase")
    newbun = document.entity("ProjectPlanningPhase")
    newbun.add_asserted_type("prov:Bundle")


    ba = ppp_bundle.agent("BusinessAnalyst")
    cu = ppp_bundle.agent("Customer")
    pm = ppp_bundle.agent("ProjectManager")
    co = ppp_bundle.agent("Company",{"prov:location":"Brno, Czech Republic"})
    co.add_asserted_type("prov:Organization")

    rg = ppp_bundle.activity("ReqGathering")
    pp = ppp_bundle.activity("ProjPlanning")

    rq = ppp_bundle.entity("Requirements",{"prov:value": "The system must allow users to create a new account."})
    rq.add_attributes({"prov:value":"The user interface should be intuitive and easy to navigate."})
    rq.add_attributes({"prov:value":"User data must be securely stored and encrypted."})
    ppd = ppp_bundle.entity("ProjPlanDocument")

    ppp_bundle.actedOnBehalfOf(ba, co)
    ppp_bundle.actedOnBehalfOf(pm, co)
    ppp_bundle.wasAssociatedWith(rg,ba)
    ppp_bundle.wasAssociatedWith(rg,cu)
    ppp_bundle.wasAssociatedWith(pp,cu)
    ppp_bundle.wasAssociatedWith(pp,pm)
    ppp_bundle.wasGeneratedBy(ppd, pp)
    ppp_bundle.wasGeneratedBy(rq, rg)

def design_bundle(document : ProvDocument):
    db: ProvBundle = document.bundle("DesignPhase")
    newbun = document.entity("DesignPhase")
    newbun.add_asserted_type("prov:Bundle")
    uidsgnrs: ProvAgent = db.agent("UIUXDesigners")
    dba: ProvAgent = db.agent("DbArchitect")
    dl: ProvAgent = db.agent("DesignLead")

    uidsgn: ProvActivity = db.activity("UIUXDesign")
    dbd: ProvActivity = db.activity("DbDesign")
    dc: ProvActivity = db.activity("DesignCoordination")

    uia1: ProvEntity = db.entity("UIUXArtifacts1")
    uia2: ProvEntity = db.entity("UIUXArtifacts2")
    dbs: ProvEntity = db.entity("DbSchema")
    dt: ProvEntity = db.entity("DesignTools",{"prov:label": "Tools like Adobe XD or Figma"})


    rq : ProvEntity = db.entity("Requirements")
    rq.add_asserted_type("prov:Plan")

    #plan
    db.wasAssociatedWith(uidsgn,uidsgnrs,rq)
    db.wasAssociatedWith(dbd,dba)
    db.wasAssociatedWith(dc,dl)
    db.usage(uidsgn,dt)
    db.wasGeneratedBy(uia1,uidsgn)
    db.wasGeneratedBy(dbs,dbd)
    db.wasInformedBy(uidsgn, dc)
    db.wasInformedBy(dbd, dc)
    #revision
    derivation = db.wasDerivedFrom(uia2,uia1)
    derivation.add_asserted_type("prov:Revision")

def implementation_bundle(document: ProvDocument):

    impl: ProvBundle = document.bundle("ImplementationPhase")
    newbun = document.entity("ImplementationPhase")
    newbun.add_asserted_type("prov:Bundle")
    sm = impl.agent("ScrumMaster")
    dev = impl.agent("Developers")
    devops = impl.agent("DevOpsEngineers")

    wsc = impl.activity("WritingSourceCode")
    up = impl.activity("UpdatingPipeline")

    v1 = impl.entity("Version1")
    v1.add_asserted_type("prov:Collection")
    vfs = impl.entity("VersionForSomeone")
    wv = impl.entity("WebVersion")
    mv = impl.entity("MobileVersion")
    dv = impl.entity("DesktopVersion")
    cicd1 = impl.entity("CICDPipeline1")
    cicd2 = impl.entity("CICDPipeline2")
    pl = impl.entity("Plan")
    pl.add_asserted_type("prov:Plan")

    impl.wasAssociatedWith(wsc,dev,pl,None,{"prov:role":"dct:contributor"})
    impl.wasAttributedTo(pl,sm)
    impl.wasAttributedTo(cicd1,devops)
    impl.wasGeneratedBy(v1,wsc)
    impl.wasDerivedFrom(cicd2,cicd1)
    impl.wasInvalidatedBy(cicd1,up)
    v1.hadMember(dv)
    v1.hadMember(mv)
    v1.hadMember(wv)
    impl.specialization(vfs,v1)
    impl.alternate(wv,dv)
    impl.alternate(dv, mv)
    impl.alternate(mv, wv)


def testing_bundle(document: ProvDocument):
    test: ProvBundle = document.bundle("TestingPhase")
    newbun = document.entity("TestingPhase")
    newbun.add_asserted_type("prov:Bundle")

    qal = test.agent("QALead")
    tstr = test.agent("Tester",{"prov:role":"Manual Tester"})
    at = test.agent("AutomationTester",{"prov:role":"Automation Test Engineer"})

    tplanning = test.activity("TestPlanning")
    wt = test.activity("WritingTests")
    tr = test.activity("TestReview")

    tp = test.entity("TestPlan")
    tp.add_asserted_type("prov:Plan")
    sys = test.entity("System")
    usys = test.entity("UpdatedSystem")
    ts = test.entity("TestSuite")

    test.wasAssociatedWith(tplanning,qal)
    test.wasAssociatedWith(wt,tstr,tp)
    test.wasAssociatedWith(wt, at,tp)
    test.wasAssociatedWith(tr, qal)
    test.wasAttributedTo(tp,qal)
    test.wasGeneratedBy(tp,tplanning)
    test.wasGeneratedBy(ts,wt)
    test.wasGeneratedBy(usys,tr)
    test.wasDerivedFrom(usys,sys)
    test.usage(wt,sys)
    test.wasInformedBy(tr,wt)


def deployment_bundle(document: ProvDocument):
    depl: ProvBundle = document.bundle("DeploymentPhase")
    newbun = document.entity("DeploymentPhase")
    newbun.add_asserted_type("prov:Bundle")
    dm = depl.agent("DeploymentManager")
    dba = depl.agent("DBAdmin")
    sa = depl.agent("ServerAdmin")
    dt = depl.agent("DeploymentTeam")
    u = depl.agent("User")

    dplning = depl.activity("DeploymentPlanning")
    es = depl.activity("EnvironmentSetup")
    ut = depl.activity("UserTraining")
    dex = depl.activity("DeploymentExecution")

    dplan = depl.entity("DeploymentPlan")
    ug = depl.entity("UserGuides",{"dct:description":"User guides simplify software adoption with essential instructions."})
    denv = depl.entity("DeploymentEnvironment")
    denv.add_asserted_type("prov:Collection")
    s = depl.entity("Server")
    db = depl.entity("DB")
    os = depl.entity("OS")
    denv.hadMember(s)
    denv.hadMember(db)
    denv.hadMember(os)

    depl.wasAssociatedWith(dplning,dm)
    depl.wasAssociatedWith(es,sa)
    depl.wasAssociatedWith(es,dba)
    depl.wasAssociatedWith(ut, dt)
    depl.wasAssociatedWith(ut,u)
    depl.wasAttributedTo(s,sa)
    depl.wasAttributedTo(db, dba)
    depl.wasAttributedTo(ug, dt)
    depl.usage(ut,ug)
    depl.usage(es,denv)
    depl.usage(dex, denv)
    depl.wasGeneratedBy(dplan,dplning)
    depl.wasStartedBy(dex,dplan)
    depl.wasEndedBy(dex, dplan)
    depl.wasInformedBy(dex,es)


def maintenance_phase(document:ProvDocument):
    main: ProvBundle = document.bundle("MaintenancePhase")
    newbun = document.entity("MaintenancePhase")
    newbun.add_asserted_type("prov:Bundle")
    dt = main.agent("DeveloperTeam")
    ld = main.agent("LeadDeveloper")
    u = main.agent("User")
    st = main.agent("SupportTeam")

    resi = main.activity("ResolvingIssues")
    repi = main.activity("ReportingIssues")
    ud = main.activity("UpdateDeployment")
    gi = main.activity("GatheringIssues")

    p = main.entity("Patch")
    uv = main.entity("UpdatedVersion")
    ov = main.entity("OldVersion")
    ir = main.entity("IssueReport")

    main.wasAssociatedWith(resi,dt)
    main.wasAssociatedWith(ud,ld)
    main.wasAssociatedWith(repi,u)
    main.wasAssociatedWith(gi,st)
    main.wasGeneratedBy(ir,gi)
    main.wasGeneratedBy(p,resi)
    main.usage(ud,uv)
    main.usage(resi,ir)
    main.wasInformedBy(gi,repi)
    main.wasInvalidatedBy(ov,ud)
    main.wasInfluencedBy(uv,p)
    main.wasAttributedTo(ir,st)




if __name__ == "__main__":
    doc = ProvDocument()
    doc.set_default_namespace("https://example.org/")
    doc.add_namespace("dct","http://purl.org/dc/terms/")
    # project_planning_bundle(doc)
    # design_bundle(doc)
    # implementation_bundle(doc)
    # testing_bundle(doc)
    # deployment_bundle(doc)
    # maintenance_phase(doc)
    rq = doc.entity("Requirements", {"prov:value": "prov:Collection"})
    rq.add_attributes({"prov:value": "prov:Person"})
    doc.serialize(r"..\java-prov\temp.provn", format="provn")
    print(doc.get_provn())
    # dot = prov_to_dot(doc)
    # print(dot)
    #bad_uri.perform()
    #provn_deserializer_not_implemented.perform()
    #weird_character_as_identifier.perform()
    #id_with_space.perform()
    #datetime_microseconds.perform()
    #invalid_records.perform()
    #prov_value.perform()