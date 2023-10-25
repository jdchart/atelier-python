"""
Writing files.
"""
import os
import json
import csv
import xml.etree.ElementTree as ET

file_path = os.path.join(os.getcwd(), "sessions", "session-3", "output", "file.txt")

def write_txt(path, content):
    with open(path, 'w') as f:
        f.write(content)
        #f.writelines(content)

def write_json(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

def write_csv(path, content):
    with open(path, mode='w') as f:
        writer = csv.writer(f)

        for row in content:
            writer.writerow(row)

def write_xml(path, content):
    content.write(path)

def create_xml_data():
    root = ET.Element("Person")
    person1 = ET.SubElement(root, "person")
    name1 = ET.SubElement(person1, "name")
    name1.text = "Alice"
    age1 = ET.SubElement(person1, "age")
    age1.text = "25"

    tree = tree = ET.ElementTree(root)
    return tree