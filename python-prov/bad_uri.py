import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    ns = document.add_namespace("ex", "http://www.w3. org/ns/prov#")
    document.serialize(r"..\java-prov\bad_uri.provn", format="provn")
    print(document.get_provn())