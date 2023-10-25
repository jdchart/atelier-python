import csv
import json
import os

def read_csv_file(path):
    content = []
    with open(path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in csv_reader:
            content.append(row)
    return content

def write_json(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)

def write_xml(path, content):
    content.write(path)

def read_json_file(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_out_path(in_path, extension):
    folder = os.path.dirname(in_path)
    filename = os.path.basename(in_path)
    without_extension = os.path.splitext(filename)[0]
    return os.path.join(folder, without_extension + "." + extension)