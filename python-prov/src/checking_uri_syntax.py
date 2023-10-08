import prov.dot
from prov.model import ProvDocument
import prov.graph

def serialize(format):
    document = ProvDocument()
    ns = document.add_namespace("ex", "http://www.w3. org/ns/prov#")
    document.serialize(fr"..\..\java-prov\data\checking_uri_syntax.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\checking_uri_syntax.{format}",format=format)
    print(document.get_provn())