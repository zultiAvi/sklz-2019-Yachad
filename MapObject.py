from BaseObject import BaseObject

class MapObject(BaseObject):
    def __init__(self, loc):
        BaseObject.__init__(self, "MapObject")
        self.location = loc
        self.alive = True

    def is_alive(self):
        return self.alive

    def distance(self, other):
        if not self.is_alive():
            return None
        return self.location.distance(other.location)

    def get_location(self):
        if not self.is_alive():
            return None
        return self.location

    def in_map(self):
        global map_size
        return self.location.row >= 0 and self.location.row < map_size.row and \
               self.location.col >= 0 and self.location.col < map_size.col

    def in_range(self, other, range):
        if not self.is_alive():
            return None
        return self.location.in_range(other.location, range)

