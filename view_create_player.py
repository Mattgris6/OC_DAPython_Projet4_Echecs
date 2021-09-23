from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from modele import Joueur
# from tkinter import *


class CreatePlayer():
    def __init__(self):
        self.window = Tk()
        w = 300 # width for the self.window
        h = 200 # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Nouveau joueur')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        # Get player infos
        self.new_player = None
        self.label_name = ttk.Label(self.window, text="Nom : ")
        self.label_name.grid(row=1, column=1, padx=5, pady=5)
        self.name = ttk.Entry(self.window, width=25)
        self.name.grid(row=1, column=2, padx=5, pady=5)
        self.label_name2 = ttk.Label(self.window, text="Prénom : ")
        self.label_name2.grid(row=2, column=1, padx=5, pady=5)
        self.name2 = ttk.Entry(self.window, width=25)
        self.name2.grid(row=2, column=2, padx=5, pady=5)
        self.label_birthday = ttk.Label(self.window, text="Date de naissance : ")
        self.label_birthday.grid(row=3, column=1, padx=5, pady=5)
        self.birthday = ttk.Entry(self.window, width=25)
        self.birthday.grid(row=3, column=2, padx=5, pady=5)
        self.label_classement = ttk.Label(self.window, text="Classement : ")
        self.label_classement.grid(row=4, column=1, padx=5, pady=5)
        self.classement = ttk.Entry(self.window, width=25)
        self.classement.grid(row=4, column=2, padx=5, pady=5)
        self.radio_value = StringVar(self.window)
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
            command=self.save_player,
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

    def save_player(self):
        self.new_player = Joueur(self.name.get(), self.name2.get(), self.birthday.get(), self.radio_value.get(), self.classement.get())
        self.window.destroy()

    def run(self):
        self.window.wait_window()
        return self.new_player
