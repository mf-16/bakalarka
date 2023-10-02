import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    e = document.entity("ex:e")
    a = document.activity("ex:a")
    document.wasGeneratedBy(e,a)
    document.serialize(r"..\..\java-prov\data\prov_relation_without_id.json", format="json", indent=2)
    print(document.get_provn())