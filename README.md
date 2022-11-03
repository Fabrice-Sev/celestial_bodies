# celestial_bodies
# Prérequis: 
- Avoir Python 3 installé sur sa machine. 
- Si ce n'est pas le cas, se rendre sur [le site officiel de python](https://www.python.org/downloads/) pour le télécharger.

# Prérequis Optionnels: 
- Avoir crée un environement virtuel grace au module venv, exe: 
  -  py -m venv chemin/vers/l'environement_virtuel (Windows)
  -  python3 -venv chemin/vers/l'environement_virtuel (Windows)
- Lancer l'environement virtuel en lançant le fichier activate ou activate.bat qui sera dans le dossier Script crée lors de la création de l'environement virtuel

# Procédure une fois le projet cloné:
1. En invite de commande (Windows) ou dans un terminal (Linux/MacOS) ou alors dans le terminal d'un IDE de votre choix (exe: IntelliJ, VSCode, Eclipse, etc...), se situer dans le dossier celestial_bodies, au même niveau que le fichier manage.py et requirements.txt
2. Installer les dépendences à l'aide de la commande: ```pip install -r requirements.txt```
3. Une fois les dépendances téléchargés, lancer le projet à l'aide de la commande: ```py manage.py runserver 8005```
4. Sur le navigateur, ouvrir l'url: [http://127.0.0.1:8005/asteroid/](http://127.0.0.1:8005/asteroid/)
