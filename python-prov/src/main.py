import importlib
import json
import os
import sys

if __name__ == "__main__":
    config_file_path = os.path.join('..', '..', 'config.json')
    with open(config_file_path, 'r') as f:
        config = json.load(f)
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
