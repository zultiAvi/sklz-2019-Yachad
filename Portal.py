from Building import *

class Portal(Building):
    def __init__(self, game, id, health, loc, owner, unique_id, size, turns_to_summon):
        Building(game, id, health, loc, owner, unique_id, size)
        self.in_summoning = None
        self.is_summoning = False
        self.turns_to_summon = turns_to_summon
        self.init_turns_to_summon = turns_to_summon

    def can_summon_ice_troll(self):
        return self.game.can_summon_ice_troll(self)

    def can_summon_lava_giant(self):
        return self.game.can_summon_lava_giant(self)

    def summon_ice_troll(self):
        if self.can_summon_ice_troll():
            self.game.summon_ice_troll(self)
            self.is_summoning = True
            self.in_summoning = "IceTroll"

    def summon_lava_giant(self):
        if self.can_summon_lava_giant():
            self.game.summon_lava_giant(self)
            self.is_summoning = True
            self.in_summoning = "LavaGiant"

