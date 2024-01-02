import importlib
import json
import os
import sys
import checking_uri_syntax
from prov.model import ProvDocument

from test_case import TestCase

if __name__ == "__main__":
    # document = ProvDocument()
    # document.add_namespace("ex", "https://example.org/")
    # document.add_namespace("prov", "http://www.w3.org/ns/prov#")
    # document.entity("ex:e", {"prov:value": 1,"prov:type": 2})
    #
    # document2 = ProvDocument()
    # document2.add_namespace("ex", "https://example.org/")
    # document2.add_namespace("prov", "http://www.w3.org/ns/prov#")
    # document2.entity("ex:e", {"prov:value": 1})
    # document2.entity("ex:e",{ "prov:type": 2})
    #
    # document.serialize("../data/temp1.provn",format="provn",indent=2)
    # document2.serialize("../data/temp2.provn", format="provn", indent=2)
    # print(document.__eq__(document2.unified()))
    with open(r"..\..\config.json", 'r') as f:
        config = json.load(f)
    sys.argv = [".\main.py","default_namespace","json","d"]
    key = sys.argv[1]
    if key in config:
        class_name = config[key]
        module = importlib.import_module(f"{key}")
        class_ = getattr(module, class_name)()
        try:
            class_ = getattr(module, class_name)()
            if sys.argv[3] == "s":
                class_.serialize(sys.argv[2])
            elif sys.argv[3] == "d":
                class_.deserialize(sys.argv[2])
        except AttributeError as e:
            raise e
    else:
        print(f"Key {key} not found in the configuration.")

