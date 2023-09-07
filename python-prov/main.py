import datetime

from prov.model import ProvDocument, ProvBundle, ProvAgent, ProvActivity, ProvEntity
import prov.graph

import bad_uri
import datetime_microseconds
import provn_deserializer_not_implemented
import weird_character_as_identifier
import id_with_space

from prov.model import ProvDocument
from prov.dot import prov_to_dot


def project_planning_bundle(document: ProvDocument):
    ppp_bundle = document.bundle("ProjectPlanningPhase")

    ba : ProvAgent = ppp_bundle.agent("BusinessAnalyst")
    cu : ProvAgent = ppp_bundle.agent("Customer")
    pm : ProvAgent = ppp_bundle.agent("ProjectManager")
    co : ProvAgent = ppp_bundle.agent("Company")

    rg : ProvActivity = ppp_bundle.activity("ReqGathering")
    pp : ProvActivity = ppp_bundle.activity("ProjPlanning")

    rq : ProvEntity = ppp_bundle.entity("Requirements")
    ppd : ProvEntity = ppp_bundle.entity("ProjPlanDocument")
    b : ProvEntity = ppp_bundle.entity("Bell")

    ppp_bundle.actedOnBehalfOf(ba, co)
    ppp_bundle.actedOnBehalfOf(pm, co)
    ppp_bundle.wasAssociatedWith(rg,ba)
    ppp_bundle.wasAssociatedWith(rg,cu)
    ppp_bundle.wasAssociatedWith(pp,cu)
    ppp_bundle.wasAssociatedWith(pp,pm)
    ppp_bundle.wasGeneratedBy(ppd, pp)
    ppp_bundle.wasGeneratedBy(rq, rg)
    ppp_bundle.wasStartedBy(pp, b)

def design_bundle(document : ProvDocument):
    db: ProvBundle = document.bundle("DesignPhase")
    sa: ProvAgent = db.agent("SystemArchitect")
    uidsgnrs: ProvAgent = db.agent("UIUXDesigners")
    dba: ProvAgent = db.agent("DbArchitect")
    dl: ProvAgent = db.agent("DesignLead")

    sd: ProvActivity = db.activity("SystemDesign")
    uidsgn: ProvActivity = db.activity("UIUXDesign")
    dbd: ProvActivity = db.activity("DbDesign")
    dc: ProvActivity = db.activity("DesignCoordination")

    sdd: ProvEntity = db.entity("SystemDesignDocuments")
    uia1: ProvEntity = db.entity("UIUXArtifacts1")
    uia2: ProvEntity = db.entity("UIUXArtifacts2")
    dbs: ProvEntity = db.entity("DbSchema")
    dt: ProvEntity = db.entity("DesignTools")

    rq : ProvEntity = db.entity("Requirements")
    rq.add_asserted_type("prov:Plan")

    db.wasAssociatedWith(sd,sa)
    #plan
    db.wasAssociatedWith(uidsgn,uidsgnrs,rq)
    db.wasAssociatedWith(dbd,dba)
    db.wasAssociatedWith(dc,dl)
    db.usage(uidsgn,dt)
    db.wasGeneratedBy(sdd,sd)
    db.wasGeneratedBy(uia1,uidsgn)
    db.wasGeneratedBy(dbs,dbd)
    db.wasInfluencedBy(sd,dc)
    db.wasInfluencedBy(uidsgn, dc)
    db.wasInfluencedBy(dbd, dc)
    #revision
    derivation = db.wasDerivedFrom(uia2,uia1)
    derivation.add_asserted_type("prov:Revision")

