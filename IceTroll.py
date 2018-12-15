from Creature import *

class IceTroll(Creature):
    def __init__(self, game, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature.__init__(self, game, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)
        self.type = "IceTroll"

    def do_your_thing(self):
        if not self.is_alive():
            return

        opponent = self.game.get_opponent(self.owner)
        opponent_creatures = self.game.get_all_living_creatures(opponent)
        min_dist = 1000
        closest_creature = None
        for creature in opponent_creatures:
            dist = self.location.distance(creature.location)
            if dist < min_dist:
                min_dist = dist
                closest_creature = creature
        if closest_creature == None:
            return

        if self.in_range(closest_creature.location):
            self.game.set_attack(self, closest_creature)
        else:
            next_loc = self.location.towards(closest_creature.location, self.max_speed)
            self.game.move_to(self, next_loc)


