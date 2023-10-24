import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "http://www.w3. org/ns/prov#")
    document.serialize(fr"..\..\java-prov\data\checking_uri_syntax.{format}", format=format, indent=2)
    document.serialize(sys.stdout, format=format, indent=2)

def deserialize(format):
    document = ProvDocument()
    document = document.deserialize(fr"..\data\checking_uri_syntax.{format}",format=format)
    document.serialize(sys.stdout, format=format, indent=2)

    document2 = ProvDocument()
    document2.add_namespace("ex1", "http://www.w2. org/ns/prov#")
    document2.add_namespace("ex2", "a")
    print(document2.__eq__(document))

