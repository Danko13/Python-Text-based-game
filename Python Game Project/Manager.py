from Team import Team
from League import League
from Helpers import select_from_menu


class TeamManager:
    '''
    manager runs a team
    '''
    def __init__(self, team, league):
        self.team = team
        self.league = league

        self.inputs = {
            1: self.view_players,
            2: self.view_market,
            3: self.trade_players,
            4: self.next_round
        }
        self.finished = False

        print ('You are a manager')
        print ('You manage {}'.format(self.team))
        print ('Good luck')

    def manage(self):
        '''
        before every round, we can make changes as a manager
        '''
        self.finished = False
        print ('')

        print ('Your team is {}'.format(self.team))
        print ('You have {} wins out of {} games'.format(self.team.wins, self.league.rounds_played))
        print ('You currently have ${} budget'.format(self.team.money))
        print ('Your team salary ${} a week'.format(self.team.weekly_salary()))

        print ('')

        while not self.finished:
            self.print_menu()
            select_from_menu(self.inputs)


        print('')

    def print_menu(self):
        print ('1. View your team players')
        print ('2. View players on the market')
        print ('3. Trade players')
        print ('4. Play the next round')

    def view_players(self):
        for i, player in enumerate(self.team.players):
            print ('{}: {}'.format(i, player))

    def view_market(self):
        for i, player in enumerate(self.league.players):
            print ('{}: {}'.format(i, player))

    def trade_players(self):
        '''
        switch a player from your team for a free agent player
        '''
        # select a player from your team
        self.view_players()
        player_index = int(input('Which player you want to switch? '))
        print('')

        # select a player from the free agents
        self.view_market()
        market_index = int(input('Which player you want to hire? '))
        print('')

        # switch em
        print ('')
        print ('Switching {} for {}'.format(self.team.players[player_index],self.league.players[market_index]))
        player_from_team = self.team.players.pop(player_index)
        player_from_market = self.league.players.pop(market_index)

        self.team.players.append(player_from_market)
        self.league.players.append(player_from_team)

    def next_round(self):
        print ('Next round!')
        self.finished = True