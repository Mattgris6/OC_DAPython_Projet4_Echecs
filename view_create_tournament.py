from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from view_create_player import CreatePlayer
# from tkinter import *


class CreateTournament():
    def __init__(self):
        self.players = []
        self.window = Tk()
        w = 600 # width for the self.windowt
        h = 400 # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the self.window window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Nouveau tournoi')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        # Get Tournament infos
        self.label_name = ttk.Label(self.window, text="Nom du tournoi : ")
        self.label_name.place(relx=0.05, rely=0.05)
        self.name = ttk.Entry(self.window, width=25)
        self.name.place(relx=0.23, rely=0.05)
        self.label_lieu = ttk.Label(self.window, text="Lieu du tournoi : ")
        self.label_lieu.place(relx=0.05, rely=0.15)
        self.lieu = ttk.Entry(self.window, width=25)
        self.lieu.place(relx=0.23, rely=0.15)
        self.label_round = ttk.Label(self.window, text="Nombre de tours : ")
        self.label_round.place(relx=0.55, rely=0.05)
        default_round = StringVar(self.window)
        default_round.set('4')
        self.round = ttk.Spinbox(
            self.window,
            from_=1,
            to=7,
            textvariable=default_round,
            width=7
            )
        self.round.place(relx=0.75, rely=0.05)
        self.label_temps = ttk.Label(self.window, text="Système de temps : ")
        self.label_temps.place(relx=0.55, rely=0.15)
        self.temps = ttk.Combobox(
            self.window,
            values=["Bullet", "Blitz", "Coup rapide"],
            width=15,
            )
        self.temps.place(relx=0.75, rely=0.15)
        self.label_describe = ttk.Label(self.window, text="Description : ")
        self.label_describe.place(relx=0.55, rely=0.25)
        self.describe = scrolledtext.ScrolledText(self.window)
        self.describe.place(relx=0.68, rely=0.25, width=170, height=250)
        self.label_players = ttk.Label(self.window, text="Liste des joueurs : ")
        self.label_players.place(relx=0.05, rely=0.25)
        self.button_player = ttk.Button(
            self.window,
            text="Ajouter un joueur",
            command=self.add_player,
            )
        self.button_player.place(relx=0.23, rely=0.24)
        self.player_frame = None
        self.button_play = ttk.Button(
            self.window,
            text="Lancer le tournoi",
            command=self.play_tournament,
            )
        self.button_play.place(relx=0.5, rely=0.93, anchor=CENTER)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.window.destroy,
            )
        self.button_quit.place(relx=0.92, rely=0.93, anchor=CENTER)

    def add_player(self):
        if len(self.players) < 8:
            view_new_player = CreatePlayer()
            new_player = view_new_player.run()
            if new_player:
                self.players.append(new_player)
            self.display_players()
        else:
            showinfo("Joueurs", "Il y a déjà 8 joueurs inscrits!")

    def display_players(self):
        if self.player_frame:
            self.player_frame.destroy()
        self.player_frame = ttk.Frame(self.window, borderwidth=2, relief=GROOVE)
        self.player_frame.place(relx=0.05, rely=0.35)
        for player in self.players:
            player_index = self.players.index(player)
            player_label = ttk.Label(self.player_frame, text=player.prenom)
            player_label.grid(row=player_index, column=0)
            player_button = ttk.Button(
                self.player_frame,
                text='Désinscrire',
                command=lambda: self.remove_player(player)
                )
            player_button.grid(row=player_index, column=1)

    def remove_player(self, player):
        self.players.remove(player)
        self.display_players()

    def play_tournament(self):
        pass

    def run(self):
        self.window.mainloop()
