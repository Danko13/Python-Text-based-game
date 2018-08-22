import random
import copy


class Team:
    '''
    team has many players
    team has a ranking in a league
    team plays games against other teams
    team has a single manager
    '''

    def __init__(self, name):
        self.name = name
        self.players = []

        self.wins = 0
        self.loses = 0

        self.money = 1000000

    def weekly_salary(self):
        salary = 0
        for player in self.players:
            salary += player.salary()
        return salary

    def pay_players(self):
        self.money -= self.weekly_salary()

    def rating(self):
        """
        what is the rating of the team
        """
        rating = 0
        for player in self.players:
            rating += player.skill
        return rating

    def __str__(self):
        return '{} {}'.format(self.name, self.rating())





