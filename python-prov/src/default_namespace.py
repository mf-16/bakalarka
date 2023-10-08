import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    document.set_default_namespace("https://default.org/")
    ns = document.add_namespace("ex", "https://example.org/")
    a = document.entity("ex:e")
    document.serialize(fr"../../java-prov/data/default_namespace.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    doc = document.deserialize(fr"../data/default_namespace.{format}",format=format)
    doc.serialize("temp.provn",format="provn")
    print(doc.get_provn())