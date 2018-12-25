from Creature import Creature

class IceTroll(Creature):
    def __init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature.__init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)
        self.type = "IceTroll"
        self.action = ""
        self.attack_object = None
        self.next_location = None

    def do_your_thing(self):
        if not self.is_alive():
            return

        opponent = self.owner.get_opponent()
        opponent_creatures = opponent.get_all_living_creatures()
        min_dist = 1000
        closest_creature = None
        for creature in opponent_creatures:
            dist = self.location.distance(creature.location)
            if dist < min_dist:
                min_dist = dist
                closest_creature = creature
        if closest_creature is None:
            return

        if self.in_range(closest_creature.location, self.attack_range):
            self._action = "attack"
            self._attack_object = closest_creature
        else:
            next_loc = self.location.towards(closest_creature.location, self.max_speed)
            self._action = "move"
            self._next_location = next_loc
