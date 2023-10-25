# Les données: lecture et création.

_Dans cette séance nous allons voir les bases pour travailler avec les données - ouvrir des fichiers, créer des fichiers, convertir de fichiers en un autre format._

1. [Où trouver les données?](#où-trouver-les-données)
2. [Manipuler les fichiers][#manipuler-les-fichiers]
3. [Créer des fichiers](#créer-des-fichiers)
4. [Convertion](#convertion)

## Où trouver les données ?

Structure de differents formats:

- Fichiers CSV.
- Fichiers JSON.
- Fichiers XML.

## Manipuler les fichiers

### Module OS

Fonctions de base:
- `os.getcwd()`
- `os.path.join()`
- `os.path.isdir()` + `os.path.isfile()`
- `os.makedir()` + `os.makedirs()`
- `os.remove()` + `os.rmdir()` + `os.removedirs()`
- `os.rename()`

### Bonus (shutil)

`shutil.copyfile()`

### Ouvrir les fichiers

- Fonction `open()`:
    - `r` : read
    - `w` : write

- Ouvrir en tant que fichier texte.
- Ouvrir en format CSV.
- Ouvrir en format JSON.
- Ouvrir en format XML.

### Lire les fichiers

- Lire du contenu CSV (lists)
- Lire du contenu JSON (dicts)
- Lire du contenu XML

## Créer des fichiers

- Créer un fichier texte.
- Créer un fichier JSON.
- Créer un fichier CSV.
- Créer un fichier XML.

## Convertion

- CSV vers JSON.
- JSON vers XML.