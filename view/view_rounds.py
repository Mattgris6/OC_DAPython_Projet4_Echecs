import tkinter as tk
from tkinter import Canvas, ttk
from tkinter.constants import LEFT


class ViewRounds():
    def __init__(self):
        self.window = tk.Tk()
        w = 400  # width for the self.window
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
        self.label_frame = tk.LabelFrame(self.window, width=400, height=200)
        self.label_frame.propagate(0)
        self.canvas = Canvas(self.label_frame)
        self.canvas.pack(side=LEFT, fill="both", expand='yes')
        # Adding a scrollbar
        y_scrollbar = ttk.Scrollbar(self.label_frame, orient="vertical", command=self.canvas.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=y_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.label_frame.pack(pady=5)
        # Quit window
        self.button_quit = ttk.Button(
            self.window,
            text="Fermer",
            command=self.cancel,
            )
        self.button_quit.pack(pady=5)

    def cancel(self):
        self.window.destroy()

    def display_rounds(self, tournament):
        for round in tournament.rounds:
            l_name = tk.Label(self.frame, text=round.name)
            l_name.pack()
            for match in round.matchs:
                player1 = f'{match[0][0].first_name} {match[0][0].name}'
                player2 = f'{match[1][0].first_name} {match[1][0].name}'
                score = f'{match[0][1]}-{match[1][1]}'
                text_display = f'{player1} vs {player2} : {score}'
                l_match = tk.Label(self.frame, text=text_display)
                l_match.pack()
