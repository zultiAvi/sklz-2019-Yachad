from GameObject import *

class Creature(GameObject):
    def __init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        GameObject.__init__(self, id, health, loc, owner, unique_id)
        self.type = "Creature"
        self.attack_multiplier = attack_multiplier
        self.attack_range = attack_range
        self.max_speed = max_speed
        self.summoner = summoner
        self.summoning_duration= summoning_duration
        self.suffocation_per_turn = suffocation_per_turn

        self._action = ""
        self._attack_object = None
        self._next_location = None

    def decrease_health_per_turn(self):
        self.decrease_health(self.suffocation_per_turn)

    def set_action(self):
        if self._action == "attack":
            self._attack_object.current_health -= self.attack_multiplier
        if self._action == "move":
            self.location = self._next_location

        self.decrease_health(self.suffocation_per_turn)