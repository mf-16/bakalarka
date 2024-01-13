from prov.model import ProvDocument

from test_case import TestCase


class LossOfTimezone(TestCase):

    def __init__(self):
        self.filename = "loss_of_timezone"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.activity("ex:a", "2023-09-08T14:12:45.109-04:00", "2023-09-08T14:12:45.109+04:00")
        return document
