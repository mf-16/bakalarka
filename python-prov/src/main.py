import datetime

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
    temp = {"checking_uri_syntax":checking_uri_syntax,"loss_of_microseconds":loss_of_microseconds,"local_part_of_id_with_space":local_part_of_id_with_space,
            "nonsense_prov_records":nonsense_prov_records,"default_namespace":default_namespace,
            "prov_record_without_id":prov_record_without_id,"multiple_prov_value":multiple_prov_value,
            "escaped_characters":escaped_characters,"loss_of_timezone":loss_of_timezone,
            "prov_value_not_in_entity":prov_value_not_in_entity, "space_in_prefix":space_in_prefix,
            "top_instance_namespace_bundle":top_instance_namespace_bundle}
    if sys.argv[3] == "s":
        temp[sys.argv[1]].serialize(sys.argv[2])
    elif sys.argv[3] == "d":
        temp[sys.argv[1]].deserialize(sys.argv[2])
    # doc = ProvDocument()
    # # doc = doc.deserialize("../data/temp.json")
    # # print(doc.get_provn())
    # doc.set_default_namespace("https://example.com")
    # doc.add_namespace("ex","https://example.org")
    # e = doc.entity("ex:e")
    # ac = doc.activity("ex:ac")
    # doc.wasGeneratedBy(e,ac)
    #
    # doc.serialize("../data/temp.rdf",format="rdf")

    # b1 = doc.bundle("b1")
    # b1.entity("ex:1")
    # b2 = doc.bundle("ex:b2")
    # b2.set_default_namespace("https://example.com")
    # b2.entity("2")
    # b3 = doc.bundle("ex:b3")
    # b3.add_namespace("ok", "https://example.org")
    # b3.add_namespace("ex", "https://example.org")
    # b3.entity("ok:3")
    # doc.serialize(r"../../java-prov/data/temp.json", format="json",indent=2)
    # print(doc.get_provn())


    #bad_uri.perform()
    #provn_deserializer_not_implemented.perform()
    #weird_character_as_identifier.perform()
    #id_with_space.perform()
    #datetime_microseconds.perform()
    #invalid_records.perform()
    #prov_value.perform()
    #java_serialization_problems.perform()
    #create_main_document.perform()
    #json_default_namespace.perform()
    #prov_relation_without_id.perform()
    #id_with_space.perform()

