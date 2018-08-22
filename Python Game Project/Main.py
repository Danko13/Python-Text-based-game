import random
from Team import Team
from League import League
from Player import generate_player
from Manager import TeamManager


def Main():
    # set up our data

    # generate some players
    players = []
    for i in range (100):
        players.append(generate_player())

    # set up 6 teams
    teams = [
        Team('Milan'),
        Team('Juve'),
        Team('Inter'),
        Team('Roma'),
        Team('Napoli'),
        Team('Lazio')
    ]

    for team in teams:
        for player_num in range (11):
            # give them 11 starting players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            # restriction for players, to play for one team only
            players.remove(selected_player)

    # we have a single league
    first_league = League('Calcio Serie A', teams, players)

    # create the manager
    manager = TeamManager(random.choice(teams), first_league)

    print ('Season begins!')
    for i in range (10):
        manager.manage()
        first_league.play_round()
    print ('Season ends!')


if __name__ == '__main__':

    Main()