import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = create_document()

    document.serialize(fr"..\..\java-prov\data\nonsense_prov_records.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\nonsense_prov_records.{format}", format=format)

    expected_document = create_document()
    print(expected_document.__eq__(document))

    document.serialize(sys.stdout, format=format, indent=2)


def create_document():
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    e = document.entity("ex:e")
    ac = document.activity("ex:ac")
    ag = document.agent("ex:ag")
    document.wasGeneratedBy(ag, e)
    document.usage(ag, ac)
    document.wasInformedBy(e, e)
    document.wasStartedBy(e, ag, ac)
    document.wasEndedBy(e, ag, ac)
    document.wasInvalidatedBy(ag, e)
    document.wasDerivedFrom(ac, ag, e, e, ag)
    document.wasAttributedTo(ac, ac)
    document.wasAssociatedWith(e, e)
    document.actedOnBehalfOf(e, ac)
    document.wasInfluencedBy(ag, ac)
    document.alternateOf(ag, ac)
    document.specializationOf(e, ac)
    c = document.collection("ex:c")
    c.hadMember(ag)
    c.hadMember(ac)
    return document