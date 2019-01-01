from Creature import Creature
from BaseObject import get_game

class LavaGiant(Creature):
    def __init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature.__init__(self, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)
        self.type = "LavaGiant"

    def __str__(self):
        return "{Lava Giant: %s, %s, %s}" % (self.id, self.current_health, self.location)

    def do_your_thing(self):
        if not self.is_alive():
            return

        opponent = self.owner.get_opponent()
        opponent_castle = opponent.castle
        game = get_game(self.owner)
        if self.in_range(opponent_castle.location, self.attack_range):
            self._action = "attack"
            self._attack_object = opponent_castle
            game.debug("Lava Giant %s attacks Castle %s" %(self, opponent_castle))
        else:
            next_loc = self.location.towards(opponent_castle.location, self.max_speed)
            self._action = "move"
            self._next_location = next_loc
            game.debug("Lava Giant %s move to %s on his way to Castle %s" %(self, next_loc, opponent_castle))

if __name__ == '__main__':
    lava = LavaGiant(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    print lava.is_alive()
