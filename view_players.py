import tkinter as tk
from tkinter import ttk


class ViewPlayer():
    def __init__(self):
        self.window = tk.Tk()
        w = 800  # width for the self.window
        h = 300  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Joueurs')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        # Get player infos
        self.label_id = ttk.Label(self.window, text="id en base : ")
        self.label_id.grid(row=0, column=3, padx=5, pady=5)
        self.id = ttk.Label(self.window, text="")
        self.id.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.label_name = ttk.Label(self.window, text="Nom : ")
        self.label_name.grid(row=1, column=3, padx=5, pady=5)
        self.name = ttk.Entry(self.window, width=40)
        self.name.grid(row=1, column=4, padx=5, pady=5, sticky="W")
        self.label_name2 = ttk.Label(self.window, text="Prénom : ")
        self.label_name2.grid(row=2, column=3, padx=5, pady=5)
        self.first_name = ttk.Entry(self.window, width=40)
        self.first_name.grid(row=2, column=4, padx=5, pady=5, sticky="W")
        self.label_birthday = ttk.Label(
            self.window,
            text="Date de naissance : ",
            )
        self.label_birthday.grid(row=3, column=3, padx=5, pady=5)
        self.birthday = ttk.Entry(self.window, width=25)
        self.birthday.grid(row=3, column=4, padx=5, pady=5, sticky="W")
        self.label_ranking = ttk.Label(self.window, text="Classement : ")
        self.label_ranking.grid(row=4, column=3, padx=5, pady=5)
        self.ranking = ttk.Entry(self.window, width=25)
        self.ranking.grid(row=4, column=4, padx=5, pady=5, sticky="W")
        self.radio_value = tk.StringVar(self.window)
        self.button_man = ttk.Radiobutton(
            self.window,
            text='Homme',
            value='Homme',
            variable=self.radio_value,
        )
        self.button_man.grid(row=5, column=3, padx=5, pady=5)
        self.button_woman = ttk.Radiobutton(
            self.window,
            text='Femme',
            value='Femme',
            variable=self.radio_value,
        )
        self.button_woman.grid(row=5, column=4, padx=5, pady=5)
        # List of players
        self.player_list = tk.Listbox(self.window, width=50)
        self.player_list.grid(row=1, column=0, rowspan=7, columnspan=3, padx=5, pady=5)
        # Order by name
        self.b_order_name = ttk.Button(
            self.window,
            text="Trier par nom",
            )
        self.b_order_name.grid(row=0, column=0, padx=5, pady=5)
        # Order by ranking
        self.b_order_rank = ttk.Button(
            self.window,
            text="Trier par classement",
            )
        self.b_order_rank.grid(row=0, column=1, padx=5, pady=5)
        # Display player information to change it
        self.b_show = ttk.Button(
            self.window,
            text="Afficher les infos",
            )
        self.b_show.grid(row=0, column=2, padx=5, pady=5)
        # Save button
        self.b_save = ttk.Button(
            self.window,
            text="Enregistrer les modifications",
            )
        self.b_save.grid(row=7, column=3, columnspan=4, padx=5, pady=5)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.grid(row=8, column=2, padx=5, pady=5)

    def cancel(self):
        self.window.destroy()

    def display_player_info(self, player):
        self.id.config(text=player.index)
        self.name.delete(0, tk.END)
        self.name.insert(0, player.name)
        self.first_name.delete(0, tk.END)
        self.first_name.insert(0, player.first_name)
        self.birthday.delete(0, tk.END)
        self.birthday.insert(0, player.birthday)
        self.ranking.delete(0, tk.END)
        self.ranking.insert(0, player.ranking)
        self.radio_value.set(player.sex)
