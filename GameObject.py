from MapObject import *

class GameObject (MapObject):

    def __init__(self, id, init_health, initial_loc, owner, unique_id):
        MapObject.__init__(self, initial_loc)
        self.type = "GameObject"

        self.id = id
        self.current_health = init_health
        self.already_acted = False
        self.initial_location = initial_loc
        self.owner = owner
        self.unique_id = unique_id

    def is_alive(self):
        return self.current_health > 0

    def decrease_health(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
