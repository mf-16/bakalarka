import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
import escaped_characters

from prov.model import ProvDocument


def serialize(format):
    document = create_document()
    document.serialize(fr"..\..\java-prov\data\local_part_of_id_with_space.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\local_part_of_id_with_space.{format}", format=format)

    expected_document = create_document()
    print(expected_document.__eq__(document))

    document.serialize(sys.stdout, format=format, indent=2)

def create_document():
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    document.entity("ex:a b c")
    return document
