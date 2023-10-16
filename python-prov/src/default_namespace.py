import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    document.set_default_namespace("https://default.org/")
    ns = document.add_namespace("ex", "https://example.org/")
    a = document.entity("ex:e")
    document.serialize(fr"../../java-prov/data/default_namespace.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"../data/default_namespace.{format}",format=format)
    document.serialize(sys.stdout, format=format, indent=2)
