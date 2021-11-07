# Gestionnaire de tournoi d'echec
Téléchargez les scripts présents sur le dépôt GitHub : https://github.com/Mattgris6/OC_DAPyhon_Projet4_Echecs
Placez ces scripts dans un répertoire de travail sur votre ordinateur.

Pour créer un environnement virtuel sous Windows, dans votre terminal, placez vous dans votre répertoire de travail via la commande cd (+ chemin du répertoire).
Ensuite, tapez la commande :

```sh
python -m venv env
```

Un nouveau répertoire env s'est créé dans votre répertoire de travail.
Pour l'activer, tapez la commande :

```sh
./env/Scripts/activate.bat
```

Maintenant que vous êtes dans l'environnement virtuel, installez les paquets requis pour le code via la commande:

```sh
pip install -r requirements.txt
```

Ensuite, vous pouvez lancer le programme avec :

```sh
python main.py
```

Une fenêtre s'ouvre avec le menu principal.
Vous pouvez créer un nouveau tournoi : une nouvelle fenêtre avec un formulaire s'ouvre.
Une fois les infos remplies, vous pouvez lancer le tournoi.
Une nouvelle fenêtre s'ouvre permettant de gérer les résultats des rounds du tournoi, avec une vision sur le classement.

Depuis le menu principal, vous pouvez accéder à l'historique des tournois.

Depuis le menu principal, vous pouvez accéder à la liste de tous les joueurs en base.
C'est là que vous allez pouvoir modifier les informations d'un joueur, et notamment son classement en fonction de ses résultats.

Une base de données de démo est fournie sur ce dépo.

Pour vérifier la conformité du code et générer un rapport flake8, vous pouvez lancer le script ctrl_flake8.py:

```sh
python ctrl_flake8.py
```
