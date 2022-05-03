from lib2to3.pytree import _Results
import re
from unittest import result
from human import Human
from ai import AI
from players import Players
player = Players()


class Game:
    def __init__(self) -> None:
        self.player_one = Human()
        self.player_two = Human()

    def run_game(self) -> None:
        self.display_welcome()
        single_player = self.single_play_game()
        if single_player == True:
            self.player_two = AI()
        while self.player_one.score < 2 and self.player_two.score < 2:
            winner = self.who_won_gestures(self.player_one.choose_gesture('Player One'), self.player_two.choose_gesture('Player Two'))
            if winner == "Player One has won":
                self.player_one.score += 1
            elif winner == "Player Two has won":
                self.player_two.score += 1
            print(f'{winner} this round! ')
        self.display_winner(self.player_one.score, self.player_two.score)

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, & Spock!")
        print("")
        print("Here are the rules for RPSLS: ")
        print("Rock crushes Scissors!")
        print("Scissors cuts Paper!")
        print("Paper covers Rock!")
        print("Rock crushes Lizard!")
        print("Lizard poisons Spock!")
        print("Spock smashes Scissors!")
        print("Scissors decapitates Lizard!")
        print("Lizard eats Paper!")
        print("")
        print("Let the games BEGIN!")

    def single_play_game(self):
        players_choice = ''
        while players_choice != '1' and players_choice != '2':
            players_choice = input("Enter '1' for single player or '2' for multiplayer game mode: ")
            if players_choice != '1' and players_choice != '2':
                print("Please enter '1' or '2' ")
        if players_choice == '1':
            return True
        else: 
            return False 

    def who_won_gestures(self, gesture_one, gesture_two):
        if gesture_one == gesture_two:
            return "It's a DRAW! Let's PLAY AGAIN!"

        if self.player_one.gestures == "Rock" and self.player_two.gestures == "Scissors":
            print('Rock crushs Scissors!')
            return results == 1 
        elif self.player_one.gestures == "Rock" and self.player_two.gestures == "Paper":
             print('Paper covers Rock!')
             return results == 0
        elif self.player_one.gestures == "Rock" and self.player_two.gestures == "Lizard":
             print('Rock crushes Lizard!')
             return results == 1
        elif self.player_one.gestures == "Rock" and self.player_two.gestures == "Spock":
             print('Spock vaporizes Rock!')
             return results == 0
        elif self.player_one.gestures == "Scissors" and self.player_two.gestures == "Rock":
            print('Rock crushes Scissors')
            return results == 0
        elif self.player_one.gestures == "Scissors" and self.player_two.gestures == "Spock":
            print('Spock smashes Scissors')
            return results == 0
        elif self.player_one.gestures == "Scissors" and self.player_two.gestures == "Lizard":
            print('Scissors decapitates Lizard')
            return results == 1
        elif self.player_one.gestures == "Scissors" and self.player_two.gestures == "Paper":
            print("Scissors cut Paper!")
            return results == 1
        elif self.player_one.gestures == "Paper" and self.player_two.gestures == "Rock":
            print("Paper covers Rock!")
            return results == 1
        elif self.player_one.gestures == "Paper" and self.player_two.gestures == "Scissors":
            print('Scissors cuts Paper')
            return results == 0
        elif self.player_one.gestures == "Paper" and self.player_two.gestures == "Lizard":
            print('Lizard eats Paper')
            return results == 0
        elif self.player_one.gestures == "Paper" and self.player_two.gestures == "Spock":
            print("Paper disproves Spock!")
            return results == 1
        elif self.player_one.gestures == "Lizard" and self.player_two.gestures == "Spock":
            print("Lizard poisons Spock!")
            return results == 1
        elif self.player_one.gestures == "Lizard" and self.player_two.gestures == "Rock":
            print('Rock crushes Lizard')
            return results == 0
        elif self.player_one.gestures == "Lizard" and self.player_two.gestures == "Scissors":
            print('Scissors decapitates Lizard')
            return results == 0
        elif self.player_one.gestures == "Lizard" and self.player_two.gestures == "Paper":
            print("Lizard eats Paper!")
            return results == 1
        elif self.player_one.gestures == "Spock" and self.player_two.gestures == "Scissors":
            print("Spock smashes Scissors!")
            return results == 1
        elif self.player_one.gestures == "Spock" and self.player_two.gestures == "Paper":
            print('Paper disproves Spock')
            return results == 0
        elif self.player_one.gestures == "Spock" and self.player_two.gestures == "Lizard":
            print('Lizard poisons Spock')
            return results == 0
        elif self.player_one.gestures == "Spock" and self.player_two.gestures == "Rock":
            print("Spock vaporizes Rock!")
            return results == 1

        
        results = Players.gestures[gesture_one].count(gesture_two)

        if results == 1:
            return 'Player One has won this round!'
        else:
            return 'Player Two has won this round!'
        

        

    def display_winner(self, player_one_scoresheet, player_two_scoresheet):
        if player_one_scoresheet > player_two_scoresheet:
            print('Player One has won the game of RPSLS!!!')
        else:
            print('Player Two has won the game of RPSLS!!!')