from GameObject import *

class Building (GameObject):
    def __init__(self, game, id, health, loc, owner, unique_id, size):
        GameObject(game, id, health, loc, owner, unique_id)
        self.size = size
