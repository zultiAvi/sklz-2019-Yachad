from GameObject import *

class Creature(GameObject):
    def __init__(self, game, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        GameObject(game, id, health, loc, owner, unique_id)
        self.attack_multiplier = attack_multiplier
        self.attack_range = attack_range
        self.max_speed = max_speed
        self.summoner = summoner
        self.summoning_duration= summoning_duration
        self.suffocation_per_turn = suffocation_per_turn

    def decrease_health_per_turn(self):
        self.decrease_health(self.suffocation_per_turn)


    def do_your_thing(self):
        pass
