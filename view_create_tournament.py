import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
# from tkinter import *


class CreateTournament():
    def __init__(self):
        self.tournament = None
        self.window = tk.Tk()
        w = 600  # width for the self.window
        h = 400  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Nouveau tournoi')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        # Get Tournament infos
        self.label_name = ttk.Label(self.window, text="Nom du tournoi : ")
        self.label_name.place(relx=0.05, rely=0.05)
        self.name = ttk.Entry(self.window, width=25)
        self.name.place(relx=0.23, rely=0.05)
        self.label_location = ttk.Label(self.window, text="Lieu du tournoi : ")
        self.label_location.place(relx=0.05, rely=0.15)
        self.location = ttk.Entry(self.window, width=25)
        self.location.place(relx=0.23, rely=0.15)
        self.label_round = ttk.Label(self.window, text="Nombre de tours : ")
        self.label_round.place(relx=0.55, rely=0.05)
        self.default_round = tk.StringVar(self.window)
        self.default_round.set('4')
        self.round = ttk.Spinbox(
            self.window,
            from_=1,
            to=7,
            textvariable=self.default_round,
            width=7
            )
        self.round.place(relx=0.75, rely=0.05)
        self.label_time_system = ttk.Label(
            self.window,
            text="Système de temps : ",
            )
        self.label_time_system.place(relx=0.55, rely=0.15)
        self.time_system = ttk.Combobox(
            self.window,
            values=["Bullet", "Blitz", "Coup rapide"],
            width=15,
            )
        self.time_system.place(relx=0.75, rely=0.15)
        self.label_describe = ttk.Label(self.window, text="Description : ")
        self.label_describe.place(relx=0.55, rely=0.25)
        self.describe = scrolledtext.ScrolledText(self.window)
        self.describe.place(relx=0.68, rely=0.25, width=170, height=250)
        self.label_players = ttk.Label(
            self.window,
            text="Liste des joueurs : ",
            )
        self.label_players.place(relx=0.05, rely=0.25)
        self.button_player = ttk.Button(
            self.window,
            text="Ajouter un joueur",
            )
        self.button_player.place(relx=0.23, rely=0.24)
        self.player_frame = None
        self.button_play = ttk.Button(
            self.window,
            text="Lancer le tournoi",
            )
        self.button_play.place(relx=0.5, rely=0.93, anchor=tk.CENTER)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.place(relx=0.92, rely=0.93, anchor=tk.CENTER)
        # Default players
        self.button_player_default = ttk.Button(
            self.window,
            text="Joueurs par defaut",
            )
        self.button_player_default.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

    def cancel(self):
        self.tournament = None
        self.window.destroy()
