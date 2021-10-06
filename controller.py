from tkinter.constants import DISABLED
from view_main_menu import MainMenu
from view_create_tournament import CreateTournament
from view_create_player import CreatePlayer
from view_tournament_menu import TournamentMenu

from model import Tournament, Player, Round, joueurs

from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter import ttk


class Controller():
    def __init__(self):
        # Initialize the different windows of the app
        self.v_main_menu = MainMenu()
        self.v_create_tournament = None
        self.v_create_player = None
        self.v_tournament_menu = None
        # Initialize other variable
        self.players = []
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
        if len(self.players) < 8:
            self.v_create_player = CreatePlayer()
            # Config the callback
            self.v_create_player.button_add.config(command=self.save_player)
            # Run and wait for the user input
            self.v_create_player.window.wait_window()
            if self.v_create_player.new_player:
                self.players.append(self.v_create_player.new_player)
            self.display_players()
        else:
            showinfo("Joueurs", "Il y a déjà 8 joueurs inscrits!")

    # Create tournament
    def display_players(self):
        """Display player list in a frame, with button to remove a player"""
        if self.v_create_tournament.player_frame:
            self.v_create_tournament.player_frame.destroy()
        self.v_create_tournament.player_frame = ttk.Frame(
            self.v_create_tournament.window,
            borderwidth=2,
            relief=tk.GROOVE,
            )
        self.v_create_tournament.player_frame.place(relx=0.05, rely=0.35)
        for player in self.players:
            player_index = self.players.index(player)
            player_title = f'{player.name} {player.first_name}'
            player_label = ttk.Label(self.v_create_tournament.player_frame, text=player_title)
            player_label.grid(row=player_index, column=0)
            player_button = ttk.Button(
                self.v_create_tournament.player_frame,
                text='Désinscrire',
                command=lambda: self.remove_player(player)
                )
            player_button.grid(row=player_index, column=1)

    # Create tournament
    def remove_player(self, player):
        """Remove a player from the list"""
        self.players.remove(player)
        self.display_players()

    # Create tournament
    def play_tournament(self):
        """Create the tournament with the filling infos"""
        self.v_create_tournament.tournament = Tournament(
            self.v_create_tournament.name.get(),
            self.v_create_tournament.location.get(),
            self.v_create_tournament.time_system.get(),
            self.v_create_tournament.default_round.get()
            )
        self.v_create_tournament.tournament.players = self.players
        self.v_create_tournament.window.destroy()

    # Create tournament
    def joueurs_par_defaut(self):
        self.player = []
        for joueur in joueurs:
            nouveau_joueur = Player(joueur[1],
                            joueur[0],
                            joueur[2],
                            joueur[3],
                            joueur[4]
                            )
            self.players.append(nouveau_joueur)
        self.display_players()

    # Create player
    def save_player(self):
        self.v_create_player.new_player = Player(
            self.v_create_player.name.get(),
            self.v_create_player.name2.get(),
            self.v_create_player.birthday.get(),
            self.v_create_player.radio_value.get(),
            self.v_create_player.ranking.get(),
            )
        self.v_create_player.window.destroy()

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
