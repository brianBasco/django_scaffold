# Déploiement d'un template Django :

## Virtual environment :
Dans mon répertoire de travail :
python -m venv ./django-env

activer l'environnement virtuel (windows)
django-env\Scripts\activate

## Installer Django :
pip install Django

## Ajouter un projet :
django-admin startproject projet

ou avec un template (ZIP ou répertoire, ici ZIP):
django-admin startproject --template=/chemin/template.zip mon_projet nom

## Ajouter une app :
python manage.py startapp app

ajouter l'app dans Settings :
'django.apps.AppConfig',


## HTMX et gestion des erreurs :

2 possibilités, soit :
- on met le code 200 en code de retour pour forcer le swap
- on met un écouter dans la div html #error :
hx-on::response-error="this.innerHTML = event.detail.xhr.responseText"

