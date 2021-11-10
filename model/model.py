from datetime import datetime
from typing import List
from copy import deepcopy


class Player():
    def __init__(self, name, first_name, birthday, sex, ranking=0, id=0):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.id = id

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

    def set_points(self, tournament):
        points = 0
        for round in tournament.rounds:
            for match in round.matchs:
                if match[0][0].id == self.id:
                    points += match[0][1]
                    break
                elif match[1][0].id == self.id:
                    points += match[1][1]
                    break
        return points


class Tournament():
    NB_PLAYERS = 8

    def __init__(self, name, location, time_system='bullet', nb_round=4, description='', id=0):
        self.name = name
        self.location = location
        self.date_tournament = datetime.now().strftime("%d/%m/%Y")
        self.time_system = time_system
        self.nb_round = nb_round
        self.players: List[Player] = []
        self.rounds: List[Round] = []
        self.description = description
        self.id = id

    @property
    def serial_tournament(self):
        s_tournament = {
            'name': self.name,
            'location': self.location,
            'date_tournament': self.date_tournament,
            'time_system': self.time_system,
            'nb_round': self.nb_round,
            'description': self.description,
            'rounds': [round.serial_round for round in self.rounds],
            'players': [player.id for player in self.players],
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
        new_matchs = deepcopy(self.matchs)
        for new_match in new_matchs:
            new_match[0][0] = new_match[0][0].id
            new_match[1][0] = new_match[1][0].id
        s_round = {
            'name': self.name,
            'date_begin': self.date_begin,
            'date_end': self.date_end,
            'matchs': new_matchs,
        }
        return s_round
