from prov.model import ProvDocument

from test_case import TestCase


class CheckingUriSyntax(TestCase):
    def __init__(self):
        self.filename = "checking_uri_syntax"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "http://www.w3. org/ns/prov#")
        document.entity("ex:e")
        return document
