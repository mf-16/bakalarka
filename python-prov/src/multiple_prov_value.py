import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class MultipleProvValue(TestCase):

    def __init__(self):
        self.filename = "multiple_prov_value"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        e = document.entity("ex:e", {"prov:value": 1})
        e.add_attributes({"prov:value": 2})
        e.add_attributes({"prov:value": 3})
        return document