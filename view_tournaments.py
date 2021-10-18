import tkinter as tk
from tkinter import ttk


class ViewTournaments():
    def __inti__(self):
        self.window = tk.Tk()
        w = 800  # width for the self.window
        h = 300  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Historic of Tournaments')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        # List of Tournaments
        self.tournament_list = tk.Listbox(self.window, width=50)
        self.tournament_list.grid(row=1, column=0, rowspan=7, columnspan=3, padx=5, pady=5)
        # Info of one tournament
        self.l_name = ttk.Label(self.window, text="Nom du tournoi : ")
        self.l_name.grid(row=1, column=3, padx=5, pady=5)
        self.l_location = ttk.Label(self.window, text="Lieu du tournoi : ")
        self.l_location.place(row=2, column=3, padx=5, pady=5)
        self.l_date = ttk.Label(self.window, text="Date du tournoi : ")
        self.l_date.place(row=3, column=3, padx=5, pady=5)
        self.l_round = ttk.Label(self.window, text="Nombre de tours : ")
        self.l_round.place(row=4, column=3, padx=5, pady=5)
        self.l_time_system = ttk.Label(
            self.window,
            text="Système de temps : ",
            )
        self.l_time_system.place(row=5, column=3, padx=5, pady=5)
        self.l_describe = ttk.Label(self.window, text="Description : ")
        self.l_describe.place(row=6, column=3, padx=5, pady=5)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.grid(row=8, column=2, padx=5, pady=5)

    def cancel(self):
        self.window.destroy()