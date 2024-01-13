from prov.model import ProvDocument

from test_case import TestCase


class SpaceInPrefix(TestCase):

    def __init__(self):
        self.filename = "space_in_prefix"

    def create_document(self):
        document = ProvDocument()
        ns = document.add_namespace("ex ex", "https://example.org/")
        ns = document.add_namespace("ex", "https://example.com/")
        document.entity("ex ex:e")
        document.activity("ex:a")
        return document
