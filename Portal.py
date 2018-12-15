from Building import *
from elf_kingdom import get_game

class Portal(Building):
    def __init__(self, id, health, loc, owner, unique_id, size, turns_to_summon):
        Building.__init__(self, id, health, loc, owner, unique_id, size)
        global game
        self.game = get_game(owner)

        self.type = "Portal"
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

