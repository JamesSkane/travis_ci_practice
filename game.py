
import os, sys
from random import choice
from rps.moves import Rock, Paper, Scissors

class Game:
    def __init__(self, player, rounds=3):
        self.rounds = rounds
        self.player = player
        self.score = [0,0]

    def _convert_move(self, move):
        if move == 'r':
            return Rock()
        elif move == 'p':
            return Paper()
        elif move == 's':
            return Scissors()

    def summary(self, title):
        print("\n{}".format(title))
        print("-"*len(title))
        print("{}: {}".format(self.player, self.score[0]))
        print("Computer: {}\n".format(self.score[1]))

    def get_move(self, move=None):
        move = move or input("[R]ock, [P]aper, [S]cissors?").lower()
        if move == 'q':
            print 'Bye!'
            sys.exit()
        elif move not in list('rps'):
            return self.get_choice()
        return self._convert_move(move)

    def game_round(self):
        player_move = self.get_move()
        computer_move = self._convert_move(choice(list('rps')))
        if player_move > computer_move:
            self.score[0] += 1
            print("You won that round, {}!".format(self.player))
        elif computer_move > player_move:
            self.score[1] += 1
            print("You lost that round, {}!".format(self.player))
        else:
            print("You tied!")
        self.summary("Current Score")

    def game_over(self):
        if self.score[0] > self.score[1]:
            print "You won!"
        else:
            print "Better luck next time!"

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game(player=input("Whats your name?"))

    while 3 not in game.score:
        game.game_round()
    else:
        game.game_over()



