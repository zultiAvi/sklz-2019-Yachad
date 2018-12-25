from Creature import Creature
from BaseObject import get_game

class LavaGiant(Creature):
    def __init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature.__init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)
        self.type = "LavaGiant"

    def do_your_thing(self):
        if not self.is_alive():
            return

        opponent = self.owner.get_opponent()
        opponent_castle = opponent.castle
        if self.in_range(opponent_castle.location, self.attack_range):
            self._action = "attack"
            self._attack_object = opponent_castle
        else:
            next_loc = self.location.towards(opponent_castle.location, self.max_speed)
            self._action = "move"
            self._next_location = next_loc

if __name__ == '__main__':
    lava = LavaGiant(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    print lava.is_alive()
