import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class NonsenseProvRecords(TestCase):

    def __init__(self):
        self.filename = "nonsense_prov_records"

    def create_document(self):
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