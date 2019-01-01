from Creature import Creature
from BaseObject import get_game

class IceTroll(Creature):
    def __init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature.__init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)
        self.type = "IceTroll"
        self.action = ""
        self.attack_object = None
        self.next_location = None

    def __str__(self):
        return "{Ice Troll: %s, %s, %s}" % (self.id, self.current_health, self.location)

    def do_your_thing(self):
        if not self.is_alive():
            return

        game = get_game(self.owner)
        opponent = self.owner.get_opponent()
        opponent_creatures = opponent.get_all_living_creatures()
        min_dist = 100000
        closest_creature = None
        for c in opponent_creatures:
            dist = self.location.distance(c.location)
            if dist < min_dist:
                min_dist = dist
                closest_creature = c
        if closest_creature is None:
            return

        if self.in_range(closest_creature.location, self.attack_range):
            self._action = "attack"
            self._attack_object = closest_creature
            game.debug("Ice Troll %s attacks Opponent creature %s" %(self, closest_creature))
        else:
            next_loc = self.location.towards(closest_creature.location, self.max_speed)
            self._action = "move"
            self._next_location = next_loc
            game.debug("Ice Troll %s move to %s on his way to Opponent Creature %s" %(self, next_loc, closest_creature))
