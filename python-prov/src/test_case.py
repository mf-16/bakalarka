import sys
from abc import ABC, abstractmethod

from prov.model import ProvDocument


class TestCase(ABC):
    filename = ""

    @abstractmethod
    def create_document(self):
        pass

    def serialize(self, format_type):
        document = self.create_document()
        document.serialize(fr"..\..\java-prov\data\{self.filename}.{format_type}", format=format_type, indent=2)
        document.serialize(sys.stdout, format=format_type, indent=2)

    def deserialize(self, format_type):
        document = ProvDocument()
        document = document.deserialize(fr"..\data\{self.filename}.{format_type}", format=format_type)

        expected_document = self.create_document()
        print(expected_document.__eq__(document))

        document.serialize(sys.stdout, format=format_type, indent=2)
