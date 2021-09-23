from datetime import datetime
from typing import List

joueurs = [['Matthieu', 'Grison', '20/12/1992', 'Homme'],
            ['Pierre', 'Grison', '16/11/1994', 'Homme'],
            ['Joseph', 'Grison', '10/04/1985', 'Homme'],
            ['Jean-Baptiste', 'Grison', '04/06/1983', 'Homme'],
            ['Jeanne', 'Grison', '22/06/1991', 'Femme'],
            ['Blandine', 'Grison', '18/09/1988', 'Femme'],
            ['Helene', 'Grison', '11/03/1987','Femme'],
            ['Catherine', 'Grison', '13/12/1956', 'Femme']]


class Joueur():
    def __init__(self, nom, prenom, date_naissance, sexe, classement=0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.points = 0


class Tournoi():
    NB_JOUEURS = 8
    def __init__(self, nom, lieu, temps='bullet', nb_tour=4):
        self.nom = nom
        self.lieu = lieu
        self.date_tournoi = datetime.now().strftime("%d/%m/%Y")
        self.temps = temps
        self.nb_tour = nb_tour
        self.joueurs : List[Joueur] = []
        self.rondes : List[Tour] = []
        self.description = ""


class Tour():
    def __init__(self, nom):
        self.nom = nom
        self.date_debut = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_fin = None
        self.matchs = []