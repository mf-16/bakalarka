import os
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
        file_path = os.path.join('..', '..', 'java-prov', 'data', f'{self.filename}.{format_type}')
        document.serialize(file_path, format=format_type, indent=2)
        document.serialize(sys.stdout, format=format_type, indent=2)

    def deserialize(self, format_type):
        document = ProvDocument()
        file_path = os.path.join('..', 'data', f'{self.filename}.{format_type}')
        document = document.deserialize(file_path, format=format_type)

        expected_document = self.create_document()
        print(expected_document.__eq__(document))
        print("----------")
        document.serialize(sys.stdout, format=format_type, indent=2)
