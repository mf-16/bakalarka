import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = create_document()
    document.serialize(fr"..\..\java-prov\data\test_test_case.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\test_test_case.{format}", format=format)

    expected_document = create_document()
    print(expected_document.__eq__(document))

    document.serialize(sys.stdout, format=format, indent=2)

def create_document():
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    c = document.collection("ex:c")
    e = document.entity("ex:e")
    c.hadMember(e)
    return document