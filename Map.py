from Location import Location
from Castle import Castle
from Portal import Portal
from Elf import Elf
from Player import Player

map_size = Location(0,0)

class Map:
    def __init__(self, size=Location(3801,6401), max_turns=750, score_player_0 = 0, score_player_1 = 0, default_mana_per_turn=10, init_mana_player0 = 20, init_mana_player1 = 20,
                 castle_data = Castle_data(), elf_data = Elf_data(), portal_data = Portal_data(), ice_troll_data = Ice_Troll_data(), lava_giant_data = Lava_Giant_data(),
                 player_0_castle = None, player_1_castle = None, player_0_elves = None, player_1_elves = None,
                 player_0_portals = None, player_1_portals = None,player_0_ice_trolls = None, player_1_ice_trolls = None,
                 player_0_lava_giants = None, player_1_lava_giants = None):

        global map_size
        map_size = size
        self.max_turns = max_turns
        self.score_player_0 = score_player_0
        self.score_player_1 = score_player_1
        self.default_mana_per_turn = default_mana_per_turn
        self.init_mana_player0 = init_mana_player0
        self.init_mana_player1 = init_mana_player1

        self.castle_data = castle_data
        self.elf_data = elf_data
        self.portal_data = portal_data
        self.ice_troll_data = ice_troll_data
        self.lava_giant_data = lava_giant_data

        self.player_0_castle = player_0_castle # castle object
        self.player_1_castle = player_1_castle

        self.player_0_elves = player_0_elves #list of elves objects
        self.player_1_elves = player_1_elves
        self.player_0_portals = player_0_portals
        self.player_1_portals = player_1_portals
        self.player_0_ice_trolls = player_0_ice_trolls
        self.player_1_ice_trolls = player_1_ice_trolls
        self.player_0_lava_giants = player_0_lava_giants
        self.player_1_lava_giants = player_1_lava_giants

        self.player_0 = Player(0, self.player_0_elves, init_mana_player0, default_mana_per_turn, score_player_0,
                               self.player_0_portals, self.player_0_castle, self.player_0_ice_trolls, self.player_0_lava_giants)
        self.player_1 = Player(1, self.player_1_elves, init_mana_player1, default_mana_per_turn, score_player_1,
                               self.player_1_portals, self.player_1_castle, self.player_1_ice_trolls, self.player_1_lava_giants)

    def save_map(self):
        pass

    def read_map(self):
        pass

    def get_player_0(self):
        return self.player_0


    def get_player_1(self):
        return self.player_1


class Castle_data:
    def __init__(self, castle_max_health = 150, castle_size = 500):
        self.castle_max_health = castle_max_health
        self.castle_size = castle_size

class Elf_data:
    def __init__(self, elf_attack_multiplier = 1, elf_attack_range = 300, elf_max_health = 12, elf_spawn_turns = 40):
        self.elf_attack_multiplier = elf_attack_multiplier
        self.elf_attack_range = elf_attack_range
        self.elf_max_health = elf_max_health
        self.elf_spawn_turns = elf_spawn_turns

class Portal_data:
    def __init__(self, portal_building_duration = 4, portal_cost = 60, portal_max_health = 8, portal_size = 300):
        self.portal_building_duration = portal_building_duration
        self.portal_cost = portal_cost
        self.portal_max_health = portal_max_health
        self.portal_size = portal_size

class Ice_Troll_data:
    def __init__(self, ice_troll_attack_multiplier = 1, ice_troll_attack_range = 300, ice_troll_cost = 50, ice_troll_max_health = 25, ice_troll_max_speed = 100, ice_troll_suffocation_per_turn = 1, ice_troll_summoning_duration = 3):
        self.ice_troll_attack_multiplier = ice_troll_attack_multiplier
        self.ice_troself.ll_attack_range = ice_troll_attack_range
        self.ice_troll_cost = ice_troll_cost
        self.ice_troll_max_health = ice_troll_max_health
        self.ice_troll_max_speed = ice_troll_max_speed
        self.ice_troll_suffocation_per_turn = ice_troll_suffocation_per_turn
        self.ice_troll_summoning_duration = ice_troll_summoning_duration

class Lava_Giant_data:
    def __init__(self, lava_giant_attack_multiplier = 1, lava_giant_attack_range = 300, lava_giant_cost = 40, lava_giant_max_health = 25, lava_giant_max_speed = 200, lava_giant_suffocation_per_turn = 1, lava_giant_summoning_duration = 3):
        self.lava_giant_attack_multiplier = lava_giant_attack_multiplier
        self.lava_giant_attack_range = lava_giant_attack_range
        self.lava_giant_cost = lava_giant_cost
        self.lava_giant_max_health = lava_giant_max_health
        self.lava_giant_max_speed = lava_giant_max_speed
        self.lava_giant_suffocation_per_turn = lava_giant_suffocation_per_turn
        self.lava_giant_summoning_duration = lava_giant_summoning_duration


class Default_Map(Map):
    def __init__(self):
        # Player (game, id, elves, mana, mana_per_turn, score, portals, castle, ice_trolls=None, lava_giants=None):
        player_0 = Player(0, None, 20, 10, 0, None, None, None, None)
        player_1 = Player(1, None, 20, 10, 0, None, None, None, None)

        # Castle ( game, id, health, loc, owner, unique_id, size)
        player_0_castle = Castle(0, 150, Location(3100, 700), player_0, 1000, 500)
        player_1_castle = Castle(0, 150, Location(700, 5800), player_1, 1001, 500)

        # Elf(game, id, init_health, initial_loc, owner, unique_id, attack_multiplier, attack_range, max_speed, turns_to_revive)
        player_0_elves = [Elf(0, 12, Location(3100, 1200), player_0, 1004, 1, 300, 100, 0),
                          Elf(1, 12, Location(2600,  700), player_0, 1005, 1, 300, 100, 0)]
        player_1_elves = [Elf(0, 12, Location( 700, 5300), player_1, 1006, 1, 300, 100, 0),
                          Elf(1, 12, Location(1200, 5800), player_1, 1007, 1, 300, 100, 0)]
        # Portal ( game, id, health, loc, owner, unique_id, size, turns_to_summon)
        player_0_portals = [Portal(0, 8, Location(1900, 1000), player_0, 1002, 300, 2)]
        player_1_portals = [Portal(0, 8, Location(1900, 5500), player_1, 1003, 300, 2)]

        player_0.update_all_elves(player_0_elves)
        player_0.castle = player_0_castle
        player_0.portals = player_0_portals
        player_1.update_all_elves(player_1_elves)
        player_1.castle = player_1_castle
        player_1.portals = player_1_portals


        Map.__init__(self, size=Location(3801, 6401), max_turns=750, score_player_0 = 0, score_player_1 = 0, default_mana_per_turn=10, init_mana_player0 = 20, init_mana_player1 = 20,
            castle_data=Castle_data(), elf_data=Elf_data(), portal_data=Portal_data(),
            ice_troll_data=Ice_Troll_data(), lava_giant_data=Lava_Giant_data(),
            player_0_castle=player_0_castle, player_1_castle=player_1_castle, player_0_elves=player_0_elves, player_1_elves=player_1_elves,
            player_0_portals=player_0_portals, player_1_portals=player_1_portals, player_0_ice_trolls=None, player_1_ice_trolls=None,
            player_0_lava_giants=None, player_1_lava_giants=None)
