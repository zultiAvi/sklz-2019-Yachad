import os
import json

from Location import Location
from Castle import Castle
from Player import Player
from Portal import Portal
from Elf import Elf
from LavaGiant import LavaGiant
from IceTroll import IceTroll
map_size = Location(0,0)

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
        self.ice_troll_attack_range = ice_troll_attack_range
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


class Map:

    def __init__(self, size=Location(3801,6401), turn=0, max_turns=750, score_player_0 = 0, score_player_1 = 0, default_mana_per_turn=10, init_mana_player0 = 20, init_mana_player1 = 20,
                 castle_data = Castle_data(), elf_data = Elf_data(), portal_data = Portal_data(), ice_troll_data = Ice_Troll_data(), lava_giant_data = Lava_Giant_data(),
                 player_0_castle = None, player_1_castle = None, player_0_elves = None, player_1_elves = None,
                 player_0_portals = None, player_1_portals = None,player_0_ice_trolls = None, player_1_ice_trolls = None,
                 player_0_lava_giants = None, player_1_lava_giants = None, file_name = None):

        if file_name is not None:
            self.read_game_from_file(file_name)
        else:
            global map_size
            map_size = size
            self.map_size = size

            self.turn = turn
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

    def get_player_0(self):
        return self.player_0

    def get_player_1(self):
        return self.player_1

    def get_next_index(self, index, text):
        index += 1
        while index < len(text):
            w = text[index][:-1].split(" = ")
            if len(w) == 1:
                return index
            index += 1
        return index

    def get_location(self, text):
        loc = text.replace("(","").replace(")","").split(",")
        return Location(int(loc[0]), int(loc[1]))

    def read_game_from_file(self, fn):
        with open(fn, "r") as f:
            text = f.readlines()

        index = 0
        while index < len(text):
            w = text[index][:-1].split(" = ")
            if len(w) == 1:
                next_index = self.get_next_index(index, text)
                text_to_parse = text[index + 1:next_index]
                if w[0] == "Game":
                    self.create_game(text_to_parse)
                if w[0] == "Player":
                    self.create_player(text_to_parse)
                if w[0] == "Elf":
                    self.create_elf(text_to_parse, index)
                if w[0] == "Creature":
                    self.create_creature(text_to_parse, index)
                if w[0] == "Castle":
                    self.create_castle(text_to_parse, index)
                if w[0] == "Portal":
                    self.create_portal(text_to_parse, index)

                index = next_index

            elif len(w) == 2:
                print "Unknown Field: '%s'. Data: '%s' !!!!!" % (w[0], w[1])
                break

        self.turn -= 1
        self.player_0.decrease_mana(self.player_0.mana_per_turn)
        self.player_1.decrease_mana(self.player_1.mana_per_turn)


    def create_game(self, text):
        cols = 0
        self.castle_data = Castle_data()
        self.elf_data = Elf_data()
        self.portal_data = Portal_data()
        self.ice_troll_data = Ice_Troll_data()
        self.lava_giant_data = Lava_Giant_data()

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "game.turn":
                self.turn = int(w[1])
            elif w[0] == "game.cols":
                cols = int(w[1])
            elif w[0] == "game.rows":
                rows = int(w[1])
                loc = Location(rows, cols)
                global map_size
                map_size = loc
                self.map_size = map_size
            elif w[0] == "game.max_points":
                self.castle_data.castle_max_health = int(w[1])
            elif w[0] == "game.max_turns":
                self.max_turns = int(w[1])
            elif w[0] == "game.default_mana_per_turn":
                self.default_mana_per_turn = int(w[1])
            elif w[0] == "game.castle_max_health":
                self.castle_data.castle_max_health = int(w[1])
            elif w[0] == "game.castle_size":
                self.castle_data.castle_size = int(w[1])
            elif w[0] == "game.elf_attack_multiplier":
                self.elf_data.elf_attack_multiplier = int(w[1])
            elif w[0] == "game.elf_attack_range":
                self.elf_data.elf_attack_range = int(w[1])
            elif w[0] == "game.elf_max_health":
                self.elf_data.elf_max_health = int(w[1])
            elif w[0] == "game.elf_spawn_turns":
                self.elf_data.elf_spawn_turns = int(w[1])
            elif w[0] == "game.ice_troll_attack_multiplier":
                self.ice_troll_data.ice_troll_attack_multiplier = int(w[1])
            elif w[0] == "game.ice_troll_attack_range":
                self.ice_troll_data.ice_troll_attack_range = int(w[1])
            elif w[0] == "game.ice_troll_cost":
                self.ice_troll_data.ice_troll_cost = int(w[1])
            elif w[0] == "game.ice_troll_max_health":
                self.ice_troll_data.ice_troll_max_health = int(w[1])
            elif w[0] == "game.ice_troll_max_speed":
                self.ice_troll_data.ice_troll_max_speed = int(w[1])
            elif w[0] == "game.ice_troll_suffocation_per_turn":
                self.ice_troll_data.ice_troll_suffocation_per_turn = int(w[1])
            elif w[0] == "game.ice_troll_summoning_duration":
                self.ice_troll_data.ice_troll_summoning_duration = int(w[1])
            elif w[0] == "game.lava_giant_attack_multiplier":
                self.lava_giant_data.lava_giant_attack_multiplier = int(w[1])
            elif w[0] == "game.lava_giant_attack_range":
                self.lava_giant_data.lava_giant_attack_range = int(w[1])
            elif w[0] == "game.lava_giant_cost":
                self.lava_giant_data.lava_giant_cost = int(w[1])
            elif w[0] == "game.lava_giant_max_health":
                self.lava_giant_data.lava_giant_max_health = int(w[1])
            elif w[0] == "game.lava_giant_max_speed":
                self.lava_giant_data.lava_giant_max_speed = int(w[1])
            elif w[0] == "game.lava_giant_suffocation_per_turn":
                self.lava_giant_data.lava_giant_suffocation_per_turn = int(w[1])
            elif w[0] == "game.lava_giant_attack_multiplier":
                self.lava_giant_data.lava_giant_attack_multiplier = int(w[1])
            elif w[0] == "game.portal_building_duration":
                self.portal_data.portal_building_duration = int(w[1])
            elif w[0] == "game.portal_cost":
                self.portal_data.portal_cost = int(w[1])
            elif w[0] == "game.portal_max_health":
                self.portal_data.portal_max_health = int(w[1])
            elif w[0] == "game.portal_size":
                self.portal_data.portal_size = int(w[1])

    def create_player(self, text):
        player = Player(0, None, 20, 10, 0, None, None, None, None)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "player.id":
                player.id = int(w[1])
            elif w[0] == "player.mana":
                player.mana = int(w[1])
            elif w[0] == "player.mana_per_turn":
                player.mana_per_turn = int(w[1])
            elif w[0] == "player.score":
                player.score = int(w[1])

        if player.id == 0:
            self.player_0 = player
        if player.id == 1:
            self.player_1 = player

    def create_elf(self, text, index):
        elf = Elf(0, 0, 0, 0, index, 0, 0, 0,0)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "Elf.id":
                elf.id = int(w[1])
            elif w[0] == "Elf.current_health":
                elf.current_health = int(w[1])
            elif w[0] == "Elf.location":
                elf.location = self.get_location(w[1])
            elif w[0] == "Elf.initial_location":
                elf.initial_location = self.get_location(w[1])
            elif w[0] == "Elf.owner":
                elf.owner  = self.player_0 if int(w[1]) == 0 else self.player_1
            elif w[0] == "Elf.attack_multiplier":
                elf.attack_multiplier = int(w[1])
            elif w[0] == "Elf.attack_range":
                elf.attack_range = int(w[1])
            elif w[0] == "Elf.max_speed":
                elf.max_speed = int(w[1])
            elif w[0] == "Elf.turns_to_revive":
                elf.turns_to_revive = int(w[1])

        elf.owner.add_elf(elf)

    def create_creature(self, text, index):
        l = text[0]
        w = l[:-1].split(" = ")
        if len(w) == 1:
            return
        if w[0] == "Portal.type":
            if w[1] == "LavaGiant":
                self.create_lava_giant(text[1:], index)
        if w[1] == "IceTroll":
            self.create_ice_troll(text[1:], index)

    def create_lava_giant(self, text, index):
        lava_giant = LavaGiant(0, 0, 0, 0, index, 0, 0, 0, None, 0, 0)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "Creature.id":
                lava_giant.id = int(w[1])
            elif w[0] == "Creature.current_health":
                lava_giant.current_health = int(w[1])
            elif w[0] == "Creature.location":
                lava_giant.location = self.get_location(w[1])
            elif w[0] == "Creature.initial_location":
                lava_giant.initial_location = self.get_location(w[1])
            elif w[0] == "Creature.owner":
                lava_giant.owner  = self.player_0 if int(w[1]) == 0 else self.player_1
            elif w[0] == "Creature.attack_multiplier":
                lava_giant.attack_multiplier = int(w[1])
            elif w[0] == "Creature.attack_range":
                lava_giant.attack_range = int(w[1])
            elif w[0] == "Creature.max_speed":
                lava_giant.max_speed = int(w[1])
            elif w[0] == "Creature.summoner":
                lava_giant.summoner = None if w[1] == "None" else w[1]
            elif w[0] == "Creature.summoning_duration":
                lava_giant.summoning_duration = None if w[1] == "None" else int(w[1])
            elif w[0] == "Creature.suffocation_per_turn":
                lava_giant.suffocation_per_turn = int(w[1])

        lava_giant.owner.add_lava_giant(lava_giant)

    def create_ice_troll(self, text, index):
        ice_troll = IceTroll(0, 0, 0, 0, index, 0, 0, 0, None, 0, 0)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "Creature.id":
                ice_troll.id = int(w[1])
            elif w[0] == "Creature.current_health":
                ice_troll.current_health = int(w[1])
            elif w[0] == "Creature.location":
                ice_troll.location = self.get_location(w[1])
            elif w[0] == "Creature.initial_location":
                ice_troll.initial_location = self.get_location(w[1])
            elif w[0] == "Creature.owner":
                ice_troll.owner  = self.player_0 if int(w[1]) == 0 else self.player_1
            elif w[0] == "Creature.attack_multiplier":
                ice_troll.attack_multiplier = int(w[1])
            elif w[0] == "Creature.attack_range":
                ice_troll.attack_range = int(w[1])
            elif w[0] == "Creature.max_speed":
                ice_troll.max_speed = int(w[1])
            elif w[0] == "Creature.summoner":
                ice_troll.summoner = None if w[1] == "None" else w[1]
            elif w[0] == "Creature.summoning_duration":
                ice_troll.summoning_duration = None if w[1] == "None" else int(w[1])
            elif w[0] == "Creature.suffocation_per_turn":
                ice_troll.suffocation_per_turn = int(w[1])

        ice_troll.owner.add_ice_troll(ice_troll)

    def create_castle(self, text, index):
        castle = Castle(0, 0, 0, 0, index, 0)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "Castle.type":
                if w[1] != "Castle":
                    return
            if w[0] == "Castle.id":
                castle.id = int(w[1])
            elif w[0] == "Castle.current_health":
                castle.current_health = int(w[1])
            elif w[0] == "Castle.location":
                castle.location = self.get_location(w[1])
            elif w[0] == "Castle.initial_location":
                castle.initial_location = self.get_location(w[1])
            elif w[0] == "Castle.owner":
                castle.owner  = self.player_0 if int(w[1]) == 0 else self.player_1
            elif w[0] == "Castle.size":
                castle.size = int(w[1])

        castle.owner.add_castle(castle)

    def create_portal(self, text, index):
        portal = Portal(0, 0, 0, 0, index, 0, self.portal_data.portal_building_duration)

        for l in text:
            w = l[:-1].split(" = ")
            if len(w) == 1:
                break
            if w[0] == "Portal.type":
                if w[1] != "Portal":
                    return
            if w[0] == "Portal.id":
                portal.id = int(w[1])
            elif w[0] == "Portal.current_health":
                portal.current_health = int(w[1])
            elif w[0] == "Portal.location":
                portal.location = self.get_location(w[1])
            elif w[0] == "Portal.initial_location":
                portal.initial_location = self.get_location(w[1])
            elif w[0] == "Portal.owner":
                portal.owner  = self.player_0 if int(w[1]) == 0 else self.player_1
            elif w[0] == "Portal.size":
                portal.size = int(w[1])
            elif w[0] == "Portal.in_summoning":
                portal.in_summoning = w[1]
            elif w[0] == "Portal.is_summoning":
                portal.is_summoning = True if w[1] == "True" else False
            elif w[0] == "Portal.turns_to_summon":
                portal.turns_to_summon = int(w[1])

        portal.owner.add_portal(portal)


