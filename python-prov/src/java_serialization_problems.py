import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    document = document.deserialize("java_serialization_problems.xml",format="xml")
    document.serialize("temp.provn",format="provn")