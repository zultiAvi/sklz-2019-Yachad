import BaseObject
import Map
import elf_kingdom

class Game(BaseObject):
    def __init__(self, owner, enemy, mapa):
        BaseObject.__init__(self, "Game")
        self.owner = owner
        self.enemy = enemy
        self.mapa = mapa

        self.turn = 0
        self.cols = mapa.size.cols
        self.rows = mapa.size.rows
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
        self.ice_troself.ll_attack_range = mapa.ice_troll_data.ice_troll_attack_range
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
        print obj

    def get_max_turn_time(self):
        return 0.1
    
    def get_all_buildings(self):
        owner_buildings = self.owner.get_all_buildings()
        enemy_buildings = self.enemy.get_all_buildings()
        return owner_buildings + enemy_buildings

    def get_all_castles(self):
        return [self.owner.castle, self.enemy.castle]

    def get_all_my_elves(self):
        return self.owner.all_elves

    def get_all_enemy_elves(self):
        return self.enemy.all_elves

    def get_all_elves(self):
        return self.get_all_my_elves() + self.get_all_enemy_elves()

    def get_all_living_elves(self):
        return self.get_my_living_elves() + self.get_enemy_living_elves()

    def get_all_players(self):
        return [self.owner, self.enemy]

    def get_all_portals(self):
        return self.owner.portals + self.enemy.portals

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
        if obj.location.rows >= 0 and obj.location.rows < self.rows and obj.location.cols >= 0 and obj.location.cols < self.cols:
            return True
        return False

    def can_build_portal_at(self, loc):
        if self.owner.mana < self.portal_cost:
            return False
        for b in self.get_all_buildings():
            if loc.distance(b.location) < self.portal_size + b.size:
                return False
        return True


    def build_portal(self, object):
        pass

    def set_attack(self, object, target):
        pass

    def move_to(self, object, loc):
        pass

    def can_summon_ice_troll(self):
        return False

    def can_summon_lava_giant(self):
        return False

    def summon_ice_troll(self):
        pass

    def summon_lava_giant(self):
        pass

