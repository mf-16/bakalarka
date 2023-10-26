import importlib
import json
import os
import sys


if __name__ == "__main__":
    with open(r"..\..\config.json", 'r') as f:
        config = json.load(f)
    # sys.argv = [".\main.py","checking_uri_syntax","json","d"]
    key = sys.argv[1]
    if key in config:
        python_module_name = config[key]["python_module"]
        module = importlib.import_module(python_module_name)
        if sys.argv[3] == "s":
            module.serialize(sys.argv[2])
        elif sys.argv[3] == "d":
            module.deserialize(sys.argv[2])
    else:
        print(f"Key {key} not found in the configuration.")

