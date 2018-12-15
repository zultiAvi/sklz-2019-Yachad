from Creature import *

class LavaGiant(Creature):
    def __init__(self, game, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed, summoner, summoning_duration, suffocation_per_turn):
        Creature(self, game, id, health, loc, owner, unique_id, attack_multiplier, attack_range, max_speed,summoner, summoning_duration, suffocation_per_turn)

    def do_your_thing(self):
        if not self.is_alive():
            return

        opponent = self.game.get_opponent(self.owner)
        opponent_castle = self.game.get_castle(opponent)
        if self.in_range(opponent_castle.location):
            self.game.set_attack(self, opponent_castle)
        else:
            next_loc = self.location.towards(opponent_castle.location, self.max_speed)
            self.game.move_to(self, next_loc)
