from datetime import datetime
from typing import List
from copy import deepcopy

joueurs = [['Matthieu', 'Grison', '20/12/1992', 'Homme', 6],
            ['Pierre', 'Grison', '16/11/1994', 'Homme', 7],
            ['Joseph', 'Grison', '10/04/1985', 'Homme', 2],
            ['Jean-Baptiste', 'Grison', '04/06/1983', 'Homme', 1],
            ['Jeanne', 'Grison', '22/06/1991', 'Femme', 5],
            ['Blandine', 'Grison', '18/09/1988', 'Femme', 4],
            ['Helene', 'Grison', '11/03/1987','Femme', 3],
            ['Catherine', 'Grison', '13/12/1956', 'Femme', 8]]


class Player():
    def __init__(self, name, first_name, birthday, sex, ranking=0, index=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.points = 0
        self.index = index

    @property
    def serial_player(self):
        s_player = {
                'name': self.name,
                'first_name': self.first_name,
                'birthday': self.birthday,
                'sex': self.sex,
                'ranking': self.ranking,
            }
        return s_player

class Tournament():
    NB_PLAYERS = 8
    def __init__(self, name, location, time_system='bullet', nb_round=4, description='', index=0):
        self.name = name
        self.location = location
        self.date_tournament = datetime.now().strftime("%d/%m/%Y")
        self.time_system = time_system
        self.nb_round = nb_round
        self.players : List[Player] = []
        self.rounds : List[Round] = []
        self.description = description
        self.index = index

    @property
    def serial_tournament(self):
        s_tournament = {
            'name': self.name,
            'locaion': self.location,
            'date_tournament': self.date_tournament,
            'time_system': self.time_system,
            'nb_round': self.nb_round,
            'description': self.description,
            'rounds': [round.serial_round for round in self.rounds],
            'players': [player.index for player in self.players],
        }
        return s_tournament


class Round():
    def __init__(self, name):
        self.name = name
        self.date_begin = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_end = None
        self.matchs = []

    @property
    def serial_round(self):
        print(self.name, self.matchs)
        new_matchs = deepcopy(self.matchs)
        print('Nouvelle liste : ', new_matchs)
        for new_match in new_matchs:
            new_match[0][0] = new_match[0][0].index
            new_match[1][0] = new_match[1][0].index
        print(self.name, self.matchs)
        print('Nouvelle liste : ', new_matchs)
        s_round = {
            'name': self.name,
            'date_begin': self.date_begin,
            'date_end': self.date_end,
            'matchs': new_matchs,
        }
        return s_round