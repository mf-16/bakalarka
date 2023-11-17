import datetime
import sys

import prov.dot
from prov.model import ProvDocument
import prov.graph

import checking_uri_syntax
import provn_deserializer_not_implemented
import escaped_characters
import local_part_of_id_with_space

from prov.model import ProvDocument

from test_case import TestCase


class LossOfTimezone(TestCase):

    def __init__(self):
        self.filename = "loss_of_timezone"

    def create_document(self):
        document = ProvDocument()
        document.add_namespace("ex", "https://example.org/")
        document.activity("ex:a", "2023-09-08T14:12:45.109-04:00", "2023-09-08T14:12:45.109+04:00")
        return document