import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class TestTestCase(TestCase):

    def __init__(self):
        self.filename = "test_test_case"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        c = document.collection("ex:c")
        e = document.entity("ex:e")
        c.hadMember(e)
        return document
