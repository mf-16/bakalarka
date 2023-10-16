import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    e = document.entity("ex:e")
    a = document.activity("ex:a")
    document.wasGeneratedBy(e,a)
    document.serialize(fr"..\..\java-prov\data\prov_record_without_id.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\prov_record_without_id.{format}", format=format)
    document.serialize(sys.stdout, format=format, indent=2)