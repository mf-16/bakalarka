import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
from prov.model import ProvDocument

from test_case import TestCase


class EscapedCharacters(TestCase):

    def __init__(self):
        self.filename = "escaped_characters"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.entity("ex:='(),-:;[].")
        return document
