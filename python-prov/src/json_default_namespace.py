import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    doc = document.deserialize(r"../data/json_default_namespace.json",format="json")
    doc.serialize("temp.provn",format="provn")
    print(doc.get_provn())