#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round

import random
import time

moves = ['rock', 'paper', 'scissors']

# Place time in between messages as they print to the screen.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

# The Player class is the parent class for all of the Players
# in this game
class Player:
    def __init__(self):
        self.score = 0
        self.move_choice = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# Create a player subclass that plays randomly
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# Create a subclass for a human player and
# Validate user input
class HumanPlayer(Player):
    def move(self):
        while True:
            player_input = input("Rock, paper, scissors? > ")
            if player_input.lower() in moves:
                return player_input.lower()
            else:
                print_pause("Please enter a valid command.")

# Create player classes that remember
class ReflectPlayer(Player):
    def move(self):
        return self.move_choice

    def learn(self, my_move, their_move):
        self.move_choice = their_move

class CyclePlayer(Player):
    def move(self):
        return self.move_choice

    def learn(self, my_move, their_move):
        if my_move == moves[0]:
            self.move_choice = moves[1]
        elif my_move == moves[1]:
            self.move_choice = moves[2]
        else:
            self.move_choice = moves[0]

# Create Game class and methods and
# Keep score and the number of rounds.
# Announce the winner after rounds end.
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rounds = 0

    def rounds_input(self):
        print_pause("Rock Paper Scissors, Go!\n")
        while True:
            try:
                self.rounds = int(input("How many rounds would you like to play? > "))
                if self.rounds <= 0:
                    print_pause("Please enter a positive number of rounds.")
                else:
                    break
            except ValueError:
                print_pause("That's not a valid number.")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"You played {move1}.\nOpponent played {move2}.")

        if beats(move1, move2):
            self.p1.score += 1
            print_pause("** PLAYER ONE WINS **")
        elif beats(move2, move1):
            self.p2.score += 1
            print_pause("** PLAYER TWO WINS **")
        else:
            print_pause("** TIE **")

        print_pause(f"Score: Player One {self.p1.score}, Player Two {self.p2.score}.")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        self.rounds_input()
        for round in range(1, self.rounds + 1):
            print_pause(f"\nRound {round} --")
            self.play_round()
        print_pause("The game is over!")

        if self.p1.score > self.p2.score:
            print_pause(f"** PLAYER ONE WINS BY A SCORE OF {self.p1.score} to {self.p2.score} **")
        elif self.p2.score > self.p1.score:
            print_pause(f"** PLAYER TWO WINS BY A SCORE OF {self.p2.score} to {self.p1.score} **")
        else:
            print_pause("** IT'S A TIE! **")

        self.new_game()

    def new_game(self):
        self.play_again = input("\nWould you like to play again? (Y/N) > ")
        if self.play_again.lower() in ["y", "yes"]:
            self.p1.score = 0
            self.p2.score = 0
            self.play_game()

if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([RandomPlayer(), ReflectPlayer(), CyclePlayer()]))
    game.play_game()
