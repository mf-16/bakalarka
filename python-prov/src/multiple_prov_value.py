import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    document.add_namespace("prov", "http://www.w3.org/ns/prov#")
    e = document.entity("ex:e",{"prov:value":1})
    e.add_attributes({"prov:value":2})
    e.add_attributes({"prov:value":3})
    document.serialize(fr"..\..\java-prov\data\multiple_prov_value.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\multiple_prov_value.{format}", format=format)
    document.serialize(sys.stdout, format=format, indent=2)
