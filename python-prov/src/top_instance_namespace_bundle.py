import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class TopInstanceNamespaceBundle(TestCase):

    def __init__(self):
        self.filename = "top_instance_namespace_bundle"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.entity("ex:e")
        document.activity("ex:ac")
        bundle = document.bundle("ex:b")
        bundle.add_namespace("ex", "https://example.com/")
        bundle.entity("ex:e2")
        return document
