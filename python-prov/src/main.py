import datetime
import importlib
import json
import os

from prov.model import ProvDocument, ProvBundle, ProvAgent, ProvActivity, ProvEntity
import prov.graph
import sys
import checking_uri_syntax
import loss_of_microseconds
import nonsense_prov_records
import java_serialization_problems
import multiple_prov_value
import provn_deserializer_not_implemented
import escaped_characters
import local_part_of_id_with_space
import create_main_document
import default_namespace
import prov_record_without_id
import loss_of_timezone
import prov_value_not_in_entity
import space_in_prefix
import top_instance_namespace_bundle

from prov.model import ProvDocument
from prov.identifier import *
from prov.dot import prov_to_dot
from prov.graph import prov_to_graph


if __name__ == "__main__":
    # temp = {"checking_uri_syntax":checking_uri_syntax,"loss_of_microseconds":loss_of_microseconds,"local_part_of_id_with_space":local_part_of_id_with_space,
    #         "nonsense_prov_records":nonsense_prov_records,"default_namespace":default_namespace,
    #         "prov_record_without_id":prov_record_without_id,"multiple_prov_value":multiple_prov_value,
    #         "escaped_characters":escaped_characters,"loss_of_timezone":loss_of_timezone,
    #         "prov_value_not_in_entity":prov_value_not_in_entity, "space_in_prefix":space_in_prefix,
    #         "top_instance_namespace_bundle":top_instance_namespace_bundle}
    sys.argv = ["main.py", "checking_uri_syntax", "json", "d"]
    # if sys.argv[3] == "s":
    #     temp[sys.argv[1]].serialize(sys.argv[2])
    # elif sys.argv[3] == "d":
    #     temp[sys.argv[1]].deserialize(sys.argv[2])
    current_directory = os.getcwd()
    print("Current working directory:", current_directory)
    with open(r"C:\Users\forma\bakalarka\config.json", 'r') as f:
        config = json.load(f)

    # Specify the key for the Python module you want to run
    key = sys.argv[1]  # Replace with the desired key

    # Check if the key exists in the configuration
    if key in config:
        python_module_name = config[key]["python_module"]

        # Import the Python module dynamically
        try:
            module = importlib.import_module(python_module_name)
            # Assuming there's a function 'deserialize' in the Python module
            current_directory = os.getcwd()
            print("Current working directory:", current_directory)
            if sys.argv[3] == "s":
                module.serialize(sys.argv[2])
            elif sys.argv[3] == "d":
                module.deserialize(sys.argv[2])
        except ImportError:
            print(f"Error importing Python module {python_module_name}")
    else:
        print(f"Key {key} not found in the configuration.")

