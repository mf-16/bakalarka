import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    ns = document.add_namespace("ex", "https://example.org/")
    a = document.activity("ex:a")
    document.wasGeneratedBy(a,a,datetime.datetime.now())
    document.serialize(r"..\java-prov\invalid_records.provn", format="provn")
    print(document.get_provn())