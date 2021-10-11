from tkinter.constants import DISABLED
from view_main_menu import MainMenu
from view_create_tournament import CreateTournament
from view_create_player import CreatePlayer
from view_tournament_menu import TournamentMenu

from model import Tournament, Player, Round, joueurs

from tkinter.messagebox import showinfo
import tkinter as tk

import re

from tinydb import TinyDB


class Controller():
    def __init__(self):
        # Initialize the different windows of the app
        self.v_main_menu = MainMenu()
        self.v_create_tournament = None
        self.v_create_player = None
        self.v_tournament_menu = None
        # Initialize database
        db = TinyDB('db.json')
        self.players_table = db.table('players')
        self.serialized_players = self.players_table.all()
        # Config the callback main menu
        self.v_main_menu.button_new_tournament.config(command=self.new_tournament)
        self.v_main_menu.button_historic.config(command=self.historic)
        self.v_main_menu.button_players.config(command=self.show_players)

    # Main menu
    def new_tournament(self):
        """Run the page to create a new tournament"""
        self.v_create_tournament = CreateTournament()
        # Config the callback create tournament
        self.v_create_tournament.button_player.config(command=self.add_player)
        self.v_create_tournament.button_play.config(command=self.play_tournament)
        self.v_create_tournament.button_player_default.config(command=self.joueurs_par_defaut)
        self.v_create_tournament.window.wait_window()
        if self.v_create_tournament.tournament:
            self.begin_tournament(self.v_create_tournament.tournament)

    # Main menu
    def historic(self):
        """Show the page of Historic"""
        showinfo("Historique", "Historique!")

    # Main menu
    def show_players(self):
        """Show all players in base"""
        showinfo("Joueurs", "Joueurs!")

    # Main menu
    def run(self):
        """Show the home page"""
        self.v_main_menu.window.mainloop()

    # Create tournament
    def add_player(self):
        if len(self.v_create_tournament.players) < 8:
            self.v_create_player = CreatePlayer()
            # Config the callback
            self.v_create_player.button_add.config(command=self.save_player)
            self.v_create_player.button_add_base.config(command=self.add_base_player)
            base_players = [
                f"{p.get('name')} {p.get('first_name')} ({p.get('birthday')})" for p in self.serialized_players
            ]
            self.v_create_player.base_player.config(values=base_players)
            # Run and wait for the user input
            self.v_create_player.window.wait_window()
            if self.v_create_player.new_player:
                ctrl_player = [
                    f'{player.name}{player.first_name}{player.birthday}'
                    for player in self.v_create_tournament.players
                ]
                new_player = self.v_create_player.new_player
                str_new_player = f'{new_player.name}{new_player.first_name}{new_player.birthday}'
                if str_new_player not in ctrl_player:
                    self.v_create_tournament.players.append(self.v_create_player.new_player)
            self.v_create_tournament.display_players()
        else:
            showinfo("Joueurs", "Il y a déjà 8 joueurs inscrits!")

    # Create tournament
    def play_tournament(self):
        """Create the tournament with the filling infos"""
        self.v_create_tournament.tournament = Tournament(
            self.v_create_tournament.name.get(),
            self.v_create_tournament.location.get(),
            self.v_create_tournament.time_system.get(),
            self.v_create_tournament.default_round.get()
            )
        if len(self.v_create_tournament.players) == self.v_create_tournament.tournament.NB_PLAYERS:
            self.v_create_tournament.tournament.players = self.v_create_tournament.players
            self.v_create_tournament.window.destroy()
        else:
            showinfo(
                "Erreur",
                f"Il n'y a pas le bon nombre de joueurs : {self.v_create_tournament.tournament.NB_PLAYERS} attendus."
                )

    # Create tournament
    def joueurs_par_defaut(self):
        self.player = []
        for joueur in joueurs:
            nouveau_joueur = Player(joueur[1], joueur[0], joueur[2], joueur[3], joueur[4])
            self.v_create_tournament.players.append(nouveau_joueur)
        self.v_create_tournament.display_players()

    # Create player
    def save_player(self):
        if self.check_player():
            self.v_create_player.new_player = Player(
                self.v_create_player.name.get(),
                self.v_create_player.name2.get(),
                self.v_create_player.birthday.get(),
                self.v_create_player.radio_value.get(),
                self.v_create_player.ranking.get(),
                )
            self.v_create_player.window.destroy()
            self.save_player_base(self.v_create_player.new_player)
        else:
            showinfo("Erreur", "Les informations renseignées ne sont pas correctes.")

    # Create player
    def check_player(self):
        f_name = re.compile(r'[A-Za-z]{2,25}((\-|\s)[A-Za-z]{2,25})*')
        f_date = re.compile('([12][0-9]|3[0-1]|0[1-9])([/])(1[0-2]|0?[1-9])([./-])(2?1?[0-9][0-9][0-9])')
        f_ranking = re.compile('[0-9]*')
        name_ok = re.fullmatch(f_name, self.v_create_player.name.get())
        first_name_ok = re.fullmatch(f_name, self.v_create_player.name2.get())
        birthday_ok = re.fullmatch(f_date, self.v_create_player.birthday.get())
        ranking_ok = re.fullmatch(f_ranking, self.v_create_player.ranking.get())
        if name_ok and first_name_ok and birthday_ok and ranking_ok:
            return True
        else:
            return False

    # Create player
    def add_base_player(self):
        player = self.serialized_players[self.v_create_player.base_player.current()]
        self.v_create_player.name.delete(0, tk.END)
        self.v_create_player.name.insert(0, player.get('name'))
        self.v_create_player.name2.delete(0, tk.END)
        self.v_create_player.name2.insert(0, player.get('first_name'))
        self.v_create_player.birthday.delete(0, tk.END)
        self.v_create_player.birthday.insert(0, player.get('birthday'))
        self.v_create_player.ranking.delete(0, tk.END)
        self.v_create_player.ranking.insert(0, player.get('ranking'))
        self.v_create_player.radio_value.set(player.get('sex'))

    def save_player_base(self, new_player):
        # Check if the new player already in base
        check_player = f'{new_player.name.lower()} {new_player.first_name.lower()} {new_player.birthday}'
        check_players = []
        for s_player in self.serialized_players:
            s_p_check = f'{s_player["name"].lower()} {s_player["first_name"].lower()} {s_player["birthday"]}'
            check_players.append(s_p_check)
        if check_player not in check_players:
            player = {
                'name': new_player.name,
                'first_name': new_player.first_name,
                'birthday': new_player.birthday,
                'sex': new_player.sex,
                'ranking': new_player.ranking,
            }
            self.serialized_players.append(player)
        self.save_base()

    def save_base(self):
        self.players_table.truncate()
        self.players_table.insert_multiple(self.serialized_players)

    # Tournament menu
    def begin_tournament(self, tournament):
        self.v_tournament_menu = TournamentMenu(tournament)
        self.v_tournament_menu.round_save_button.config(command=self.save_round)
        self.begin_next_round()

    # Tournament menu
    def begin_next_round(self):
        if len(self.v_tournament_menu.tournament.rounds) == 0:
            self.first_pairing()
        else:
            self.next_pairing()
        self.v_tournament_menu.num_round.set(f'Round {len(self.v_tournament_menu.tournament.rounds)}')
        # self.v_tournament_menu.round_label['text'] = self.v_tournament_menu.num_round.get()
        self.v_tournament_menu.display_current_round()

    # Tournament menu
    def save_round(self):
        round = self.v_tournament_menu.tournament.rounds[-1]
        for match in round.matchs:
            match_index = round.matchs.index(match)
            resultat = self.v_tournament_menu.var_win[match_index].get()
            if resultat == 'None':
                showinfo("Tournoi", "Tous les résultats n'ont pas été saisis.")
                return None
        for match in round.matchs:
            match_index = round.matchs.index(match)
            resultat = self.v_tournament_menu.var_win[match_index].get()
            if resultat == 'Victoire (1)':
                match[0][1] = 1
                match[1][1] = 0
            elif resultat == 'Victoire (2)':
                match[0][1] = 0
                match[1][1] = 1
            elif resultat == 'Match nul':
                match[0][1] = 0.5
                match[1][1] = 0.5
            match[0][0].points += match[0][1]
            match[1][0].points += match[1][1]
        self.v_tournament_menu.display_ranking()
        print(len(self.v_tournament_menu.tournament.rounds))
        print(self.v_tournament_menu.tournament.nb_round)
        if len(self.v_tournament_menu.tournament.rounds) == int(self.v_tournament_menu.tournament.nb_round):
            self.v_tournament_menu.round_save_button.config(state=DISABLED)
            self.v_tournament_menu.end_tournament()
        else:
            self.begin_next_round()

    # Tournament menu
    def check_pairing(self, pairing):
        for round in self.v_tournament_menu.tournament.rounds:
            for match in round.matchs:
                if pairing == (match[0][0], match[1][0]) or pairing == (match[1][0], match[0][0]):
                    return False
        return True

    # Tournament menu
    def first_pairing(self):
        players = sorted(
            self.v_tournament_menu.tournament.players,
            key=lambda tri: tri.ranking,
            reverse=True,
            )
        matchs = []
        half = self.v_tournament_menu.tournament.NB_PLAYERS // 2
        for i in range(half):
            match = ([players[i], 0], [players[i + half], 0])
            matchs.append(match)
        first_round = Round("Round 1")
        first_round.matchs = matchs
        self.v_tournament_menu.tournament.rounds.append(first_round)

    # Tournament menu
    def next_pairing(self):
        players = sorted(
            self.v_tournament_menu.tournament.players,
            key=lambda tri: tri.ranking,
            reverse=True,
            )
        players = sorted(players, key=lambda tri: tri.points, reverse=True)
        matchs = []
        ctrl = 0
        while len(players) > 0 and ctrl < 1000:
            ctrl += 1
            opponent = 1
            match_valid = False
            while not match_valid and opponent < len(players):
                pairing = (players[0], players[opponent])
                if self.check_pairing(pairing):
                    match = ([players[0], 0], [players[opponent], 0])
                    match_valid = True
                    matchs.append(match)
                    players.pop(opponent)
                    players.pop(0)
                else:
                    opponent += 1
            if not match_valid:
                for i in range(1, len(matchs) + 1):
                    previous_pairing = matchs[-i]
                    if self.check_pairing((previous_pairing[0][0], players[0])):
                        matchs[-i] = ([players[0], 0], [previous_pairing[0][0], 0])
                        players.pop(0)
                        players.insert(0, previous_pairing[1][0])
                        break
                    elif self.check_pairing((previous_pairing[1][0], players[0])):
                        matchs[-i] = ([players[0], 0], [previous_pairing[1][0], 0])
                        players.pop(0)
                        players.insert(0, previous_pairing[0][0])
                        break
        new_round = Round("Round " + str(len(self.v_tournament_menu.tournament.rounds) + 1))
        new_round.matchs = matchs
        self.v_tournament_menu.tournament.rounds.append(new_round)


app = Controller()
app.run()
