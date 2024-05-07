# Provenance libraries compatibility issues

## Table of contents

- [Introduction](#introduction)
- [How to run this application](#how-to-run-this-application)
- [Problems found](#problems-found)
- [Explanation of design](#explanation-of-design)

## Introduction
This repository contains a web application, which is a user interface for showcasing compatibility issues I found during testing between ProvToolbox and prov Python

## How to run this application

All you need to do is download Docker for your operating system and pull an image from Docker Hub. Once you have Docker, just use this command:

`docker pull m16f/prov:1.1.1`

This pulls the image from Docker Hub to your images locally (check with `docker images`). Now you have the image locally, and you just run the web application with the command:

`docker run -it --rm -p 5000:80 m16f/prov:1.1.1`

The web application is now running on `http://localhost:5000/`. So just put the URL to the browser of your choice.

## Problems found

1. PROV-JSON states that default namespace should be serialized to "prefix.default" node. ProvToolbox however, serializes default namespace to "defaultNamespace" node. This causes problems when deserializing in Python, which expects default namespace to be in "prefix.default" node. Other way around , if a PROV-JSON document contains "prefix.default" node, the ProvToolbox when deserializing, does not consider it as a default namespace but adds it to regular namespaces and adds an implicit default namespace, which negatively affects the interpretation of identifiers with the original default namespace.

2. When serializing to PROVN format, ProvToolbox and prov Python do not escape characters that should be escaped according to the PROV-N specification.

3. Namespace is identified by IRI. When declaring namespace we bind prefix and a namespace together. After that every qualified name with this prefix refers to this namespace. When declaring namespace with invalid IRI, both libraries do not do any validation when creating it in memory. And only prov Python, when serializing to XML does validation of the IRI.

4. Identifiers in PROV are qualified names (IRIs) that consist of a namespace and a local part. Both libraries enable serialization of provenance containing an identifier with a space in the local part of the identifier, but ProvToolbox can not deserialize such a document when it is serialized in PROV-N notation.

5. There is a difference in how the ProvToolbox and the prov Python represent microseconds in timestamps. During deserialization between the implementations, both libraries can experience some loss of information.

6. There is a difference in how the ProvToolbox and prov Python deserialize timezone information. ProvToolbox when deserializing PROV-N, always changes the timestamp to have system timezone. In JSON and XML it changes the timestamp to have GMT timzone. However, prov Python does not change the timezone of the timestamp it deserializes and just preserves the original one across all formats.

7. PROV-DM allows a relation without an identifier. When serializing this to PROV-JSON, blank node prefix must be generated in the identifier. PROV-JSON does not specify if the blank node namespace should be explicit or implicit, but ProvToolbox and prov Python represented the blank namespace differently. ProvToolbox expected blank namespace to be explicitly defined and prov Python can handle blank namespace implicitly. This causes issues when serializing in prov Python and deserializing in ProvToolbox.

8. The PROV data model introduces a pre-defined set of attributes in the PROV namespace. One of them is prov:value. PROV-DM states this about prov:value. "The attribute prov:value may occur at most once in a set of attribute-value pairs." However, Python allows multiple prov:value attributes due to a flawed representation in the model. ProvToolbox adheres to the PROV-DM and does not allow multiple prov:value attributes.

9. The PROV data model introduces a pre-defined set of attributes in the PROV namespace. One of them is prov:value. PROV-DM states this about prov:value. "The attribute prov:value is an optional attribute of entity." Meaning that only entity allows attribute prov:value. However, Python allows prov:value in other records due to flawed representation in the model. ProvToolbox adheres to the PROV-DM and does not allow prov:value in other records.

10. When declaring namespace we bind prefix and a namespace together. There is no validation if the prefix is invalid when serializing to PROVN and JSON in both libraries. However, when serializing invalid prefix to XML, both libraries validate it and throw exception. 

11. In XML format, when "prov" is the default namespace prov Python has some issues when handling conversion of XML QName to QualifiedName.

12. ProvToolbox expects that the "prov" and "xsd" namespaces are explicitly defined in the PROV-JSON serialization. However, according to PROV-JSON specification, the namespaces are implicit, which causes deserialization issues when a PROV-JSON file is serialized using the prov Python library, which does not explicitly define the namespaces.

## Explanation of design
This repository contains 3 main folders `TestCases`, `java-prov` and `python-prov`.
1. `TestCases` - There is a web application written in C#, using ASP.NET framework with razor pages. This is what user sees.
2. `java-prov` - ProvToolbox test cases in form of console application. The web application calls this console application and reads the stdout and stderr.
3. `python-prov` - prov Python test cases in form of console application. The web application calls this console application and reads the stdout and stderr.

