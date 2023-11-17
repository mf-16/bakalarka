import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
import escaped_characters

from prov.model import ProvDocument

from test_case import TestCase


class LocalPartOfIdWithSpace(TestCase):

    def __init__(self):
        self.filename = "local_part_of_id_with_space"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.entity("ex:a b c")
        return document


