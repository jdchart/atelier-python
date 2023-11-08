# Traitement et visualization des données

_Dans cette séance nous allons commencer à faire des choses avec nos données! On commencera à voir comment on peut les manipuler et comment les visualizer._

1. [Modules](#modules)
2. [matplotlib](#matplotlib)
3. [networkx](#networkx)
4. [scikit-learn](#scikit-learn)

## Modules

On va commencer à utiliser des bibliothèques qui ne sont pas inclus dans Python de base. Il faudra donc les telecherger dans notre environnmeent (global ou virtuel).

### Rappel : créer un environement virtuel:

[Créer un environnement virtuel](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) pour son projet.

D'abord, installer `virtualenv` dans son environnement global.

```shell
pip3 install virtualenv
```

Puis, dans le dossier de son projet:

```shell
virtualenv venv
```

Pour activer (VS code le fait automatiquement):

```shell
# Mac:
source env/bin/activate
# Windows:
env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershel
```

### Télécharger une module

Pour installer une module dans son environnement, il suffit de lancer le faire avec pip. Voici les 3 modules que nous allons utiliser:

```shell
pip install matplotlib
pip install networkx
pip install scikit-learn
```

On aura egalement besoin de numpy:
```shell
pip install numpy
```

## Matplotlib

[Matplotlib](https://matplotlib.org/) est une module pour la visualization de données en python.

- Acceder aux données

- Line plot
- Subplots
- Scatter plot
- Bar plot
- Pie plot
- 3D plot

- Manipulations simples avec des conditions

## Networkx

[Networkx](https://networkx.org/) est une module pour la manipulation et la visualization de structures en réseaux en python.

- Structure des données en réseau
- Création de graphs
- Visualisation
- Analyse de réseaux
    - Centralité
    - Chemin le plus court

## scikit-learn

- Un point sur numpy - qu'est-ce que c'est? Pourquoi l'utiliser?

[scikit-learn](https://scikit-learn.org/stable/) est une module d'analyse des données qui met à disposition beaucoup d'algorithmes de machine learning et d'intelligence artificielle.

- Pre/post processing
- Réduction de la dimensionalité
- Normalization
- Clusters
- Visualization
- Voisin le plus proche