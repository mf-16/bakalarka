from prov.model import ProvDocument

from test_case import TestCase


class LossOfMicroseconds(TestCase):

    def __init__(self):
        self.filename = "loss_of_microseconds"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.activity("ex:a", "2023-09-08T14:12:45.10931231236545213876",
                          "2023-09-08T14:12:45.109321321312321432523")
        return document
