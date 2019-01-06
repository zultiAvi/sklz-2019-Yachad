from GameObject import GameObject
from BaseObject import get_game
# from Game import Game

class Elf (GameObject):
    def __init__(self, id, init_health, initial_loc, owner, unique_id, attack_multiplier, attack_range, max_speed, turns_to_revive):
        GameObject.__init__(self, id, init_health, initial_loc, owner, unique_id)
        self.type = "Elf"

        self.attack_multiplier = attack_multiplier
        self.attack_range = attack_range
        self.currently_building = None
        self.is_building = False
        self.max_speed = max_speed
        self.spawn_turns = turns_to_revive
        self.turns_to_revive = 0

        self._need_mana = 0
        self._action = ""
        self._attack_object = None
        self._next_location = None
        self._turns_to_build = 0

    def __str__(self):
        return "{Elf: %s, %s, %s}" % (self.id, self.current_health, self.location)

    def can_build_portal(self):
        game = get_game(self.owner)
        return game.can_build_portal_at(self.location)

    def in_attack_range(self, object):
        try:
            d = object.size
        except AttributeError:
            d = 0

        return self.location.in_range(object.location, self.attack_range + d)

    def attack(self, target):
        if not self.is_alive():
            return
        if self.is_building:
            return
        if self._action != "":
            self._action = "multiple"
            self._need_mana = 0
            return
        self._action = "attack"
        self._attack_object = target

    def build_portal(self):
        if not self.is_alive():
            return
        if self.is_building:
            return
        if self._action != "":
            self._action = "multiple"
            self._need_mana = 0
            return
        self._action = "build portal"

    def move_to(self, object):
        if not self.is_alive():
            return
        if self.is_building:
            return
        if self._action != "":
            self._action = "multiple"
            self._need_mana = 0
            return
        game = get_game(self.owner)
        if not game.in_map(object):
            self._action = "multiple"
            self._need_mana = 0
            return

        new_loc = self.location.towards(object.location, self.max_speed)
        self._action = "move"
        self._next_location = new_loc

    def under_attack(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            self.turns_to_revive = self.spawn_turns-1
            self.location = None

    def clear_locals(self):
        self._need_mana = 0
        self._action = ""
        self._attack_object = None
        self._next_location = None

    def do_your_thing(self):
        if not self.is_alive():
            if self.turns_to_revive > 0:
                self.turns_to_revive -= 1
                if self.turns_to_revive == 0:
                    game = get_game(self.owner)
                    self.location = self.initial_location
            else:
                game = get_game(self.owner)
                self.current_health = game.elf_max_health

            self.clear_locals()
            return

        game = get_game(self.owner)
        if self.is_building:
            self._turns_to_build -= 1
            if self._turns_to_build == 0:
                game.create_building(self.currently_building, self.location, self)
                self.currently_building = None
                self.is_building = False

        if self._action == "multiple":
            self.clear_locals()
            return

        if self._action == "build portal":
            if game.can_build_portal_at(self.location):
                self._need_mana = game.portal_cost
            else:
                self._action = ""
        if self._action == "attack":
            if not self.in_attack_range(self._attack_object):
                self._action = ""
        if self._action == "move":
            return

    def need_mana(self):
        return self._need_mana

    def clean_action_with_mana(self):
        if self._action == "build portal":
            self.clear_locals()

    def set_action(self):
        if self._action == "attack":
            self._attack_object.under_attack(self.attack_multiplier)
        if self._action == "move":
            self.location = self._next_location
        if self._action == "build portal":
            self.currently_building = "Portal"
            self.is_building = True
            self.owner.decrease_mana(self._need_mana)
            game = get_game(self.owner)
            self._turns_to_build = game.portal_building_duration

        self.clear_locals()