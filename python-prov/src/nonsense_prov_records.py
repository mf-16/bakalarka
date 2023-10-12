import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    e = document.entity("ex:e")
    ac = document.activity("ex:ac")
    ag = document.agent("ex:ag")
    document.wasGeneratedBy(ac,e)
    document.usage(ag,ac)
    document.wasInformedBy(e,e)
    document.wasStartedBy(e,ag,ac)
    document.wasEndedBy(e,ag,ac)
    document.wasInvalidatedBy(ag,e)
    document.wasDerivedFrom(ac,ag,e,e,ag)
    document.wasAttributedTo(ac,ac)
    document.wasAssociatedWith(e,e)
    document.actedOnBehalfOf(e,ac)
    document.wasInfluencedBy(ag,ac)
    document.alternateOf(ag,ac)
    document.specializationOf(e,ac)
    c = document.collection("ex:c")
    c.hadMember(ag)
    c.hadMember(ac)


    document.serialize(fr"..\..\java-prov\data\nonsense_prov_records.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\nonsense_prov_records.{format}", format=format)
    print(document.get_provn())