class Empty_Map(Map):
    def __init__(self):
        # Player (game, id, elves, mana, mana_per_turn, score, portals, castle, ice_trolls=None, lava_giants=None):
        player_0 = Player(0, None, 20, 10, 0, None, None, None, None)
        player_1 = Player(1, None, 20, 10, 0, None, None, None, None)

        # Castle ( game, id, health, loc, owner, unique_id, size)
        player_0_castle = Castle(0, 150, Location(3100, 700), player_0, 1000, 500)
        player_1_castle = Castle(0, 150, Location(700, 5800), player_1, 1001, 500)

        # Elf(game, id, init_health, initial_loc, owner, unique_id, attack_multiplier, attack_range, max_speed, turns_to_revive)
        player_0_elves = []
        player_1_elves = []
        # Portal ( game, id, health, loc, owner, unique_id, size, turns_to_summon)
        player_0_portals = []
        player_1_portals = []

        player_0.update_all_elves(player_0_elves)
        player_0.castle = player_0_castle
        player_0.portals = player_0_portals
        player_1.update_all_elves(player_1_elves)
        player_1.castle = player_1_castle
        player_1.portals = player_1_portals


        Map.__init__(self, size=Location(0, 0), max_turns=0, score_player_0 = 0, score_player_1 = 0, default_mana_per_turn=10, init_mana_player0 = 20, init_mana_player1 = 20,
            castle_data=Castle_data(), elf_data=Elf_data(), portal_data=Portal_data(),
            ice_troll_data=Ice_Troll_data(), lava_giant_data=Lava_Giant_data(),
            player_0_castle=player_0_castle, player_1_castle=player_1_castle, player_0_elves=player_0_elves, player_1_elves=player_1_elves,
            player_0_portals=player_0_portals, player_1_portals=player_1_portals, player_0_ice_trolls=None, player_1_ice_trolls=None,
            player_0_lava_giants=None, player_1_lava_giants=None)


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
