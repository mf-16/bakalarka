import prov.dot
from prov.model import ProvDocument
import prov.graph

import bad_uri
import provn_deserializer_not_implemented
from prov.model import ProvDocument

def perform():
    document = ProvDocument()
    document.set_default_namespace("default")
    document.add_namespace("ex","https://example.org/")
    document.entity(".")
    document.serialize(r"..\java-prov\weird_char_as_id.provn", format="provn")
    print(document.get_provn())