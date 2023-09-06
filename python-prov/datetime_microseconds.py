import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

import bad_uri
import provn_deserializer_not_implemented
import weird_character_as_identifier
import id_with_space

from prov.model import ProvDocument

def perform():
    document = ProvDocument()
    document.activity("prov:a","2023-09-02T09:43:22.6350551221",datetime.datetime.now())
    document.serialize(r"..\java-prov\datetime_microseconds.provn", format="provn")
    print(document.get_provn())