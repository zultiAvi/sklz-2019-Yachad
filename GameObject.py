from MapObject import *

class GameObject (MapObject):

    def __init__(self, game, id, init_health, initial_loc, owner, unique_id):
        MapObject(game, initial_loc)

        self.id = id
        self.current_health = init_health
        self.already_acted = False
        self.initial_location = initial_loc
        self.owner = owner
        self.unique_id = unique_id
        self.type = "GameObject"

    def decrease_health(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def is_alive(self):
        return self.current_health > 0
