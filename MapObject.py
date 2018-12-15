from BaseObject import *

class MapObject(BaseObject):
    def __init__(self, game, loc):
        BaseObject("MapObject")
        self.location = loc
        self.game = game

    def get_game(self):
        return self.game

    def distance(self, other):
        return self.location.distance(other.location)

    def get_location(self):
        return self.location

    def in_map(self):
        map_size = self.game.get_map_size()
        return self.location.row >= 0 and self.location.row < map_size.row and \
               self.location.col >= 0 and self.location.col < map_size.col

    def in_range(self, other):
        return self.location.in_range(other.location)

