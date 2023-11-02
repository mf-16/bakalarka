import importlib
import json
import os
import sys

from prov.model import ProvDocument

if __name__ == "__main__":
    document = ProvDocument()
    document.add_namespace("ex", "https://example.org/")
    document.add_namespace("prov", "http://www.w3.org/ns/prov#")
    document.entity("ex:e", {"prov:value": 1,"prov:type": 2})

    document2 = ProvDocument()
    document2.add_namespace("ex", "https://example.org/")
    document2.add_namespace("prov", "http://www.w3.org/ns/prov#")
    document2.entity("ex:e", {"prov:value": 1})
    document2.entity("ex:e",{ "prov:type": 2})

    document.serialize("../data/temp1.provn",format="provn",indent=2)
    document2.serialize("../data/temp2.provn", format="provn", indent=2)
    print(document.__eq__(document2.unified()))
    # with open(r"..\..\config.json", 'r') as f:
    #     config = json.load(f)
    # # sys.argv = [".\main.py","checking_uri_syntax","json","d"]
    # key = sys.argv[1]
    # if key in config:
    #     python_module_name = config[key]["python_module"]
    #     module = importlib.import_module(python_module_name)
    #     if sys.argv[3] == "s":
    #         module.serialize(sys.argv[2])
    #     elif sys.argv[3] == "d":
    #         module.deserialize(sys.argv[2])
    # else:
    #     print(f"Key {key} not found in the configuration.")

