import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    document = ProvDocument()
    document.set_default_namespace("def")
    ns = document.add_namespace("ex ex", "https://example.org/")
    a = document.activity("ex ex:a",datetime.datetime.now())
    g = document.wasGeneratedBy(a,a)
    document.serialize(r"..\java-prov\data\invalid_records.provn", format="provn")
    print(document.get_provn())