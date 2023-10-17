# Session 2 : Les bases de python

_Dans cette séance nous voyons les bases de python._

1. [Git](#git)
2. [Les environnments virtuels](#les-environnments-virtuels)
3. [Variables et datatypes](#variables-et-datatypes)
4. [Fonctions](#fonctions)
5. [Conditions](#conditions)
6. [Boucles](#boucles)
7. [Modules](#modules)
8. [Classes](#classes)
9. [Erreurs](#erreurs)

## Git

Voici un [cheat sheet](/sessions/session-2/git-cheat-sheet-education.pdf) pour donner les commandes de base de git.

Faites un _pull_ et _checkout_ pour être à jour dans notre repo d'atelier python.

Qu'est ce qu'un fichier `.gitignore` ?

## Les environnments virtuels

### Pip

[Package Installer for Python](https://pypi.org/project/pip/).

Que sont les packages ?

Qu'est ce que l'environnment global ?

### Virtualenv et les modules

[Créer un environnement virtuel](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) pour son projet.

D'abord, installer `virtualenv` dans son environnement global.

```shell
pip3 install virtualenv
```

Puis, dans le dossier de son projet:

```shell
virtualenv venv
```

Créer un fichier `.gitignore`.

### requirements.txt

Pour partager ses projets:

```shell
pip freeze > requirements.txt
```

Utiliser un fichier requirements.txt:

```shell
pip install requirements.txt
```

## Variables et datatypes

NB: les commentaires.

Créer des variables (notion de variables dynamiques).

Types de données:
- Strings et caractères
- Integers
- Floats
- Booleans
- Lists, Sets, tuples (pas arrays)
- Dictionnaires

Connaitre le type d'un variable.

Conversion des variables.

## Fonctions

Qu'est ce qu'une fonction ?

Qu'est ce qu'un argument ?

Créer une fonction. + indentation.

## Conditions

Ecrire une condition.

Types de comparaisons (opérateurs):
- `==`, `!=`
- `>`, `<`, `<=`, `>=`
- `inv
- `not in`

Enchainer les conditions (`and`)

## Boucles

Qu'est ce qu'une boucle ?

Types de boucle:
- `for` + `range()` et `len()`
- `while`

`break` et `continue`.

Boucles imbriquées.

## Modules

Qu'est ce qu'une module ?

Comment installer les modules.

(Créer une module.)

## Classes

Qu'est-ce qu'une classe ?

Créer une classe + `__init__()`

## Erreurs
Qu'est ce qu'une erreur ?

Interpréter une erreur.

Debugger.

Prévenir les erreurs.
- `try` et `except`