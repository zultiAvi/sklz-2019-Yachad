from GameObject import *

class Building (GameObject):
    def __init__(self, id, health, loc, owner, unique_id, size):
        GameObject.__init__(self, id, health, loc, owner, unique_id)
        self.type = "Building"
        self.size = size
