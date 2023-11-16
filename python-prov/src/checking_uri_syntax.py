import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

from test_case import TestCase


class CheckingUriSyntax(TestCase):
    def __init__(self):
        self.filename = "checking_uri_syntax"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "http://www.w3. org/ns/prov#")
        document.entity("ex:e")
        return document


# def serialize(format):
#     document = create_document()
#     document.serialize(fr"..\..\java-prov\data\checking_uri_syntax.{format}", format=format, indent=2)
#     document.serialize(sys.stdout, format=format, indent=2)
#
# def deserialize(format):
#     document = ProvDocument()
#     document = document.deserialize(fr"..\data\checking_uri_syntax.{format}",format=format)
#
#     expected_document = create_document()
#     print(expected_document.__eq__(document))
#
#     document.serialize(sys.stdout, format=format, indent=2)
#
# def create_document():
#     document = ProvDocument()
#     document.add_namespace("ex", "http://www.w3. org/ns/prov#")
#     document.entity("ex:e")
#     return document

