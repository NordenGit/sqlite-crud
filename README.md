# sqlite-crud-app

## Description

Application Python Flask avec SQLite, tests automatisés avec Pytest et Selenium.  
Le projet est packagé dans une image Docker et testé dans un conteneur.

---

## Prérequis

- Docker installé sur ta machine
- (Optionnel) Windows pour exécuter le script `run.bat` fourni

---

## Fichiers importants

- `Dockerfile` : définition de l'image Docker
- `requirements.txt` : liste des dépendances Python (pytest, selenium, flask, flask_sqlalchemy)
- `run.bat` : script batch Windows pour build, lancer le conteneur et exécuter les tests
- `app.py` : application Flask
- `test/` : dossier contenant les fichiers de tests Pytest

---

## Comment générer le fichier requirements.txt

Si tu n'as pas encore de `requirements.txt`, crée-le avec cette commande (dans ton environnement virtuel Python) :

```bash
pip freeze > requirements.txt
```

### Demo
![alt text](https://user-images.githubusercontent.com/16520789/71201563-54cce200-22c0-11ea-97c2-5dd89637ca5a.png "Node File Explorer")
