from elf_kingdom import *
from BaseObject import games, players

class elf_kingdom:
    def __init__(self, mapa):
        self.current_map = mapa

        global players
        global games
        players[0] = mapa.get_player_0()
        players[1] = mapa.get_player_1()
        players[0].set_opponent(players[1])
        players[1].set_opponent(players[0])

        games[0] = Game(players[0], players[1], mapa)
        games[1] = Game(players[1], players[0], mapa)

        self.players = players
        self.games = games

    def do_turn(self, turn_number):
        self.set_new_turn(turn_number)

        # try:
        #     do_turn_0(self.games[0])
        # except:
        #     self.players[0].is_alive = False
        #     print "Player 0 crash"
        #     return
        #
        # try:
        #     do_turn_1(self.games[1])
        # except:
        #     self.players[1].is_alive = False
        #     print "Player 1 crash"
        #     return
        do_turn_0(self.games[0])
        do_turn_1(self.games[1])

        self.set_board()

    def set_new_turn(self, turn_number):
        for g in self.games:
            g.turn = turn_number
            g.update_mana_per_turn()

    def set_board(self):
        for p in players:
            p.do_your_things()

        for i, p in enumerate(players):
            ok = p.have_enough_mana(self.games[i])
            if not ok:
                p.clean_mana_operations()

            p.set_actions()

    def end_game(self, last_turn=False):
        p0_lost = not self.players[0].is_alive()
        p1_lost = not self.players[1].is_alive()
        if p0_lost and not p1_lost:
            print "Player 1 WON"
            return 2
        elif not p0_lost and p1_lost:
            print "Player 0 WON"
            return 1
        elif p0_lost and p1_lost:
            print "Draw"
            return 3
        elif last_turn:
            score0 = self.players[0].score
            score1 = self.players[1].score
            if score0 > score1:
                print "Player 0 WON"
                return 1
            elif score0 < score1:
                print "Player 1 WON"
                return 2
            else:
                print "Draw"
                return 3

        return 0

    def run_game(self,number_of_turns):
        for i in range(1, number_of_turns + 1):
            # print i
            kingdom.do_turn(i)
            ended = kingdom.end_game()
            if ended != 0:
                return ended

        ended = kingdom.end_game(True)
        return ended


if __name__ == '__main__':
    kingdom = elf_kingdom(Map.Default_Map())
    number_of_turns = 350

    winner = kingdom.run_game(number_of_turns)
    exit(winner)