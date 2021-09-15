class Vue():
    def inscrire_joueur(self):
        """Prompt for a name."""
        nom = input("Tapez le nom du joueur : ")
        if not nom:
            return None
        prenom = input("Tapez le prénom du joueur : ")
        if not prenom:
            return None
        date_naissance = input("Tapez la date de naissance du joueur : ")
        if not date_naissance:
            return None
        sexe = input("Tapez le sexe du joueur : ")
        if not sexe:
            return None
        return {"nom":nom,
                "prenom":prenom,
                "date":date_naissance,
                "sexe":sexe
                }

    def demarrer_prochaine_ronde(self):
        demarrer = ''
        while demarrer != 'O':
            demarrer = input("Voulez vous démarrer la ronde suivante? (O/N)")
            '''if demarrer.upper() == 'O':
                return True
            elif demarrer.upper() == 'N':
                return False
            else:
                print("Erreur de saisie")'''

    def afficher_matchs(self, ronde):
        print(ronde.nom)
        i = 1
        for match in ronde.matchs:
            print('Match ' + str(i), match[0][0].prenom, 'vs', match[1][0].prenom)
            i += 1

    def terminer_ronde(self):
        demarrer = ''
        while demarrer != 'O':
            demarrer = input("Voulez vous terminer la ronde en cours? (O/N)")

    def enregistrer_resultat(self, match):
        print("Qui a gagné le match " + match[0][0].prenom + " vs " + match[1][0].prenom + " ?")
        print(match[0][0].prenom + " : tapez 1")
        print(match[1][0].prenom + " : tapez 2")
        print("Match nul : tapez 3")
        return(int(input()))

    def afficher_classement(self, tournoi):
        print("Classement : ")
        classement = sorted(tournoi.joueurs, key = lambda tri: tri.classement, reverse=True)
        classement = sorted(tournoi.joueurs, key = lambda tri: tri.points, reverse=True)
        for joueur in classement:
            print(joueur.prenom, ' : ', joueur.points)

    def menu_principal(self):
        print("Menu principal")
        print("Commencer un tournoi : T")
        print("Afficher la liste des tournois : LT")
        print("Afficher la liste des acteurs : LA")
        print("Quitter : Q")

    def menu_tournoi(self, tournoi):
        print("Menu tournoi")
        print("Afficher la liste des rounds : LR")
        print("Afficher la liste des joueurs : LJ")
        print("Afficher la liste des matchs : LM")
        print("Continuer le tournoi : C")
        print("Retour au menu principal : MP")