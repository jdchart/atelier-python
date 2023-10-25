"""
Des fonctions pour convertir des données d'un format à un autre.
"""
import utils
import xml.etree.ElementTree as ET

def csv_to_json(csv_file):
    csv_data = utils.read_csv_file(csv_file)
    dict_data = convert_to_dict(csv_data)
    
    out_path = utils.get_out_path(csv_file, "json")
    utils.write_json(out_path, dict_data)

def json_to_xml(json_file):
    json_data = utils.read_json_file(json_file)
    xml_data = convert_to_xml(json_data)

    out_path = utils.get_out_path(json_file, "xml")
    utils.write_xml(out_path, xml_data)

def convert_to_dict(data):
    labels = data[0]
    return_data = {"people" : []}

    for item in data:
        if item != labels:
            entry = {}
            for i, val in enumerate(item):
                entry[labels[i]] = val
            return_data["people"].append(entry)
    
    return return_data

def convert_to_xml(data):
    root = ET.Element("People")

    for item in data["people"]:
        key_list = list(item.keys())
        entry = ET.SubElement(root, "person")
        for key in key_list:
            subentry = ET.SubElement(entry, key)
            subentry.text = str(item[key])
    
    return ET.ElementTree(root)

#csv_to_json("/Users/jacob/Documents/Repos/atelier-python/sessions/session-3/data/csv-example.csv")
json_to_xml("/Users/jacob/Documents/Repos/atelier-python/sessions/session-3/data/json-example.json")