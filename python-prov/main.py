import datetime

import prov.dot
from prov.model import ProvDocument, ProvBundle, ProvAgent, ProvActivity, ProvEntity
import prov.graph

import bad_uri
import datetime_microseconds
import provn_deserializer_not_implemented
import weird_character_as_identifier
import id_with_space

from prov.model import ProvDocument
from prov.dot import prov_to_dot


def project_planning_bundle(document :ProvDocument):
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
    db: ProvBundle = document.bundle("DesignBundle")
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

    impl: ProvBundle = document.bundle("ImplementationBundle")
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












if __name__ == "__main__":
    document = ProvDocument()
    document.set_default_namespace("https://example.org/")
    project_planning_bundle(document)
    design_bundle(document)
    implementation_bundle(document)
    document.serialize(r"C:\Users\Matúš\PROV-JAVA\test\temp.provn", format="provn")
    dot = prov_to_dot(document)
    print(dot)

#bad_uri.perform()
#provn_deserializer_not_implemented.perform()
#weird_character_as_identifier.perform()
#id_with_space.perform()
#datetime_microseconds.perform()