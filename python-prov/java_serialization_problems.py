import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    doc = document.deserialize("java_serialization_problems.xml",format="xml")
    doc.serialize("temp.provn",format="provn")