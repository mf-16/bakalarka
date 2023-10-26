import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = create_document()

    document.serialize(fr"..\..\java-prov\data\space_in_prefix.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\space_in_prefix.{format}",format=format)

    expected_document = create_document()
    print(expected_document.__eq__(document))

    document.serialize(sys.stdout, format=format, indent=2)

def create_document():
    document = ProvDocument()
    ns = document.add_namespace("ex ex", "https://example.org/")
    ns = document.add_namespace("ex", "https://example.com/")
    document.entity("ex ex:e")
    document.activity("ex:a")
    return document