import Map
from Game import Game
from Player import Player

games = [None, None]
players = [None, None]
def get_game(owner):
    if owner.id < 0 or owner.id > 1:
        return None

    return games[owner.id]


class elf_kingdom:
    def __init__(self, mapa):
        current_map = mapa

        global players
        global games
        players[0] = mapa.get_player_0()
        players[1] = mapa.get_player_1()

        games[0] = Game(players[0], players[1], mapa)
        games[1] = Game(players[1], players[0], mapa)

        self.players = players
        self.games = games

    def do_turn(self, turn_number):
        self.games[0].turn = turn_number
        self.games[1].turn = turn_number

        self.players[0].do_turn(self.games[0])
        self.players[1].do_turn(self.games[1])

    def end_game(self):
        p0_lost = not players[0].is_alive()
        p1_lost = not players[1].is_alive()
        if p0_lost and not p1_lost:
            print "Player 1 WON"
        elif not p0_lost and p1_lost:
            print "Player 0 WON"
        else:
            print "Draw"

        return  p0_lost or p1_lost

if __name__ == '__main__':
    kingdom = elf_kingdom(Map.Default_Map())

    ended = False
    for i in range(1,750):
        kingdom.do_turn(i)
        if kingdom.end_game():
            ended = True
            break

    if not ended:
        print "Draw"
