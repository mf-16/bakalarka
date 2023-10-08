import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.set_default_namespace("https://example.com")
    document.add_namespace("ex", "https://example.org/")
    document.entity("ex:e")
    document.activity("ex:ac")
    bundle = document.bundle("ex:b")
    bundle.entity("ex:e2")

    document.serialize(fr"..\..\java-prov\data\top_instance_namespace_bundle.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\top_instance_namespace_bundle.{format}",format=format)
    print(document.get_provn())