def implementation_bundle(document: ProvDocument):

    impl: ProvBundle = document.bundle("ImplementationPhase")
    sm = impl.agent("ScrumMaster")
    dev = impl.agent("Developers")
    pm = impl.agent("ProjectManager")
    devops = impl.agent("DevOpsEngineers")

    wsc = impl.activity("WritingSourceCode")
    wut = impl.activity("WritingUnitTests")
    up = impl.activity("UpdatingPipeline")

    v1 = impl.entity("Version1")
    vfs = impl.entity("VersionForSomeone")
    wv = impl.entity("WebVersion")
    mv = impl.entity("MobileVersion")
    dv = impl.entity("DesktopVersion")
    ut = impl.entity("UnitTests")
    cicd1 = impl.entity("CICDPipeline1")
    cicd2 = impl.entity("CICDPipeline2")
    pl = impl.entity("Plan")
    pl.add_asserted_type("prov:Plan")

    impl.wasAssociatedWith(wsc,dev,pl)
    impl.wasAssociatedWith(wut,dev)
    impl.wasAttributedTo(pl,sm)
    impl.wasAttributedTo(cicd1,devops)
    impl.wasGeneratedBy(v1,wsc)
    impl.wasGeneratedBy(ut, wut)
    impl.wasDerivedFrom(cicd2,cicd1)
    impl.actedOnBehalfOf(sm,pm)
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

    qal = test.agent("QALead")
    tstr = test.agent("Tester")
    at = test.agent("AutomationTester")

    tplanning = test.activity("TestPlanning")
    wt = test.activity("WritingTests")
    tr = test.activity("TestReview")

    tp = test.entity("TestPlan")
    tp.add_asserted_type("prov:Plan")
    sys = test.entity("System")
    usys = test.entity("UpdatedSystem")
    ts = test.entity("TestSuite")
    tc1 = test.entity("TestCase1")
    tc2 = test.entity("TestCase2")
    tc3 = test.entity("TestCase3")
    ts.hadMember(tc1)
    ts.hadMember(tc2)
    ts.hadMember(tc3)

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
    dm = depl.agent("DeploymentManager")
    dba = depl.agent("DBAdmin")
    sa = depl.agent("ServerAdmin")
    dt = depl.agent("DeploymentTeam")
    u = depl.agent("User")

    dplning = depl.activity("DeploymentPlanning")
    es = depl.activity("EnvironmentSetup")
    vat = depl.activity("VerificationAndTesting")
    ut = depl.activity("UserTraining")
    dex = depl.activity("DeploymentExecution")

    dplan = depl.entity("DeploymentPlan")
    ug = depl.entity("UserGuides")
    denv = depl.entity("DeploymentEnvironment")
    dr = depl.entity("DeploymentReports")
    s = depl.entity("Server")
    db = depl.entity("DB")
    os = depl.entity("OS")
    denv.hadMember(s)
    denv.hadMember(db)
    denv.hadMember(os)

    depl.wasAssociatedWith(dplning,dm)
    depl.wasAssociatedWith(es,sa)
    depl.wasAssociatedWith(es,dba)
    depl.wasAssociatedWith(vat,dt)
    depl.wasAssociatedWith(ut, dt)
    depl.wasAssociatedWith(ut,u)
    depl.wasAttributedTo(s,sa)
    depl.wasAttributedTo(db, dba)
    depl.wasAttributedTo(ug, dt)
    depl.usage(ut,ug)
    depl.usage(es,denv)
    depl.usage(dex, denv)
    depl.wasGeneratedBy(dplan,dplning)
    depl.wasGeneratedBy(dr, vat)
    depl.wasStartedBy(dex,dplan)
    depl.wasEndedBy(dex, dplan)
    depl.wasInformedBy(dex,es)


def maintenance_phase(document:ProvDocument):
    main: ProvBundle = document.bundle("MaintenancePhase")
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
    project_planning_bundle(doc)
    design_bundle(doc)
    implementation_bundle(doc)
    testing_bundle(doc)
    deployment_bundle(doc)
    maintenance_phase(doc)
    doc.serialize(r"temp.provn", format="provn")
    dot = prov_to_dot(doc)
    print(dot)
    #bad_uri.perform()
    #provn_deserializer_not_implemented.perform()
    #weird_character_as_identifier.perform()
    #id_with_space.perform()
    #datetime_microseconds.perform()