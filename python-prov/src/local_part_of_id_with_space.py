import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
import escaped_characters

from prov.model import ProvDocument


def serialize(format):
    document = ProvDocument()
    document.entity("prov:a b c")
    document.serialize(fr"..\..\java-prov\data\local_part_of_id_with_space.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\local_part_of_id_with_space.{format}", format=format)
    print(document.get_provn())