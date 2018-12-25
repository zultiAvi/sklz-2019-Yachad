import random

games = [None, None]
players = [None, None]

def get_game(owner):
    global games

    if owner.id < 0 or owner.id > 1:
        return games[0]

    return games[owner.id]


class BaseObject:
    def __init__(self, t):
        self.type = t
        self.rnd = random.randint(0,100000)

    def __hash__(self):
        c = [int(x) for x in self.__str__()]
        return sum(c)

    def __str__(self):
        return "Type: %s. %s" % (self.type, self.rnd)

    def equals(self, other):
        return self.type == other.type
