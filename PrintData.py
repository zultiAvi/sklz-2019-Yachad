def print_data(game, turn):
    if game.turn == turn or turn < 0:
        text = data_to_text(game)
        for t in text:
            print t

def data_to_text(game):
    text = []
    text += game_constants_to_text(game)
    text += players_to_text(game)
    return text

def game_constants_to_text(game):
    text = ["Game"]
    text.append("game.turn = %s" % game.turn)
    text.append("game.cols = %s" % game.cols)
    text.append("game.rows = %s" % game.rows)
    text.append("game.max_points = %s" % game.max_points)
    text.append("game.max_turns = %s" % game.max_turns)
    text.append("game.castle_max_health = %s" % game.castle_max_health)
    text.append("game.castle_size = %s" % game.castle_size)
    text.append("game.default_mana_per_turn = %s" % game.default_mana_per_turn)
    text.append("game.elf_attack_multiplier = %s" % game.elf_attack_multiplier)
    text.append("game.elf_attack_range = %s" % game.elf_attack_range)
    text.append("game.elf_max_health = %s" % game.elf_max_health)
    text.append("game.elf_spawn_turns = %s" % game.elf_spawn_turns)
    text.append("game.ice_troll_attack_multiplier = %s" % game.ice_troll_attack_multiplier)
    text.append("game.ice_troll_attack_range = %s" % game.ice_troll_attack_range)
    text.append("game.ice_troll_cost = %s" % game.ice_troll_cost)
    text.append("game.ice_troll_max_health = %s" % game.ice_troll_max_health)
    text.append("game.ice_troll_max_speed = %s" % game.ice_troll_max_speed)
    text.append("game.ice_troll_suffocation_per_turn = %s" % game.ice_troll_suffocation_per_turn)
    text.append("game.ice_troll_summoning_duration = %s" % game.ice_troll_summoning_duration)
    text.append("game.lava_giant_attack_multiplier = %s" % game.lava_giant_attack_multiplier)
    text.append("game.lava_giant_attack_range = %s" % game.lava_giant_attack_range)
    text.append("game.lava_giant_cost = %s" % game.lava_giant_cost)
    text.append("game.lava_giant_max_health = %s" % game.lava_giant_max_health)
    text.append("game.lava_giant_max_speed = %s" % game.lava_giant_max_speed)
    text.append("game.lava_giant_suffocation_per_turn = %s" % game.lava_giant_suffocation_per_turn)
    text.append("game.lava_giant_summoning_duration = %s" % game.lava_giant_summoning_duration)
    text.append("game.portal_building_duration = %s" % game.portal_building_duration)
    text.append("game.portal_cost = %s" % game.portal_cost)
    text.append("game.portal_max_health = %s" % game.portal_max_health)
    text.append("game.portal_size = %s" % game.portal_size)
    return text

def players_to_text(game):
    p = game.get_myself()
    text = ["Player"]
    text.append("player.id = %s" % p.id)
    text.append("player.mana = %s" % p.mana)
    text.append("player.mana_per_turn = %s" % p.mana_per_turn)
    text.append("player.score = %s" % p.score)
    e = game.get_enemy()
    text.append("Player")
    text.append("player.id = %s" % e.id)
    text.append("player.mana = %s" % e.mana)
    text.append("player.mana_per_turn = %s" % e.mana_per_turn)
    text.append("player.score = %s" % e.score)

    text += all_elves_to_text(game.get_all_elves())
    text += all_creatures_to_text(game.get_my_creatures())
    text += all_creatures_to_text(game.get_enemy_creatures())
    text += castle_to_text(game.get_all_castles())
    text += all_portals_to_text(game.get_my_portals(), game.get_enemy_portals())

    return text

def all_elves_to_text(all_elves):
    text = []
    for e in all_elves:
        text.append("Elf")
        text.append("Elf.id = %s" % e.id)
        text.append("Elf.current_health = %s" % e.current_health)
        text.append("Elf.location = %s" % e.location)
        text.append("Elf.initial_location = %s" % e.initial_location)
        text.append("Elf.owner = %s" % e.owner.id)
        text.append("Elf.attack_multiplier = %s" % e.attack_multiplier)
        text.append("Elf.attack_range = %s" % e.attack_range)
        text.append("Elf.max_speed = %s" % e.max_speed)
        text.append("Elf.turns_to_revive = %s" % e.turns_to_revive)
        text.append("Elf.currently_building = %s" % e.currently_building)
        text.append("Elf.is_building = %s" % e.is_building)
        text.append("Elf.spawn_turns = %s" % e.spawn_turns)

    return text

def all_creatures_to_text(all_creatures):
    text = []
    for c in all_creatures:
        text.append("Creature")
        text.append("Creature.type = %s" % c.type)
        text.append("Creature.id = %s" % c.id)
        text.append("Creature.current_health = %s" % c.current_health)
        text.append("Creature.location = %s" % c.location)
        text.append("Creature.initial_location = %s" % c.initial_location)
        text.append("Creature.owner = %s" % c.owner.id)
        text.append("Creature.attack_multiplier = %s" % c.attack_multiplier)
        text.append("Creature.attack_range = %s" % c.attack_range)
        text.append("Creature.max_speed = %s" % c.max_speed)
        text.append("Creature.summoner = %s" % c.summoner)
        text.append("Creature.summoning_duration = %s" % c.summoning_duration)
        text.append("Creature.suffocation_per_turn = %s" % c.suffocation_per_turn)
    return text

def castle_to_text(all_castls):
    text = []
    for c in all_castls:
        text.append("Castle")
        text.append("Castle.type = %s" % c.type)
        text.append("Castle.id = %s" % c.id)
        text.append("Castle.current_health = %s" % c.current_health)
        text.append("Castle.location = %s" % c.location)
        text.append("Castle.initial_location = %s" % c.initial_location)
        text.append("Castle.owner = %s" % c.owner.id)
        text.append("Castle.size = %s" % c.size)
        
    return text

def all_portals_to_text(my_portals, enemy_portals):
    text = []
    all_portals = my_portals + enemy_portals
    for p in all_portals:
        text.append("Portal")
        text.append("Portal.type = %s" % p.type)
        text.append("Portal.id = %s" % p.id)
        text.append("Portal.current_health = %s" % p.current_health)
        text.append("Portal.location = %s" % p.location)
        text.append("Portal.initial_location = %s" % p.initial_location)
        text.append("Portal.owner = %s" % p.owner.id)
        text.append("Portal.size = %s" % p.size)
        text.append("Portal.currently_summoning = %s" % p.currently_summoning)
        text.append("Portal.is_summoning = %s" % p.is_summoning)
        text.append("Portal.turns_to_summon = %s" % p.turns_to_summon)

    return text
