# Gestionnaire de tournoi d'echec

## Installation
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

Le programme utilise tkinter pour l'interface graphique, il faudra donc s'assurer de l'avoir installé préalablement.

## Utilisation
Ensuite, vous pouvez lancer le programme avec :

```sh
python main.py
```

### Création d'un tournoi
Une fenêtre s'ouvre avec le menu principal.
Vous pouvez créer un nouveau tournoi en cliquant sur le bouton "Nouveau tournoi": une nouvelle fenêtre s'ouvre avec un formulaire.
Attention, il faut exactement 8 joueurs pour commencer le tournoi!
Vous pouvez ajouter des joueurs en base ou enregistrer un nouveau joueur en renseignant le formulaire.

### Gestion du tournoi
Une fois les informations remplies, vous pouvez lancer le tournoi à l'aide du bouton "Lancer le tournoi". 
Une nouvelle fenêtre s'ouvre permettant de gérer les résultats des rounds du tournoi, avec une vision sur le classement.

### Historique des tournois
Depuis le menu principal, vous pouvez accéder à l'historique des tournois. 
Sélectionnez le tournoi dans la liste et cliquez sur "Afficher les infos".

### Joueurs en base
Depuis le menu principal, vous pouvez accéder à la liste de tous les joueurs en base.
C'est là que vous allez pouvoir modifier les informations d'un joueur, et notamment son classement en fonction de ses résultats.
Sélectionnez le joueur dans la liste et cliquez sur "Afficher les infos".
Après toute modification, vous pouvez enregistrer en cliquant sur "Enregistrer les modifications"

### Base de données de démonstration
Une base de données de démo est fournie sur ce dépôt. Toutes les données présentes sont fictives.

## Vérification du code
Pour vérifier la conformité du code et générer un rapport flake8, vous pouvez lancer le script ctrl_flake8.py:

```sh
python ctrl_flake8.py
```
