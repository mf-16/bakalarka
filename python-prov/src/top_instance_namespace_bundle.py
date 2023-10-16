import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    document.entity("ex:e")
    document.activity("ex:ac")
    bundle = document.bundle("ex:b")
    bundle.add_namespace("ex", "https://example.com/")
    bundle.entity("ex:e2")

    document.serialize(fr"..\..\java-prov\data\top_instance_namespace_bundle.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\top_instance_namespace_bundle.{format}",format=format)
    document.serialize(sys.stdout, format=format, indent=2)