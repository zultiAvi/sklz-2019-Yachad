from Building import *

class Castle(Building):
    def __init__(self, game, id, health, loc, owner, unique_id, size):
        Building(game, id, health, loc, owner, unique_id, size)

    