import tkinter as tk
from tkinter import ttk


class ViewTournaments():
    def __init__(self):
        self.window = tk.Tk()
        w = 800  # width for the self.window
        h = 250  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Historique des tournois')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        # List of Tournaments
        self.tournament_list = tk.Listbox(self.window, width=50)
        self.tournament_list.grid(row=1, column=0, rowspan=7, columnspan=3, padx=5, pady=5)
        # Order by name
        self.b_order_name = ttk.Button(
            self.window,
            text="Trier par nom",
            )
        self.b_order_name.grid(row=0, column=0, padx=5, pady=5)
        # Order by ranking
        self.b_order_date = ttk.Button(
            self.window,
            text="Trier par date",
            )
        self.b_order_date.grid(row=0, column=1, padx=5, pady=5)
        # Display player information to change it
        self.b_show = ttk.Button(
            self.window,
            text="Afficher les infos",
            )
        self.b_show.grid(row=0, column=2, padx=5, pady=5)
        # Info of one tournament
        self.l_id = ttk.Label(self.window, text="id en base : ")
        self.l_id.grid(row=0, column=3, padx=5, pady=5, sticky="E")
        self.id = ttk.Label(self.window, text="")
        self.id.grid(row=0, column=4, padx=5, pady=5, sticky="W")
        self.l_name = ttk.Label(self.window, text="Nom du tournoi : ")
        self.l_name.grid(row=1, column=3, padx=5, pady=5, sticky="E")
        self.name = ttk.Label(self.window, text="")
        self.name.grid(row=1, column=4, padx=5, pady=5, sticky="W")
        self.l_location = ttk.Label(self.window, text="Lieu : ")
        self.l_location.grid(row=2, column=3, padx=5, pady=5, sticky="E")
        self.location = ttk.Label(self.window, text="")
        self.location.grid(row=2, column=4, padx=5, pady=5, sticky="W")
        self.l_date = ttk.Label(self.window, text="Date : ")
        self.l_date.grid(row=3, column=3, padx=5, pady=5, sticky="E")
        self.date = ttk.Label(self.window, text="")
        self.date.grid(row=3, column=4, padx=5, pady=5, sticky="W")
        self.l_round = ttk.Label(self.window, text="Nombre de tours : ")
        self.l_round.grid(row=4, column=3, padx=5, pady=5, sticky="E")
        self.round = ttk.Label(self.window, text="")
        self.round.grid(row=4, column=4, padx=5, pady=5, sticky="W")
        self.l_time_system = ttk.Label(
            self.window,
            text="Système de temps : ",
            )
        self.l_time_system.grid(row=5, column=3, padx=5, pady=5, sticky="E")
        self.time_system = ttk.Label(self.window, text="",)
        self.time_system.grid(row=5, column=4, padx=5, pady=5, sticky="W")
        self.l_describe = ttk.Label(self.window, text="Description : ")
        self.l_describe.grid(row=6, column=3, padx=5, pady=5, sticky="E")
        self.describe = ttk.Label(self.window, text="")
        self.describe.grid(row=6, column=4, padx=5, pady=5, sticky="W")
        self.l_ranking = ttk.Label(self.window, text="Classement : ")
        self.l_ranking.grid(row=0, column=5, padx=5, pady=5)
        self.player_frame = None
        # To show all the rounds
        self.b_show_round = ttk.Button(
            self.window,
            text="Voir les rounds",
            state=tk.DISABLED,
            )
        self.b_show_round.grid(row=8, column=4, padx=5, pady=5)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.grid(row=8, column=2, padx=5, pady=5)

    def cancel(self):
        self.window.destroy()

    def display_tournament_info(self, tournament):
        self.id.config(text=tournament.index)
        self.name.config(text=tournament.name)
        self.date.config(text=tournament.date_tournament)
        self.location.config(text=tournament.location)
        self.time_system.config(text=tournament.time_system)
        self.round.config(text=tournament.nb_round)
        self.describe.config(text=tournament.description)
        if self.player_frame:
            self.player_frame.destroy()
        self.player_frame = ttk.Frame(self.window, borderwidth=2, relief=tk.GROOVE)
        self.player_frame.grid(
            row=0,
            column=5,
            rowspan=8,
            sticky="W",
            padx=5,
            pady=5,
            )
        players = sorted(tournament.players, key=lambda tri: tri.ranking, reverse=True)
        players = sorted(players, key=lambda tri: tri.set_points(tournament), reverse=True)
        for player in players:
            player_index = players.index(player)
            player_title = f'{player.name} {player.first_name} : {player.set_points(tournament)}pts'
            player_label = ttk.Label(self.player_frame, text=player_title)
            player_label.grid(row=player_index, column=0)
        # Enable the button to show rounds
        self.b_show_round.config(state=tk.ACTIVE)

    def display_list(self, list_tournamnents):
        """Order the listbox by date"""
        self.tournament_list.delete(0, tk.END)
        for tournament in list_tournamnents:
            self.tournament_list.insert(
                'end',
                f'{tournament.name} ({tournament.date_tournament})'
                )
        