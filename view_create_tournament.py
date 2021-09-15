from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
import os

class CreateTournament():
    def __init__(self):
        self.window = Tk()
        self.window.title('Nouveau tournoi')
        self.window.geometry("600x300+0+0")
        # Get Tournament infos
        self.label_name = Label(self.window, text="Nom du tournoi : ")
        self.label_name.place(relx = 0.05, rely = 0.05)
        self.name = Entry(self.window, width=25)
        self.name.place(relx = 0.23, rely = 0.05)
        self.label_lieu = Label(self.window, text="Lieu du tournoi : ")
        self.label_lieu.place(relx = 0.05, rely = 0.15)
        self.lieu = Entry(self.window, width=25)
        self.lieu.place(relx = 0.23, rely = 0.15)
        self.label_round = Label(self.window, text="Nombre de tours : ")
        self.label_round.place(relx = 0.55, rely = 0.05)
        default_round = StringVar(self.window)
        default_round.set("4")
        self.round = Spinbox(self.window, from_=0, to=10, textvariable=default_round, width=5)
        self.round.place(relx = 0.75, rely = 0.05)
        self.label_temps = Label(self.window, text="Système de temps : ")
        self.label_temps.place(relx = 0.55, rely = 0.15)
        self.temps = ttk.Combobox(self.window, values=[
                                                    "Bullet",
                                                    "Blitz",
                                                    "Coup rapide"
                                                ], width=15)
        self.temps.place(relx = 0.75, rely = 0.15)
        # Quit window
        self.button_quit=Button(
            self.window,
            text="Fermer",
            command=self.window.destroy
            )
        self.button_quit.place(relx = 0.92, rely = 0.93, anchor=CENTER)

    def run(self):
        self.window.mainloop()