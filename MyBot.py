"""
This is an example for a bot.
"""
from elf_kingdom import *

class my_bot_0:
    def __init__ (self):
        self.game = None

    def __call__(self, game):
        self.game = game
        self.do_turn()

    def do_turn(self):
        """
        Makes the bot run a single turn.

        :param game: the current game state.
        :type game: Game
        """

        self.handle_elves()
        # self.handle_portals()


    def handle_elves(self):
        """
        Gives orders to my elves.

        :param game: the current game state.
        :type game: Game
        """
        # Get enemy castle.
        enemy_castle = self.game.get_enemy_castle()  # type: Castle
        # Go over all the living elves.
        for elf in self.game.get_my_living_elves():
            # Try to attack enemy castle, if not move to it.
            if elf.in_attack_range(enemy_castle):
                # Attack!
                elf.attack(enemy_castle)
                # Print a message.
                self.game.debug( "elf %s attacks %s" %(elf, enemy_castle))

            else:
                # Move to enemy castle!
                elf.move_to(enemy_castle)
                # Print a message.
                self.game.debug("elf %s moves to %s" %(elf, enemy_castle))


    def handle_portals(self):
        """
        Gives orders to my portals.

        :param game: the current game state.
        :type game: Game
        """
        # Go over all of my portals.
        for portal in self.game.get_my_portals():
            # If the portal can summon a lava giant, do that.
            if portal.can_summon_lava_giant():
                # Summon the lava giant.
                portal.summon_lava_giant()
                # Print a message.
                self.game.debug("portal %s summons a lava giant" %(portal))

"""
This is an example for a bot.
"""

class my_bot_1:
    def __init__ (self):
        self.game = None

    def __call__(self, game):
        self.game = game
        self.do_turn()

    def do_turn(self):
        """
        Makes the bot run a single turn.

        :param game: the current game state.
        :type game: Game
        """

        self.handle_elves()
        # Give orders to my portals.
        self.handle_portals()


    def handle_elves(self):
        """
        Gives orders to my elves.

        :param game: the current game state.
        :type game: Game
        """
        # Get enemy castle.
        enemy_castle = self.game.get_enemy_castle()  # type: Castle
        # Go over all the living elves.
        for elf in self.game.get_my_living_elves():
            # Try to attack enemy castle, if not move to it.
            if elf.in_attack_range(enemy_castle):
                # Attack!
                elf.attack(enemy_castle)
                # Print a message.
                self.game.debug("elf %s attacks %s" %(elf, enemy_castle))

            else:
                # Move to enemy castle!
                elf.move_to(enemy_castle)
                # Print a message.
                self.game.debug("elf %s moves to %s" %(elf, enemy_castle))


    def handle_portals(self):
        """
        Gives orders to my portals.

        :param game: the current game state.
        :type game: Game
        """
        # Go over all of my portals.
        for portal in self.game.get_my_portals():
            # If the portal can summon a lava giant, do that.
            if portal.can_summon_lava_giant():
                # Summon the lava giant.
                portal.summon_lava_giant()
                # Print a message.
                self.game.debug("portal %s summons a lava giant" %(portal))


do_turn_0 = my_bot_0()
do_turn_1 = my_bot_1()
do_turn = my_bot_0()
