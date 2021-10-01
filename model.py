from datetime import datetime
from typing import List

joueurs = [['Matthieu', 'Grison', '20/12/1992', 'Homme', 6000],
            ['Pierre', 'Grison', '16/11/1994', 'Homme', 7000],
            ['Joseph', 'Grison', '10/04/1985', 'Homme', 2000],
            ['Jean-Baptiste', 'Grison', '04/06/1983', 'Homme', 1000],
            ['Jeanne', 'Grison', '22/06/1991', 'Femme', 5000],
            ['Blandine', 'Grison', '18/09/1988', 'Femme', 4000],
            ['Helene', 'Grison', '11/03/1987','Femme', 3000],
            ['Catherine', 'Grison', '13/12/1956', 'Femme', 500]]


class Player():
    def __init__(self, name, first_name, birthday, sex, ranking=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.points = 0


class Tournament():
    NB_PLAYERS = 8
    def __init__(self, name, location, time_system='bullet', nb_round=4, description=''):
        self.name = name
        self.location = location
        self.date_tournament = datetime.now().strftime("%d/%m/%Y")
        self.time_system = time_system
        self.nb_round = nb_round
        self.players : List[Player] = []
        self.rounds : List[Round] = []
        self.description = description


class Round():
    def __init__(self, name):
        self.name = name
        self.date_begin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_end = None
        self.matchs = []