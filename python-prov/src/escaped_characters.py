import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
from prov.model import ProvDocument

def serialize(format):
    document = create_document()
    document.serialize(fr"..\..\java-prov\data\escaped_characters.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\escaped_characters.{format}", format=format)

    expected_document = create_document()
    print(expected_document.__eq__(document))

    document.serialize(sys.stdout, format=format, indent=2)

def create_document():
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    document.entity("ex:='(),-:;[].")
    return document
