from modele import Tournoi
from controleur import Organisation
from vue import Vue
from tinydb import TinyDB


'''serialized_players = []
joueurs = [['Matthieu', 'Grison', '20/12/1992', 'Homme'],
            ['Pierre', 'Grison', '16/11/1994', 'Homme'],
            ['Joseph', 'Grison', '10/04/1985', 'Homme'],
            ['Jean-Baptiste', 'Grison', '04/06/1983', 'Homme'],
            ['Jeanne', 'Grison', '22/06/1991', 'Femme'],
            ['Blandine', 'Grison', '18/09/1988', 'Femme'],
            ['Helene', 'Grison', '11/03/1987','Femme'],
            ['Catherine', 'Grison', '13/12/1956', 'Femme']]
for joueur in joueurs:
    serialized_player = {
        "nom":joueur[1],
        "prenom":joueur[0],
        "date_naissance":joueur[2],
        "sexe":joueur[3]
    }
    serialized_players.append(serialized_player)
db = TinyDB('db.json')
players_table = db.table('players')
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_players)
'''
nouveau_tournoi = Tournoi("Premier tournoi", "Toulouse")
nouvelle_vue = Vue()


nouvelle_organistaion = Organisation(nouveau_tournoi, nouvelle_vue)
nouvelle_organistaion.run()