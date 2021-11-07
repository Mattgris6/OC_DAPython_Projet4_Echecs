import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image


class MainMenu():
    """Home page"""
    def __init__(self):
        self.window = tk.Tk()
        # Fix width and height for the self.window
        w = 300
        h = 200
        # Get screen width and height
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        # Calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Gestionnaire de tournoi')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)
        self.label_menu = ttk.Label(self.window, text="Menu principal")
        self.label_menu.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        # We create all buttons we need for home page
        self.button_new_tournament = ttk.Button(
            self.window,
            text="Nouveau tournoi",
            )
        self.button_new_tournament.place(relx=0.1, rely=0.25)
        self.button_historic = ttk.Button(
            self.window,
            text="Historique",
            )
        self.button_historic.place(relx=0.1, rely=0.4)
        self.button_players = ttk.Button(
            self.window,
            text="Joueurs",
            )
        self.button_players.place(relx=0.1, rely=0.55)
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.window.destroy,
            )
        self.button_quit.place(relx=0.8, rely=0.9, anchor=tk.CENTER)
        # Insert an image of chess
        main_path = os.path.abspath(os.path.dirname(__file__))
        image_file = main_path + r'/../Ressources/image_menu.png'
        image_menu = Image.open(image_file)
        image_menu = image_menu.resize((105, 105), Image.ANTIALIAS)
        image_menu = ImageTk.PhotoImage(image_menu)
        self.canvas_image = tk.Canvas(
            self.window,
            width=100,
            height=100,
            bg='blue',
            )
        self.canvas_image.create_image(0, 0, anchor=tk.NW, image=image_menu)
        self.canvas_image.image = image_menu
        self.canvas_image.place(relx=0.9, rely=0.2, anchor=tk.NE)
