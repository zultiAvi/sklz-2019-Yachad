"""
This is an example for a bot.
"""
from elf_kingdom import *
from PrintData import print_data

def do_turn(game):
    """
    Makes the bot run a single turn.

    :param game: the current game state.
    :type game: Game
    """

    # loc1 = Location(1804, 1388)
    # loc2 = Location(700, 5800)
    # speed = 200
    # next_loc = loc1.towards(loc2, speed)
    # print next_loc
    #
    # loc1 = Location(0, 0)
    # for i in range(20):
    #     loc2 = Location(100, i)
    #     d = loc1.distance(loc2)
    #     print i, d

    temp_mana = game.get_my_mana()
    # print_data(game, -1)
    # print_data(game, 32)
    temp_mana = handle_elves(game, temp_mana)
    temp_mana = handle_portals(game, temp_mana)


def handle_elves(game, temp_mana):
    """
    Gives orders to my elves.

    :param game: the current game state.
    :type game: Game
    """
    # Get enemy castle.
    enemy_castle = game.get_enemy_castle()  # type: Castle
    enemy_portals = game.get_enemy_portals()
    enemy_elves = game.get_enemy_living_elves()

    # Go over all the living elves.
    for elf in game.get_my_living_elves():
        # Try to attack enemy castle, if not move to it.
        if game.turn < 30 and temp_mana >= game.portal_cost and elf.can_build_portal():
            elf.build_portal()
            temp_mana -= game.portal_cost
            game.debug( "elf %s is building a portal" %elf)
            continue

        # if len(enemy_portals) > 0:
        #     attack_or_move(game, elf, enemy_portals[0])
        #     continue

        if len(enemy_elves) > 0:
            attack_or_move(game, elf, enemy_elves[0])
            continue

        attack_or_move(game, elf, enemy_castle)

    return temp_mana


def attack_or_move(game, elf, target):
    if elf.in_attack_range(target):
        # Attack!
        elf.attack(target)
        # Print a message.
        game.debug("elf %s attacks %s" % (elf, target))
    else:
        # Move to enemy castle!
        elf.move_to(target)
        # Print a message.
        game.debug("elf %s moves to %s" % (elf, target))


def handle_portals(game, temp_mana):
    """
    Gives orders to my portals.

    :param game: the current game state.
    :type game: Game
    """
    # Go over all of my portals.
    if game.turn < 20:
        return

    for portal in game.get_my_portals():
        # If the portal can summon a lava giant, do that.
        if (game.turn % 100) < 50:
            if temp_mana >= game.lava_giant_cost and portal.can_summon_lava_giant():
                # Summon the lava giant.
                portal.summon_lava_giant()
                temp_mana -= game.lava_giant_cost

                # Print a message.
                game.debug("portal %s summons a lava giant" %(portal))
        else:
            if temp_mana >= game.ice_troll_cost and portal.can_summon_ice_troll():
                # Summon the lava giant.
                portal.summon_ice_troll()
                temp_mana -= game.ice_troll_cost
                # Print a message.
                game.debug("portal %s summons an ice troll" %(portal))

    return temp_mana
