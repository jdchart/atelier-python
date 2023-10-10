# Session 1 : Mise en place de l'environnment de travail

_La première séance est consacrée à la mise en place d'un environnment de travail qui permet de travailler de manière efficase et en collaboration._

1. [Terminal](#terminal)
2. [Installation de Python](#installation-de-python)
3. [Installation d'un IDE (VS Code)](#installation-dun-ide-vs-code)
4. [Installation de git](#installation-de-git)
5. [Les environnments virtuels](#les-environnments-virtuels)

## Terminal

[Commandes de base](https://tracer.gitbook.io/manual/support/command-line-mac-vs.-windows) (ça peut changer selon Windows et Mac).

## Installation de python

[Installation avec l'outil d'installation (Windows et Mac)](https://www.python.org/downloads/).

**ou**

[Installation sur Mac](https://docs.python-guide.org/starting/install3/osx/) avec [homebrew (recommandé)](https://brew.sh/)

### Verification de la version de Python

```shell
python3 --version
```

## Installation d'un IDE (VS Code)

[Télécharger et installer VS Code](https://code.visualstudio.com/)

- Créer un premier script python de test

```python
print("hello world")
```

- Il sera peut être nécessaire d'activer l'extension "Python" de VS Code
- Il sera peut être nécessaire de changer d'interpretateur Python dans VS Code (`Ctrl + Shift + P` sur Windows, `Cmd + Shift + P` sur Mac)

## Installation de git

[Sur Mac](https://git-scm.com/download/mac)

[Sur Windows](https://git-scm.com/download/win)

### Installation de fork

[Installer Fork pour Windows ou Mac](https://git-fork.com/)

### Créer un compte sur github

[Github](https://github.com/)

### Git:

- [ ] Cloner des repos
- [ ] Pull
- [ ] Créer des repos
- [ ] Stage, commit, push
- [ ] Branches

## Les environnments virtuels

### Pip

[Package Installer for Python](https://pypi.org/project/pip/).

Que sont les packages ?

Qu'est ce que l'environnment global ?

### Virtualenv

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

## Premier script python !

Créer un [premier script](/sessions/session-1/premier-script.py) dans Python !