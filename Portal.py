from Building import *
from BaseObject import get_game


class Portal(Building):
    def __init__(self, b_id, health, loc, owner, unique_id, size, turns_to_summon):
        Building.__init__(self, b_id, health, loc, owner, unique_id, size)
        self.type = "Portal"
        self.in_summoning = None
        self.is_summoning = False
        self.turns_to_summon = 0
        self.init_turns_to_summon = turns_to_summon

        self._need_mana = 0
        self._action = ""
        self._duration = 0

    def __str__(self):
        return "{Portal: %s, %s, %s}" % (self.id, self.current_health, self.location)

    def can_summon_ice_troll(self):
        if self.is_summoning:
            return False

        game = get_game(self.owner)
        return game.can_owner_summon_ice_troll()

    def can_summon_lava_giant(self):
        if self.is_summoning:
            return False
        game = get_game(self.owner)
        return game.can_owner_summon_lava_giant()

    def summon_ice_troll(self):
        if self.is_summoning:
            return
        if self._need_mana > 0:
            self._need_mana = 100000
            return
        game = get_game(self.owner)
        self._action = "IceTroll"
        self._need_mana = game.ice_troll_cost
        self._duration = game.ice_troll_summoning_duration
        self.already_acted = True

    def summon_lava_giant(self):
        if self.is_summoning:
            return
        if self._need_mana > 0:
            self._need_mana = 100000
            return
        game = get_game(self.owner)
        self._need_mana = game.lava_giant_cost
        self._action = "LavaGiant"
        self._duration = game.lava_giant_summoning_duration
        self.already_acted = True

    def do_your_thing(self):
        if self.turns_to_summon == 0 or not self.is_summoning:
            return
        self.turns_to_summon -= 1

        if self.turns_to_summon == 0:
            game = get_game(self.owner)
            game.create_creature(self.in_summoning, self.location, self)
            self.in_summoning = ""
            self.is_summoning = False

    def need_mana(self):
        return self._need_mana

    def clean_action_with_mana(self):
        if self._need_mana > 0:
            self._need_mana = 0
            self._action = ""
            self._duration = 0
            self.already_acted = False

    def set_action(self):
        if self._action == "":
            return

        self.is_summoning = True
        self.in_summoning = self._action
        self.turns_to_summon = self._duration
        self.owner.decrease_mana(self._need_mana)

        self._action = ""
        self._need_mana = 0
        self._duration = 0
        self.already_acted = False

if __name__ == '__main__':
    class own:
        def __init__(self):
            self.id = 0
    port = Portal(0, 0, 0, own(), 0, 0, 0)

    print port.is_alive()
