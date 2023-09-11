import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    a = document.agent("ex:a",{"prov:value":4})
    document.serialize(r"..\java-prov\prov_value.provn", format="provn")
    print(document.get_provn())