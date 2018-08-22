class Game:
    """
    plays a game between two teams
    game belongs to a league
    """

    def __init__(self, league, home_team, away_team):
        self.league = league

        self.home_team = home_team
        self.away_team = away_team

        self.home_team_won = None
        self.away_team_won = None

        print('{} vs. {}'.format(self.home_team, self.away_team))

    def play(self):
        """
        play the game, return who won
        True means the home team won, False means the away team won
        """
        print('Play begins')

        # insert a game here

        print('Game ends.')

        if self.home_team.rating() > self.away_team.rating():
            print('{} wins'.format(self.home_team))
            self.home_team_won = True
        else:
            print('{} wins'.format(self.away_team))
            self.away_team_won = True

        return True