from tkinter.messagebox import *
from tkinter import *
import os
from view_create_tournament import CreateTournament
from PIL import ImageTk, Image

class MainMenu():
    """Home page"""
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
        self.window.title('Gestionnaire de tournoi')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.label_menu = Label(self.window, text="Menu principal")
        self.label_menu.place(relx = 0.5, rely = 0.1, anchor=CENTER)
        # We create all buttons we need for home page
        self.button_new_tournament = Button(
            self.window,
            text="Nouveau tournoi",
            command=self.new_tournament
            )
        self.button_new_tournament.place(relx = 0.1, rely = 0.25)
        self.button_historic = Button(
            self.window,
            text="Historique",
            command=self.historic
            )
        self.button_historic.place(relx = 0.1, rely = 0.4)
        self.button_players = Button(
            self.window,
            text="Joueurs",
            command=self.players
            )
        self.button_players.place(relx = 0.1, rely = 0.55)
        self.button_quit=Button(
            self.window,
            text="Fermer",
            command=self.window.destroy
            )
        self.button_quit.place(relx = 0.9, rely = 0.9, anchor=CENTER)
        # Insert an image of chess
        image_file = os.path.abspath(os.path.dirname(__file__)) + r'/Ressources/image_menu.png'
        image_menu = Image.open(image_file)
        image_menu = image_menu.resize((105,105), Image.ANTIALIAS)
        image_menu = ImageTk.PhotoImage(image_menu)
        self.canvas_image = Canvas(self.window, width=100, height=100, bg='blue')
        self.canvas_image.create_image(0, 0, anchor=NW, image=image_menu)
        self.canvas_image.image = image_menu
        self.canvas_image.place(relx = 0.9, rely = 0.2, anchor=NE)

    def new_tournament(self):
        """Run the page to create a new tournament"""
        tournoi = CreateTournament()
        tournoi.run()

    def historic(self):
        """Show the page of Historic"""
        showinfo("Historique", "Historique!")

    def players(self):
        """Show all players in base"""
        showinfo("Joueurs", "Joueurs!")

    def run(self):
        """Show the home page"""
        self.window.mainloop()