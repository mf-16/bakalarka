from prov.model import ProvDocument

from test_case import TestCase


class GenericTestCase(TestCase):

    def __init__(self):
        self.filename = "generic_test_case"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        rw = document.agent("ex:rw")
        mf = document.agent("ex:mf")
        wr = document.activity("ex:writing")
        document.delegation(mf,rw,wr)
        return document
