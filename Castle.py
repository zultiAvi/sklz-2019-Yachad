from Building import *

class Castle(Building):
    def __init__(self, id, health, loc, owner, unique_id, size):
        Building.__init__(self, id, health, loc, owner, unique_id, size)
        self.type = "Castle"

    def __str__(self):
        return "{Castle: %s, %s, %s}" % (self.id, self.current_health, self.location)

    