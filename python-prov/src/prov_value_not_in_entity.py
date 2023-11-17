import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class ProvValueNotInEntity(TestCase):

    def __init__(self):
        self.filename = "prov_value_not_in_entity"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.activity("ex:ac", None, None, {"prov:value": 1})
        return document