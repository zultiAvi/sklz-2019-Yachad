from BaseObject import *

class Player(BaseObject):
    def __init__(self, id, elves, mana, mana_per_turn, score, portals, castle, ice_trolls=None, lava_giants=None):
        BaseObject.__init__(self, "Player")

        self.id = id
        self.update_all_elves(elves)

        self.ice_trolls = ice_trolls if ice_trolls is not None else []
        self.lava_giants = lava_giants if lava_giants is not None else []
        self.update_creatures()
        self.mana = mana
        self.mana_per_turn = mana_per_turn
        self.score = score
        self.portals = portals if portals is not None else []
        self.castle = castle

    def is_alive(self):
        return self.castle.current_health > 0

    def get_all_buildings(self):
        c = self.castle
        p = self.portals
        return [c].append(p)

    def update_all_elves(self, elves):
        self.all_elves = elves if elves is not None else []
        self.update_living_elves()

    def update_living_elves(self):
        self.living_elves = []
        for elf in self.all_elves:
            if elf.is_alive():
                self.living_elves.append(elf)

    def update_creatures(self):
        self.creatures = self.ice_trolls + self.lava_giants

    def do_turn(self, game):
        # do_turn(self, game)
        pass

