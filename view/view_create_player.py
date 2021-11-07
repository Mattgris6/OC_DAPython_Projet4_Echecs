import tkinter as tk
from tkinter import ttk


class CreatePlayer():
    def __init__(self):
        self.window = tk.Tk()
        w = 500  # width for the self.window
        h = 250  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Nouveau joueur')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        # Get player infos
        self.new_player = None
        self.label_base_player = ttk.Label(self.window, text="Joueur déjà enregistré : ")
        self.label_base_player.grid(row=0, column=1, padx=5, pady=5)
        self.base_player = ttk.Combobox(
            self.window,
            width=40,
        )
        self.base_player.grid(row=0, column=2, padx=5, pady=5)
        self.button_add_base = ttk.Button(
            self.window,
            text="OK",
            )
        self.button_add_base.grid(row=0, column=3, padx=5, pady=5)
        self.label_name = ttk.Label(self.window, text="Nom : ")
        self.label_name.grid(row=1, column=1, padx=5, pady=5)
        self.name = ttk.Entry(self.window, width=40)
        self.name.grid(row=1, column=2, padx=5, pady=5, sticky="W")
        self.label_name2 = ttk.Label(self.window, text="Prénom : ")
        self.label_name2.grid(row=2, column=1, padx=5, pady=5)
        self.name2 = ttk.Entry(self.window, width=40)
        self.name2.grid(row=2, column=2, padx=5, pady=5, sticky="W")
        self.label_birthday = ttk.Label(
            self.window,
            text="Date de naissance : ",
            )
        self.label_birthday.grid(row=3, column=1, padx=5, pady=5)
        self.birthday = ttk.Entry(self.window, width=25)
        self.birthday.grid(row=3, column=2, padx=5, pady=5, sticky="W")
        self.label_ranking = ttk.Label(self.window, text="Classement : ")
        self.label_ranking.grid(row=4, column=1, padx=5, pady=5)
        self.ranking = ttk.Entry(self.window, width=25)
        self.ranking.grid(row=4, column=2, padx=5, pady=5, sticky="W")
        self.radio_value = tk.StringVar(self.window)
        self.button_man = ttk.Radiobutton(
            self.window,
            text='Homme',
            value='Homme',
            variable=self.radio_value,
        )
        self.button_man.grid(row=5, column=1, padx=5, pady=5)
        self.button_woman = ttk.Radiobutton(
            self.window,
            text='Femme',
            value='Femme',
            variable=self.radio_value,
        )
        self.button_woman.grid(row=5, column=2, padx=5, pady=5)
        self.button_add = ttk.Button(
            self.window,
            text="Ajouter le joueur",
            )
        self.button_add.grid(row=7, column=1, padx=5, pady=5)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.grid(row=7, column=2, padx=5, pady=5)

    def cancel(self):
        self.new_player = None
        self.window.destroy()
