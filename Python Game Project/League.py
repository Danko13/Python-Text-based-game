import random
import copy
from Game import Game

class League:
    """
    league has many teams
    each team is going to have a ranking within this league
    """

    def __init__(self, name, teams, players):
        self.name = name
        self.teams = teams
        self.players = players
        self.rounds_played = 0



    def play_round(self):
        """
        play a round, which is 3 games
        """
        print('Round begins')
        num_teams = len(self.teams)
        num_games = num_teams // 2

        teams_to_play = copy.copy(self.teams)

        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            game.play()
            self.resolve_game(game)

        print('Round ends')
        self.rounds_played += 1
        # ladder/table status
        self.ladder()

    def ladder(self):
        for team in sorted(self.teams, key=lambda t: -t.wins):  # minus is for reverse order
            print('{} {} wins'.format(team, team.wins))

    def resolve_game(self, game):
        if game.home_team_won:
            # home team won
            game.home_team.wins += 1
            game.away_team.loses += 1
            game.home_team.money += round(200000 * random.random(),2)
        else:
            # away team won
            game.away_team.wins += 1
            game.home_team.loses += 1
            game.away_team.money += round(200000 * random.random(),2)

        game.home_team.pay_players()
        game.away_team.pay_players()
