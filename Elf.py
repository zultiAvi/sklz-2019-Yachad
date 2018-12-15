from GameObject import *

class Elf (GameObject):
    def __init__(self, id, init_health, initial_loc, owner, unique_id, attack_multiplier, attack_range, max_speed, turns_to_revive):
        GameObject.__init__(self, id, init_health, initial_loc, owner, unique_id)
        self.type = "Elf"

        self.attack_multiplier = attack_multiplier
        self.attack_range = attack_range
        self.currently_building = None
        self.is_building = False
        self.max_speed = max_speed
        self.spawn_turns = 0
        self.turns_to_revive = turns_to_revive

    def attack(self, target):
        if self.location.in_range(target.location):
            self.game.set_attack(self, target.unique_id)

    def build_portal(self):
        if self.game.can_build_portal_at(self,self.location):
            self.game.build_portal(self)
            self.is_building = True
            self.currently_building = "Portal"

    def can_build_portal(self):
        return self.game.can_build_portal_at(self, self.location)

    def in_attack_range(self, object):
        return self.location.in_range(object.location, self.attack_range)

    def is_alive(self):
        return self.current_health > 0

    def move_to(self, object):
        self.game.move_to(self, self.location.towards(object.location, self.max_speed))




