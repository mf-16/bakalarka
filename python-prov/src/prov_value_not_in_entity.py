import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    document.activity("ex:ac",None,None,{"prov:value":1})
    document.serialize(fr"..\..\java-prov\data\prov_value_not_in_entity.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\prov_value_not_in_entity.{format}", format=format)
    print(document.get_provn())