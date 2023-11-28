# APIs, web scraping et Classes

_Dans cette séance on va apprendre ce que sont les classes, et comment se servir des APIs._

1. [Classes](#classes)
2. [Requests et beautiful soup](#requests-et-beautiful-soup)
3. [RESTful API](#restful-api)

## Classes

C'est quoi une classe ? 

C'est quoi le OOP ?

[Exemple basique](/sessions/session-5/scripts/01-classes.py)

- Définition d'une classe
- Attributs
- Méthodes
- Héritage

### Un point sur les arguments:

- Types et arguments par défaut
- **kwargs
- Return types

## Requests et beautiful soup

Le package `requests` permet d'effectuer des requetes html en python.

```python
pip install requests
pip install beautifulsoup4
```

### Requests:

- get
- status_code (200, 404)
- response.content (bytes), response.text (texte), response.json() (json)

### Beautiful soup

- html parser
- find()
- content (.string, .get())

## RESTful API

- C'est quoi un RESTful API ?
- GET, PUT, POST et DELETE (requests.get(), requests.put(), requests.post(), requests.delete())
- url parameters (?, = et &)

Exemple: l'API de [Nakala](https://api.nakala.fr/doc)