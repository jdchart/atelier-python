"""
Opening files
"""
import os
import json
import csv
import xml.etree.ElementTree as ET

file_path = os.path.join(os.getcwd(), "sessions", "session-3", "data", "xml-example.xml")

def process(path):
    if os.path.isfile(path):

        method = os.path.splitext(path)[1]
        
        if method == "txt":
            content = read_txt_file(path)
        elif method == "json":
            content = read_json_file(path)
        elif method == "csv":
            content = read_csv_file(path)
        elif method == "xml":
            content = read_xml_file(path)
        
        print(content)
        #print_xml_content(content)
    else:
        print("Error! \"" + path + "\" does not exist!")

def read_txt_file(path):
    f = open(path)
    content = f.read()
    #content = f.readlines()
    f.close()
    return content

def read_csv_file(path):
    content = []
    with open(path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in csv_reader:
            content.append(row)
    return content

def read_json_file(path):
    with open(path, 'r') as f:
        return json.load(f)
    
def read_xml_file(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return root

def print_xml_content(root):
    for element in root:
        print("Element: " + element.tag)
        for subelement in element:
            print("  " + subelement.tag + ": " + subelement.text)

process(file_path, "xml")