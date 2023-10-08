import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    e = document.entity("ex:e",{"prov:value":1})
    e.add_attributes({"prov:value":2})
    e.add_attributes({"prov:value":3})
    document.serialize(fr"..\..\java-prov\data\multiple_prov_value.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\multiple_prov_value.{format}", format=format)
    print(document.get_provn())