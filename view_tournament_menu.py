import tkinter as tk
from tkinter import ttk


class TournamentMenu():
    def __init__(self, tournament):
        self.tournament = tournament
        self.window = tk.Tk()
        w = 800  # width for the self.windowt
        h = 400  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title(f'Gestion du tournoi {tournament.name}')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        self.round_frame = None
        self.ranking_frame = None
        self.ranking_label = ttk.Label(self.window, text='Classement :')
        self.ranking_label.grid(row=0, column=2, padx=5, pady=5)
        self.num_round = tk.StringVar(self.window)
        self.num_round.set(f'Round {len(self.tournament.rounds)}')
        self.round_label = ttk.Label(self.window, textvariable=self.num_round)
        self.round_label.grid(row=0, column=0, padx=5, pady=5)
        self.round_save_button = ttk.Button(
            self.window,
            text='Enregistrer les résultats et terminer le round',
        )
        self.round_save_button.grid(row=1, column=0, padx=5, pady=5)
        # Create a list of variable for every match of a round
        self.var_win = []
        for i in range(len(self.tournament.players) // 2):
            var_win = tk.StringVar(self.window)
            self.var_win.append(var_win)
        self.display_ranking()

    def display_ranking(self):
        if self.ranking_frame:
            self.ranking_frame.destroy()
        self.ranking_frame = ttk.Frame(self.window, borderwidth=2, relief=tk.GROOVE)
        self.ranking_frame.grid(
            row=1,
            column=2,
            rowspan=8,
            columnspan=3,
            sticky="W",
            padx=5,
            pady=5,
            )
        players = sorted(self.tournament.players, key=lambda tri: tri.ranking, reverse=True)
        players = sorted(players, key=lambda tri: tri.points, reverse=True)
        for player in players:
            player_index = players.index(player)
            player_title = f'{player.name} {player.first_name} : {player.points}pts'
            player_label = ttk.Label(self.ranking_frame, text=player_title)
            player_label.grid(row=player_index, column=0)

    def display_current_round(self):
        for var_win in self.var_win:
            var_win.set('None')
        if self.round_frame:
            self.round_frame.destroy()
        self.round_frame = ttk.Frame(self.window, borderwidth=2, relief=tk.GROOVE)
        self.round_frame.grid(
            row=3,
            column=0,
            rowspan=7,
            columnspan=2,
            sticky="W",
            padx=5,
            pady=5,
            )
        round = self.tournament.rounds[-1]
        for match in round.matchs:
            match_index = round.matchs.index(match)
            player1 = f'(1) {match[0][0].first_name} {match[0][0].name}'
            player2 = f'(2) {match[1][0].first_name} {match[1][0].name}'
            match_title = f'{player1} vs {player2}'
            match_label = ttk.Label(self.round_frame, text=match_title)
            match_label.grid(row=match_index, column=0)
            button_list = ['Victoire (1)', 'Victoire (2)', 'Match nul']
            c = 1
            for elem in button_list:
                b = ttk.Radiobutton(
                    self.round_frame,
                    text=elem,
                    variable=self.var_win[match_index],
                    value=elem,
                    )
                b.grid(row=match_index, column=c)
                c += 1

    def end_tournament(self):
        if self.round_frame:
            self.round_frame.destroy()
        self.num_round.set('Le tournoi est terminé!')
