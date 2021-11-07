from view.view_main_menu import MainMenu
from view.view_create_tournament import CreateTournament
from view.view_create_player import CreatePlayer
from view.view_players import ViewPlayer
from view.view_rounds import ViewRounds
from view.view_tournament_menu import TournamentMenu
from view.view_tournaments import ViewTournaments

from model.model import Tournament, Player, Round

from tkinter.messagebox import showinfo
import tkinter as tk
from tkinter.constants import DISABLED

import re
from tinydb import TinyDB
from datetime import datetime


class Controller():
    def __init__(self):
        # Initialize the different windows of the app
        self.v_main_menu = MainMenu()
        self.v_create_tournament = None
        self.v_create_player = None
        self.v_tournament_menu = None
        self.v_players = None
        self.v_tournaments = None
        self.v_rounds = None
        # Others initialization
        self.p_display_type = None
        self.t_display_type = None
        # Initialize database
        db = TinyDB('db.json')
        self.players_table = db.table('players')
        self.serialized_players = self.players_table.all()
        self.tournament_table = db.table('tournament')
        self.serialized_tournament = self.tournament_table.all()
        # Config the callback main menu
        self.v_main_menu.button_new_tournament.config(command=self.new_tournament)
        self.v_main_menu.button_historic.config(command=self.historic)
        self.v_main_menu.button_players.config(command=self.show_players)

    @property
    def instanced_players(self):
        """Players in base as instance"""
        players = []
        for player in self.serialized_players:
            i_player = Player(
                player.get('name'),
                player.get('first_name'),
                player.get('birthday'),
                player.get('sex'),
                player.get('ranking'),
                self.serialized_players.index(player) + 1,
            )
            players.append(i_player)
        return players

    @property
    def alphabetic_order_players(self):
        """Players in base as instance ordered by alphabetic"""
        players = sorted(
            sorted(self.instanced_players, key=lambda tri: tri.first_name),
            key=lambda tri: tri.name
            )
        return players

    @property
    def ranking_order_players(self):
        """Players in base as instance ordered by ranking"""
        players = sorted(self.instanced_players, key=lambda tri: tri.ranking, reverse=True)
        return players

    @property
    def instanced_tournaments(self):
        """Tournaments in base as instance"""
        tournaments = []
        for tournament in self.serialized_tournament:
            i_tournament = Tournament(
                tournament.get('name'),
                tournament.get('location'),
                tournament.get('time_system'),
                tournament.get('nb_round'),
                tournament.get('description'),
                self.serialized_tournament.index(tournament),
            )
            i_tournament.date_tournament = tournament.get('date_tournament')
            i_tournament.players = [self.instanced_players[player - 1] for player in tournament.get('players')]
            i_tournament.rounds = [self.instanced_round(round) for round in tournament.get('rounds')]
            tournaments.append(i_tournament)
        return tournaments

    @property
    def date_order_tournaments(self):
        tournaments = sorted(self.instanced_tournaments, key=lambda tri: tri.date_tournament)
        return tournaments

    @property
    def name_order_tournaments(self):
        tournaments = sorted(self.instanced_tournaments, key=lambda tri: tri.name)
        return tournaments

    def instanced_round(self, round):
        """To instance a round dictionnary"""
        i_round = Round(round.get('name'))
        i_round.date_begin = round.get('date_begin')
        i_round.date_end = round.get('date_end')
        i_round.matchs = round.get('matchs')
        for match in i_round.matchs:
            if isinstance(match[0][0], int):
                match[0][0] = self.instanced_players[match[0][0] - 1]
                match[1][0] = self.instanced_players[match[1][0] - 1]
        return i_round

    # Main menu
    def run(self):
        """Show the home page"""
        self.v_main_menu.window.mainloop()

    # Main menu (new tournment)
    def new_tournament(self):
        """Run the page to create a new tournament"""
        self.v_create_tournament = CreateTournament()
        # Config the callback create tournament
        self.v_create_tournament.button_player.config(command=self.add_player)
        self.v_create_tournament.button_play.config(command=self.play_tournament)
        self.v_create_tournament.window.wait_window()
        if self.v_create_tournament.tournament:
            s_tournament = self.v_create_tournament.tournament.serial_tournament
            self.serialized_tournament.append(s_tournament)
            self.v_create_tournament.tournament.index = self.serialized_tournament.index(s_tournament)
            self.save_base_tournament()
            self.begin_tournament(self.v_create_tournament.tournament)

    # Main menu (historic)
    def historic(self):
        """Show the page of Historic"""
        self.v_tournaments = ViewTournaments()
        self.v_tournaments.b_order_name.config(command=self.t_display_name)
        self.v_tournaments.b_order_date.config(command=self.t_display_date)
        self.v_tournaments.b_show.config(command=self.display_tournament)
        self.v_tournaments.b_show_round.config(command=self.display_rounds)
        self.v_tournaments.b_order_pname.config(command=self.order_player_name)
        self.v_tournaments.b_order_points.config(command=self.order_player_points)
        self.v_tournaments.b_order_rank.config(command=self.order_player_rank)
        self.t_display_date()

    def display_tournament(self):
        """Call back to display info of the selected tournament"""
        selected = self.v_tournaments.tournament_list.curselection()
        selected_id = self.v_tournaments.tournament_list.curselection()[0]
        if selected:
            if self.t_display_type == 'date':
                tournament = self.date_order_tournaments[selected_id]
            elif self.t_display_type == 'name':
                tournament = self.name_order_tournaments[selected_id]
        self.v_tournaments.display_tournament_info(tournament)

    def t_display_date(self):
        """Order the listbox by date"""
        self.v_tournaments.display_list(self.date_order_tournaments)
        self.t_display_type = 'date'

    def t_display_name(self):
        """Order the listbox by name"""
        self.v_tournaments.display_list(self.name_order_tournaments)
        self.t_display_type = 'name'

    def display_rounds(self):
        """Display the rounds of the selected tournament"""
        id = self.v_tournaments.id.cget("text")
        if id != "":
            tournament = self.instanced_tournaments[id]
            self.v_rounds = ViewRounds()
            self.v_rounds.display_rounds(tournament)

    def order_player_name(self):
        """Order the players of the selected tournament by name"""
        id = self.v_tournaments.id.cget("text")
        if id != "":
            tournament = self.instanced_tournaments[id]
            players = sorted(tournament.players, key=lambda tri: tri.first_name)
            players = sorted(players, key=lambda tri: tri.name)
            self.v_tournaments.order_player_frame(tournament, players)

    def order_player_points(self):
        """Order the players of the selected tournament by points"""
        id = self.v_tournaments.id.cget("text")
        if id != "":
            tournament = self.instanced_tournaments[id]
            players = sorted(tournament.players, key=lambda tri: tri.ranking, reverse=True)
            players = sorted(players, key=lambda tri: tri.set_points(tournament), reverse=True)
            self.v_tournaments.order_player_frame(tournament, players)

    def order_player_rank(self):
        """Order players of the selected tournament by rank"""
        id = self.v_tournaments.id.cget("text")
        if id != "":
            tournament = self.instanced_tournaments[id]
            players = sorted(tournament.players, key=lambda tri: tri.ranking, reverse=True)
            self.v_tournaments.order_player_frame(tournament, players)

    # Main menu
    def show_players(self):
        """Show all players in base"""
        self.v_players = ViewPlayer()
        self.v_players.b_order_name.config(command=self.display_alphabetic)
        self.v_players.b_order_rank.config(command=self.display_ranking)
        self.v_players.b_show.config(command=self.display_player)
        self.v_players.b_save.config(command=self.save_changes)
        self.display_ranking()

    def display_player(self):
        """Call back to display info of the selected player"""
        selected = self.v_players.player_list.curselection()
        selected_id = self.v_players.player_list.curselection()[0]
        if selected:
            if self.p_display_type == 'alphabetic':
                player = self.alphabetic_order_players[selected_id]
            elif self.p_display_type == 'ranking':
                player = self.ranking_order_players[selected_id]
        self.v_players.display_player_info(player)

    def display_alphabetic(self):
        """Order the listbox  by alphabetic"""
        self.v_players.display_list(self.alphabetic_order_players)
        self.p_display_type = 'alphabetic'

    def display_ranking(self):
        """Order the listbox by ranking"""
        self.v_players.display_list(self.ranking_order_players)
        self.p_display_type = 'ranking'

    def save_changes(self):
        """Save the changes of selected player"""
        if self.v_players.id.cget("text") != '':
            id = int(self.v_players.id.cget("text")) - 1
            self.serialized_players[id]['name'] = self.v_players.name.get()
            self.serialized_players[id]['first_name'] = self.v_players.first_name.get()
            self.serialized_players[id]['birthday'] = self.v_players.birthday.get()
            self.serialized_players[id]['ranking'] = int(self.v_players.ranking.get())
            self.serialized_players[id]['sex'] = self.v_players.radio_value.get()
            self.save_base_player()

    # Create tournament
    def add_player(self):
        """Add a player to the tournament"""
        if len(self.v_create_tournament.players) < 8:
            self.v_create_player = CreatePlayer()
            # Config the callback
            self.v_create_player.button_add.config(command=self.sign_player)
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
            self.v_create_tournament.default_round.get(),
            self.v_create_tournament.describe.get("1.0", tk.END),
            )
        if len(self.v_create_tournament.players) == self.v_create_tournament.tournament.NB_PLAYERS:
            self.v_create_tournament.tournament.players = self.v_create_tournament.players
            self.v_create_tournament.window.destroy()
        else:
            showinfo(
                "Erreur",
                f"Il n'y a pas le bon nombre de joueurs : {self.v_create_tournament.tournament.NB_PLAYERS} attendus."
                )

    # Create player
    def sign_player(self):
        """Create a new instance and sign up the player for the tournament"""
        if self.check_player():
            self.v_create_player.new_player = Player(
                self.v_create_player.name.get(),
                self.v_create_player.name2.get(),
                self.v_create_player.birthday.get(),
                self.v_create_player.radio_value.get(),
                int(self.v_create_player.ranking.get()),
                )
            self.save_player(self.v_create_player.new_player)
            self.v_create_player.window.destroy()
        else:
            showinfo("Erreur", "Les informations renseignées ne sont pas correctes.")

    # Create player
    def check_player(self):
        """Check the recorded info"""
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
        """Fill the entries with info of the selected player"""
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

    def save_player(self, new_player):
        """Add player in base"""
        # Check if the new player already in base
        check_player = f'{new_player.name.lower()} {new_player.first_name.lower()} {new_player.birthday}'
        check_players = []
        for s_player in self.serialized_players:
            s_p_check = f'{s_player["name"].lower()} {s_player["first_name"].lower()} {s_player["birthday"]}'
            check_players.append(s_p_check)
        if check_player not in check_players:
            self.serialized_players.append(new_player.serial_player)
        new_player.index = self.serialized_players.index(new_player.serial_player) + 1
        self.save_base_player()

    def save_base_player(self):
        """Save the player table in base"""
        self.players_table.truncate()
        self.players_table.insert_multiple(self.serialized_players)

    def save_base_tournament(self):
        """Save the tournament table in base"""
        self.tournament_table.truncate()
        self.tournament_table.insert_multiple(self.serialized_tournament)

    # Tournament menu
    def begin_tournament(self, tournament):
        """Start a new tournament"""
        self.v_tournament_menu = TournamentMenu(tournament)
        self.v_tournament_menu.round_save_button.config(command=self.save_round)
        self.begin_next_round()

    # Tournament menu
    def begin_next_round(self):
        """Begin a new round"""
        if len(self.v_tournament_menu.tournament.rounds) == 0:
            self.first_pairing()
        else:
            self.next_pairing()
        self.v_tournament_menu.num_round.set(f'Round {len(self.v_tournament_menu.tournament.rounds)}')
        self.v_tournament_menu.display_current_round()

    # Tournament menu
    def save_round(self):
        """Save the results of a round"""
        round = self.v_tournament_menu.tournament.rounds[-1]
        for match in round.matchs:
            match_index = round.matchs.index(match)
            resultat = self.v_tournament_menu.var_win[match_index].get()
            if resultat == 'None':
                showinfo("Tournoi", "Tous les résultats n'ont pas été saisis.")
                return None
        round.date_end = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
        s_tournament = self.v_tournament_menu.tournament.serial_tournament
        self.serialized_tournament[self.v_tournament_menu.tournament.index] = s_tournament
        self.save_base_tournament()
        if len(self.v_tournament_menu.tournament.rounds) == int(self.v_tournament_menu.tournament.nb_round):
            self.v_tournament_menu.round_save_button.config(state=DISABLED)
            self.v_tournament_menu.end_tournament()
        else:
            self.begin_next_round()

    # Tournament menu
    def check_pairing(self, pairing):
        """Check if the pair has not already been done"""
        for round in self.v_tournament_menu.tournament.rounds:
            for match in round.matchs:
                if pairing == (match[0][0], match[1][0]) or pairing == (match[1][0], match[0][0]):
                    return False
        return True

    # Tournament menu
    def first_pairing(self):
        """Make the pairs for the first round"""
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
        """Make the pairs for the next rounds"""
        players = sorted(
            self.v_tournament_menu.tournament.players,
            key=lambda tri: tri.ranking,
            reverse=True,
            )
        players = sorted(players, key=lambda tri: tri.points, reverse=True)
        matchs = []
        trying_pair = []
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
                    first_pair = (previous_pairing[0][0], players[0])
                    second_pair = (previous_pairing[1][0], players[0])
                    if self.check_pairing(first_pair) and first_pair not in trying_pair:
                        matchs[-i] = ([players[0], 0], [previous_pairing[0][0], 0])
                        trying_pair.append(first_pair)
                        players.pop(0)
                        players.insert(0, previous_pairing[1][0])
                        break
                    elif self.check_pairing(second_pair) and second_pair not in trying_pair:
                        matchs[-i] = ([players[0], 0], [previous_pairing[1][0], 0])
                        trying_pair.append(second_pair)
                        players.pop(0)
                        players.insert(0, previous_pairing[0][0])
                        break
        new_round = Round("Round " + str(len(self.v_tournament_menu.tournament.rounds) + 1))
        new_round.matchs = matchs
        self.v_tournament_menu.tournament.rounds.append(new_round)
