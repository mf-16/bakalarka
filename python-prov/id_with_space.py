import prov.dot
from prov.model import ProvDocument
import prov.graph

import bad_uri
import provn_deserializer_not_implemented
import weird_character_as_identifier

from prov.model import ProvDocument


def perform():
    document = ProvDocument()
    document.entity("prov:a b c")
    document.serialize(r"..\java-prov\id_with_space.provn", format="provn")
    print(document.get_provn())