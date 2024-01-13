from prov.model import ProvDocument


def perform():
    doc_from_provn = ProvDocument.deserialize('provn_file.provn', format='provn')
