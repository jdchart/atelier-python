import csv
import json
import os
import xml.etree.ElementTree as ET

def read_csv(path : str, delimiter : str = ',', quotechar : str = '"') -> list[list]:
    """Donner le chemin vers un fichier csv et retourner une liste en 2 dimensions."""
    if os.path.isfile(path):
        if os.path.splitext[1].lower() == "csv":
            content = []
            with open(path, 'r') as f:
                csv_reader = csv.reader(f, delimiter = delimiter, quotechar = quotechar)
                for row in csv_reader:
                    content.append(row)
            return content
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier csv !")
    else:
        print("Erreur ! Le fichier n'existe pas !")

def read_json(path : str) -> dict:
    """Donner le chemin vers un fichier json et retourner un dict."""
    if os.path.isfile(path):
        if os.path.splitext[1].lower() == "json":
            with open(path, 'r') as f:
                return json.load(f)
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier json !")
    else:
        print("Erreur ! Le fichier n'existe pas !")

def read_txt(path : str) -> str:
    """Donner le chemin vers un fichier txt et retourner un string."""
    if os.path.isfile(path):
        if os.path.splitext[1].lower() == "txt":
            with open(path, 'r') as f:
                return f.read()
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier txt !")
    else:
        print("Erreur ! Le fichier n'existe pas !")

def read_xml(path : str) -> ET:
    """Donner le chemin vers un fichier xml et retourner un arbre xml."""
    if os.path.isfile(path):
        if os.path.splitext[1].lower() == "xml":
            tree = ET.parse(path)
            root = tree.getroot()
            return root
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier xml !")
    else:
        print("Erreur ! Le fichier n'existe pas !")
    
def write_json(path : str, content : dict, indent : int = 4) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format json.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == "json":
        check_dir_exists(path)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii = False, indent = indent)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"json\" !")

def write_txt(path : str, content : str) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format txt.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == "txt":
        check_dir_exists(path)

        with open(path, 'w') as f:
            f.write(content)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"txt\" !")

def write_csv(path : str, content : list[list]) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format csv.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == "csv":
        check_dir_exists(path)

        with open(path, mode='w') as f:
            writer = csv.writer(f)
            for row in content:
                writer.writerow(row)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"csv\" !")

def write_xml(path : str, content : ET) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format xml.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == "xml":
        check_dir_exists(path)

        content.write(path)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"xml\" !")

def check_dir_exists(filepath):
    """Check if folder exists, if not, create it."""
    if os.path.isdir(os.path.dirname(filepath)) == False:
        os.makedirs(os.path.dirname(filepath))

def get_out_path(in_path : str, extension : str):
    """Changer l'extension d'un chemin."""
    folder = os.path.dirname(in_path)
    filename = os.path.basename(in_path)
    without_extension = os.path.splitext(filename)[0]
    return os.path.join(folder, without_extension + "." + extension)