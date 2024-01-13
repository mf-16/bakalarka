from prov.model import ProvDocument


def perform():
    document = ProvDocument()
    document = document.deserialize("java_serialization_problems.xml", format="xml")
    document.serialize("temp.provn", format="provn")
