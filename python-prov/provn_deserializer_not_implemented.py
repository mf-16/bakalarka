import prov.dot
from prov.model import ProvDocument
import prov.graph

def perform():
    doc_from_provn = ProvDocument.deserialize('provn_file.provn', format='provn')