import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class DefaultNamespace(TestCase):

    def __init__(self):
        self.filename = "default_namespace"

    def create_document(self):
        document = ProvDocument()
        document.set_default_namespace("https://default.org/")
        document.add_namespace("ex", "https://example.org/")
        document.entity("ex:e")
        return document

