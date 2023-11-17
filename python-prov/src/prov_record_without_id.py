import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class ProvRecordWithoutId(TestCase):

    def __init__(self):
        self.filename = "prov_record_without_id"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        e = document.entity("ex:e")
        a = document.activity("ex:a")
        document.wasGeneratedBy(e, a)
        return document