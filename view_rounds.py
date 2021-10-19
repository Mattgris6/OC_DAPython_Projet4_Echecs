import tkinter as tk
from tkinter import ttk


class ViewRounds():
    def __init__(self, tournament):
        self.tournament = tournament
        self.window = tk.Tk()
        w = 800  # width for the self.window
        h = 250  # height for the self.window
        # get screen width and height
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the self.window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.title('Rounds')
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.resizable(False, False)