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

    # print_data(game, -1)
    print_data(game, 32)
    handle_elves(game)
    handle_portals(game)


def handle_elves(game):
    """
    Gives orders to my elves.

    :param game: the current game state.
    :type game: Game
    """
    # Get enemy castle.
    enemy_castle = game.get_enemy_castle()  # type: Castle
    # Go over all the living elves.
    for elf in game.get_my_living_elves():
        # Try to attack enemy castle, if not move to it.
        if elf.in_attack_range(enemy_castle):
            # Attack!
            elf.attack(enemy_castle)
            # Print a message.
            game.debug( "elf %s attacks %s" %(elf, enemy_castle))

        else:
            # Move to enemy castle!
            elf.move_to(enemy_castle)
            # Print a message.
            game.debug("elf %s moves to %s" %(elf, enemy_castle))


def handle_portals(game):
    """
    Gives orders to my portals.

    :param game: the current game state.
    :type game: Game
    """
    # Go over all of my portals.
    for portal in game.get_my_portals():
        # If the portal can summon a lava giant, do that.
        if game.turn < 40:
            if portal.can_summon_lava_giant():
                # Summon the lava giant.
                portal.summon_lava_giant()
                # Print a message.
                game.debug("portal %s summons a lava giant" %(portal))
        else:
            if portal.can_summon_ice_troll():
                # Summon the lava giant.
                portal.summon_ice_troll()
                # Print a message.
                game.debug("portal %s summons an ice troll" %(portal))


