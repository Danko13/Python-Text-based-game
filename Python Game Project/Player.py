import random

class Player:
    """
    player is on a single team, with many other players
    players play in a game for a team
    """

    def __init__(self, name, skill):
        self.name = name

        # player skill ranking
        self.skill = skill

    def salary(self):
        return 5000 + self.skill * 100

    def __str__(self):
        return '{} Skill: {} Salary: {}'.format(self.name, self.skill, self.salary())


def generate_player():
    first_names = [
        'Sophia',
        'Jackson',
        'Emma',
        'Aiden',
        'Olivia',
        'Lucas',
        'Ava',
        'Liam',
        'Mia',
        'Noah',
        'Isabella',
        'Ethan',
        'Riley',
        'Mason',
        'Aria',
        'Caden',
        'Zoe',
        'Oliver',
        'Charlotte',
        'Elijah',
        'Lily',
        'Grayson',
        'Layla',
        'Jacob',
        'Amelia',
        'Michael',
        'Emily',
        'Benjamin',
        'Madelyn',
        'Carter',
        'Aubrey',
        'James',
        'Adalyn',
        'Jayden',
        'Madison',
        'Logan',
        'Chloe',
        'Alexander',
        'Harper',
        'Caleb',
        'Abigail',
        'Ryan',
        'Aaliyah',
        'Luke',
        'Avery',
        'Daniel',
        'Evelyn',
        'Jack',
        'Kaylee',
        'William',
        'Ella',
        'Owen',
        'Ellie',
        'Gabriel',
        'Scarlett',
        'Matthew',
        'Arianna',
        'Connor',
        'Hailey',
        'Jayce',
        'Nora',
        'Isaac',
        'Addison',
        'Sebastian',
        'Brooklyn',
        'Henry',
        'Hannah',
        'Muhammad',
        'Mila',
        'Cameron',
        'Leah',
        'Wyatt',
        'Elizabeth',
        'Dylan',
        'Sarah',
        'Nathan',
        'Eliana',
        'Nicholas',
        'Mackenzie',
        'Julian',
        'Peyton',
        'Eli',
        'Maria',
        'Levi',
        'Grace',
        'Isaiah',
        'Adeline',
        'Landon',
        'Elena',
        'David',
        'Anna',
        'Christian',
        'Victoria',
        'Andrew',
        'Camilla',
        'Brayden',
        'Lillian',
        'John',
        'Natalie',
        'Lincoln',
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(first_names)
    full_name = '{} {}'.format(first_name, last_name)

    skill = 10 + random.randint(0,100)
    return Player(full_name, skill)
