from prov.model import ProvDocument

from test_case import TestCase


class ImplicitExistenceOfProvNamespace(TestCase):

    def __init__(self):
        self.filename = "implicit_existence_of_prov_namespace"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        e = document.entity("ex:e")
        e.add_asserted_type(1)
        return document
