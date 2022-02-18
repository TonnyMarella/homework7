from Deck import Deck
from Players import Bot
from Game import Game


if __name__ == '__main__':
    g = Game()
    g.start_game()

    print('My money:', g.player.money)