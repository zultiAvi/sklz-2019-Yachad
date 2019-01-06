from elf_kingdom import *
from LavaGiant import LavaGiant
from IceTroll import IceTroll
from Portal import Portal

class Game(BaseObject):
    def __init__(self, owner, enemy, mapa):
        BaseObject("Game")
        self.owner = owner
        self.enemy = enemy
        self.mapa = mapa
        self.last_uid = owner.id * 100000

        self.turn = mapa.turn
        self.cols = mapa.map_size.col
        self.rows = mapa.map_size.row
        self.max_points = mapa.castle_data.castle_max_health
        self.max_turns = mapa.max_turns
        self.castle_max_health = mapa.castle_data.castle_max_health
        self.castle_size = mapa.castle_data.castle_size
        self.default_mana_per_turn = mapa.default_mana_per_turn
        self.elf_attack_multiplier = mapa.elf_data.elf_attack_multiplier
        self.elf_attack_range = mapa.elf_data.elf_attack_range
        self.elf_max_health = mapa.elf_data.elf_max_health
        self.elf_spawn_turns = mapa.elf_data.elf_spawn_turns
        self.ice_troll_attack_multiplier = mapa.ice_troll_data.ice_troll_attack_multiplier
        self.ice_troll_attack_range = mapa.ice_troll_data.ice_troll_attack_range
        self.ice_troll_cost = mapa.ice_troll_data.ice_troll_cost
        self.ice_troll_max_health = mapa.ice_troll_data.ice_troll_max_health
        self.ice_troll_max_speed = mapa.ice_troll_data.ice_troll_max_speed
        self.ice_troll_suffocation_per_turn = mapa.ice_troll_data.ice_troll_suffocation_per_turn
        self.ice_troll_summoning_duration = mapa.ice_troll_data.ice_troll_summoning_duration
        self.lava_giant_attack_multiplier = mapa.lava_giant_data.lava_giant_attack_multiplier
        self.lava_giant_attack_range = mapa.lava_giant_data.lava_giant_attack_range
        self.lava_giant_cost = mapa.lava_giant_data.lava_giant_cost
        self.lava_giant_max_health = mapa.lava_giant_data.lava_giant_max_health
        self.lava_giant_max_speed = mapa.lava_giant_data.lava_giant_max_speed
        self.lava_giant_suffocation_per_turn = mapa.lava_giant_data.lava_giant_suffocation_per_turn
        self.lava_giant_summoning_duration = mapa.lava_giant_data.lava_giant_summoning_duration
        self.portal_building_duration = mapa.portal_data.portal_building_duration
        self.portal_cost = mapa.portal_data.portal_cost
        self.portal_max_health = mapa.portal_data.portal_max_health
        self.portal_size = mapa.portal_data.portal_size

    def debug(self, obj):
        print "(%s) %s: %s" %(self.owner.id, self.turn, obj)

    def get_max_turn_time(self):
        return 0.1
    
    def get_all_buildings(self):
        owner_buildings = self.owner.get_all_buildings()
        enemy_buildings = self.enemy.get_all_buildings()
        return owner_buildings + enemy_buildings

    def get_all_castles(self):
        return [self.enemy.castle, self.owner.castle]

    def get_all_my_elves(self):
        return self.owner.all_elves

    def get_all_enemy_elves(self):
        return self.enemy.all_elves

    def get_all_elves(self):
        return self.get_all_enemy_elves() + self.get_all_my_elves()

    def get_all_living_elves(self):
        return self.get_my_living_elves() + self.get_enemy_living_elves()

    def get_all_players(self):
        return [self.owner, self.enemy]

    def get_all_portals(self):
        return self.enemy.portals + self.owner.portals

    def get_enemy(self):
        return self.enemy

    def get_enemy_castle(self):
        return self.enemy.castle

    def get_enemy_living_elves(self):
        self.enemy.update_living_elves()
        return self.enemy.living_elves

    def get_enemy_creatures(self):
        return self.enemy.creatures

    def get_enemy_ice_trolls(self):
        return self.enemy.ice_trolls

    def get_enemy_lava_giants(self):
        return self.enemy.lava_giants

    def get_enemy_portals(self):
        return self.enemy.portals

    def get_enemy_mana(self):
        return self.enemy.mana

    def get_myself(self):
        return self.owner

    def get_my_castle(self):
        return self.owner.castle

    def get_my_living_elves(self):
        self.owner.update_living_elves()
        return self.owner.living_elves

    def get_my_creatures(self):
        return self.owner.creatures

    def get_my_ice_trolls(self):
        return self.owner.ice_trolls

    def get_my_lava_giants(self):
        return self.owner.lava_giants

    def get_my_portals(self):
        return self.owner.portals

    def get_my_mana(self):
        return self.owner.mana

    def get_time_remaining(self):
        return 0.1

    def in_map(self, obj):
        if obj.location.row >= 0 and obj.location.row < self.rows and obj.location.col >= 0 and obj.location.col < self.cols:
            return True
        return False

    def decrease_mana(self, cost):
        self.owner.decrease_mana(cost)

    def update_mana_per_turn(self):
        self.owner.update_mana_per_turn()


    def can_build_portal_at(self, loc):
        if self.owner.mana < self.portal_cost:
            return False
        for b in self.get_all_buildings():
            if loc.distance(b.location) < self.portal_size + b.size:
                return False

        for e in self.get_all_elves():
            if e.is_building:
                e_size = self.portal_size if e.currently_building == "Portal" else 0
                if loc.distance(e.location) < self.portal_size + e_size:
                    return False
        return True

    def can_owner_summon_ice_troll(self):
        return self.owner.can_summon(self.ice_troll_cost)

    def can_owner_summon_lava_giant(self):
        return self.owner.can_summon(self.lava_giant_cost)

    def create_creature(self, creature_type, location, portal):
        self.last_uid = self.last_uid + 1
        if creature_type == "IceTroll":
            new_id = self.owner.last_ice_troll_id + 1
            ice = IceTroll(new_id, self.ice_troll_max_health, location, self.owner, self.last_uid,
                           self.ice_troll_attack_multiplier, self.ice_troll_attack_range, self.ice_troll_max_speed,
                           None, None, self.ice_troll_suffocation_per_turn)
            self.owner.add_ice_troll(ice)

        elif creature_type == "LavaGiant":
            new_id = self.owner.last_lava_giant_id + 1
            lava = LavaGiant(new_id, self.lava_giant_max_health, location, self.owner, self.last_uid,
                             self.lava_giant_attack_multiplier, self.lava_giant_attack_range, self.lava_giant_max_speed,
                             None, None, self.lava_giant_suffocation_per_turn)
            self.owner.add_lava_giant(lava)

    def create_building(self, building_type, location, owner):
        self.last_uid = self.last_uid + 1
        if building_type == "Portal":
            new_id = self.owner.last_portal_id + 1
            port = Portal(new_id, self.portal_max_health, location, self.owner, self.last_uid, self.portal_size, self.portal_building_duration)
            self.owner.add_portal(port)


if __name__ == '__main__':

    mapa = Map.Empty_Map()
    g = Game(mapa.get_player_0(), mapa.get_player_1(), mapa)

    print g.last_uid
