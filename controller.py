from view_main_menu import MainMenu
from view_create_tournament import CreateTournament
from view_create_player import CreatePlayer

class Controller():
    def __init__(self):
        # Initialize the different windows of the app 
        self.view_main_menu = MainMenu()
        self.view_create_tournament = CreateTournament()
        # self.view_create_player = CreatePlayer()
        # Config the callback
        # self.view_main_menu.button_new_tournament.config(command=self.new_tournament)
        self.view_main_menu.button_historic.config(command=self.historic)
        self.view_main_menu.button_players.config(command=self.players)
        
    def new_tournament(self):
        """Run the page to create a new tournament"""
        # tournament = self.view_create_tournament.run()
        if tournament:
            tournament_menu = TournamentMenu(tournament)

    def historic(self):
        """Show the page of Historic"""
        showinfo("Historique", "Historique!")

    def players(self):
        """Show all players in base"""
        showinfo("Joueurs", "Joueurs!")

    def run(self):
        """Show the home page"""
        self.view_main_menu.window.mainloop()

    



app = Controller()
app.run()