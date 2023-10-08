import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
from prov.model import ProvDocument

def serialize(format):
    document = ProvDocument()
    document.add_namespace("ex","https://example.org/")
    document.entity("ex:='(),-:;[].")
    document.serialize(fr"..\..\java-prov\data\escaped_characters.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.serialize(fr"..\data\escaped_characters.{format}", format=format)
    print(document.get_provn())