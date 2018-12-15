from Building import *

class Castle(Building):
    def __init__(self, id, health, loc, owner, unique_id, size):
        Building.__init__(self, id, health, loc, owner, unique_id, size)
        self.type = "Castle"

    