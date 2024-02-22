from prov.model import ProvDocument

from test_case import TestCase


class IdentifierWithoutPrefix(TestCase):

    def __init__(self):
        self.filename = "identifier_without_prefix"

    def create_document(self):
        document = ProvDocument()
        document.set_default_namespace("https://default.org/")
        document.entity("e")
        return document
