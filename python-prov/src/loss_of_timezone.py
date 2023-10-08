import datetime

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
import escaped_characters
import local_part_of_id_with_space

from prov.model import ProvDocument

def serialize(format):
    document = ProvDocument()
    document.add_namespace("ex","https://example.org/")
    document.activity("ex:a","2023-09-08T14:12:45.109-04:00","2023-09-08T14:12:45.109+04:00")
    document.serialize(fr"..\..\java-prov\data\loss_of_timezone.{format}", format=format, indent=2)
    print(document.get_provn())

def deserialize(format):
    document = ProvDocument()
    document.deserialize(fr"..\data\loss_of_timezone.{format}", format=format)
    print(document.get_provn())