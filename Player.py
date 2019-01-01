from BaseObject import *
import IceTroll
import LavaGiant
import Portal

class Player(BaseObject):
    def __init__(self, id, elves, mana, mana_per_turn, score, portals, castle, ice_trolls=None, lava_giants=None):
        BaseObject.__init__(self, "Player")
        self._opponent = None

        self.id = id
        self.all_elves = []
        self.living_elves = []
        self.update_all_elves(elves)

        self.ice_trolls = ice_trolls if ice_trolls is not None else []
        self.lava_giants = lava_giants if lava_giants is not None else []
        self.creatures = []
        self.update_creatures()
        self.mana = mana
        self.mana_per_turn = mana_per_turn
        self.score = score
        self.portals = portals if portals is not None else []
        self.castle = castle

    def set_opponent(self, o):
        self._opponent = o
    def get_opponent(self):
        return self._opponent

    def add_elf(self, elf):
        self.all_elves.append(elf)
        self.update_living_elves()

    def add_castle(self, castle):
        self.castle = castle

    def is_alive(self):
        return self.castle.current_health > 0

    def decrease_mana(self, cost):
        self.mana -= cost

    def update_mana_per_turn(self):
        self.mana += self.mana_per_turn

    def get_all_living_creatures(self):
        out = self.living_elves + self.creatures
        return out

    def get_all_buildings(self):
        c = self.castle
        p = self.portals
        return [c] + p

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

    def can_summon(self, cost):
        if self.mana < cost:
            return False
        return True

    def add_ice_troll(self, ice):
        self.ice_trolls.append(ice)
        self.update_creatures()

    def add_lava_giant(self, lava):
        self.lava_giants.append(lava)
        self.update_creatures()

    def remove_creatures(self):
        for index, ice in enumerate(self.ice_trolls):
            if not ice.is_alive():
                del (self.ice_trolls[index])

        for index, lava in enumerate(self.lava_giants):
            if not lava.is_alive():
                del (self.lava_giants[index])

        self.update_creatures()

    def remove_ice_troll(self, ice):
        index = self.find_creature(ice, self.ice_trolls)
        if index != -1:
            del (self.ice_trolls[index])
            self.update_creatures()

    def remove_lava_giant(self, lava):
        index = self.find_creature(lava, self.lava_giants)
        if index != -1:
            del (self.lava_giants[index])
        self.update_creatures()

    def add_portal(self, port):
        self.portals.append(port)

    def remove_portals(self):
        for p in self.portals:
            if not p.is_alive():
                del (p)

    def do_your_thing(self):
        for elf in self.all_elves:
            elf.do_your_thing()
            if not elf.is_alive():
                self.update_living_elves()

        self.remove_portals()
        for p in self.portals:
            p.do_your_thing()

        for c in self.creatures:
            c.do_your_thing()
            if not c.is_alive():
                if c.type == "IceTroll":
                    self.remove_ice_troll(c)
                if c.type == "LavaGiant":
                    self.remove_lava_giant(c)

    @staticmethod
    def find_creature(c_to_find, creatures_list):
        for i, c in enumerate(creatures_list):
            if c_to_find.id == c.id:
                return i
        return -1

    def do_your_things(self):
        for c in self.creatures:
            c.do_your_thing()

        for p in self.portals:
            p.do_your_thing()

        for e in self.living_elves:
            e.do_your_thing()

    def have_enough_mana(self, game):
        current_mana = game.get_my_mana()
        for p in self.portals:
            current_mana -= p.need_mana()
        for e in self.living_elves:
            current_mana -= e.need_mana()

        if current_mana < 0:
            return False
        else:
            return True

    def clean_mana_operations(self):
        for p in self.portals:
            p.clean_action_with_mana()

        for e in self.living_elves:
            if e.need_mana() > 0:
                e.clean_action_with_mana()

    def update_mana(self):
        current_mana = self.mana
        for p in self.portals:
            current_mana -= p.need_mana()
        for e in self.living_elves:
            current_mana -= e.need_mana()

        self.mana = current_mana

    def update_score(self, game):
        pass

    def set_actions(self):
        for p in self.portals:
            p.set_action()

        self.remove_portals()

        for e in self.living_elves:
            e.set_action()

        for c in self.creatures:
            c.set_action()

        self.remove_creatures()
