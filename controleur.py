
from modele import Joueur, Tour, joueurs
from vue import *
from datetime import datetime
from typing import List
from tinydb import TinyDB

class Organisation():
    def __init__(self, tournoi, vue):
        self.tournoi = tournoi
        self.vue = vue

    def enregistrer_joueurs(self):
        """Get some players."""
        while len(self.tournoi.joueurs) < self.tournoi.NB_JOUEURS:
            infos_joueur = self.vue.inscrire_joueur()
            if not infos_joueur:
                return None
            joueur = Joueur(infos_joueur["nom"], 
                            infos_joueur["prenom"], 
                            infos_joueur["date"], 
                            infos_joueur["sexe"]
                            )
            self.tournoi.joueurs.append(joueur)

    def joueurs_par_defaut(self):
        for joueur in joueurs:
            nouveau_joueur = Joueur(joueur[1], 
                            joueur[0], 
                            joueur[2], 
                            joueur[3]
                            )
            self.tournoi.joueurs.append(nouveau_joueur)

    def verifier_paire(self, paire):
        for ronde in self.tournoi.rondes:
            for match in ronde.matchs:
                if paire == (match[0][0],match[1][0]) or paire == (match[1][0],match[0][0]):
                    return False
        return True

    def apparier_joueur_premiere(self):
        liste_joueurs = sorted(self.tournoi.joueurs, key = lambda tri: tri.classement, reverse=True)
        liste_matchs = []
        moitie = self.tournoi.NB_JOUEURS // 2
        for i in range(moitie):
            match = ([liste_joueurs[i], 0], [liste_joueurs[i + moitie], 0])
            liste_matchs.append(match)
        premier_tour = Tour("Round 1")
        premier_tour.matchs = liste_matchs
        self.tournoi.rondes.append(premier_tour)

    def apparier_joueur_suivante(self):
        liste_joueurs = sorted(self.tournoi.joueurs, key = lambda tri: tri.classement, reverse=True)
        liste_joueurs = sorted(liste_joueurs, key = lambda tri: tri.points, reverse=True)
        liste_matchs = []
        ctrl = 0
        while len(liste_joueurs) > 0 and ctrl < 100:
            ctrl += 1
            adversaire = 1
            match_valide = False
            while not match_valide and adversaire < len(liste_joueurs):
                paire = (liste_joueurs[0], liste_joueurs[adversaire])
                if self.verifier_paire(paire):
                    match = ([liste_joueurs[0], 0], [liste_joueurs[adversaire], 0])
                    match_valide = True
                    liste_matchs.append(match)
                    liste_joueurs.pop(adversaire)
                    liste_joueurs.pop(0)
                else:
                    adversaire += 1
            if not match_valide:
                for i in range(1, len(liste_matchs) + 1):
                    paire_precedente = liste_matchs[-i]
                    if self.verifier_paire((paire_precedente[0][0], liste_joueurs[0])):
                        liste_matchs[-i] = ([liste_joueurs[0], 0], [paire_precedente[0][0], 0])
                        liste_joueurs.pop(0)
                        liste_joueurs.insert(0, paire_precedente[1][0])
                        break
                    elif self.verifier_paire((paire_precedente[1][0], liste_joueurs[0])):
                        liste_matchs[-i] = ([liste_joueurs[0], 0], [paire_precedente[1][0], 0])
                        liste_joueurs.pop(0)
                        liste_joueurs.insert(0, paire_precedente[0][0])
                        break
        nouveau_tour = Tour("Round " + str(len(self.tournoi.rondes) + 1))
        nouveau_tour.matchs = liste_matchs
        self.tournoi.rondes.append(nouveau_tour)

    def resultat_ronde(self):
        ronde = self.tournoi.rondes[-1]
        for match in ronde.matchs:
            resultat = self.vue.enregistrer_resultat(match)
            if resultat == 1:
                match[0][1] = 1
                match[1][1] = 0
            elif resultat == 2:
                match[0][1] = 0
                match[1][1] = 1
            elif resultat == 3:
                match[0][1] = 0.5
                match[1][1] = 0.5
            match[0][0].points += match[0][1]
            match[1][0].points += match[1][1]

    def run(self):
        """Run the game."""
        #self.enregistrer_joueurs()
        self.joueurs_par_defaut()
        #print([j.prenom for j in self.tournoi.joueurs])
        while len(self.tournoi.rondes) < self.tournoi.nb_tour:
            self.vue.demarrer_prochaine_ronde()
            if len(self.tournoi.rondes) == 0:
                self.apparier_joueur_premiere()
            else:
                self.apparier_joueur_suivante()
            self.vue.afficher_matchs(self.tournoi.rondes[-1])
            self.vue.terminer_ronde()
            self.resultat_ronde()
            self.vue.afficher_classement(self.tournoi)
        