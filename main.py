from Deck import Deck
from game import Game


from Player import Bot

if __name__ == '__main__':
    g = Game()
    g.start_game()

    print(g.player.money)