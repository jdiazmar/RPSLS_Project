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

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, & Spock!")
        print("")
        print("Here are the rules for RPSLS: ")
        print("Rock crushes Scissors\Scissors cuts Paper\Paper covers Rock\Rock crushes Lizard\Lizard poisons Spock\Spock smashes Scissors\Scissors decapitates Lizard\Lizard eats Paper!")
        print("Let the games BEGIN!")

    def single_play_game(self):
        players_choice = ''
        while players_choice != '1' and players_choice != '2':
            players_choice = input("Enter '1' for single player or '2' for multiplayer game mode: ")
            if players_choice != '1' and players_choice != '2':
                print("Please enter '1' or '2' ")
        if players_choice == '1':
            return True
        else: return False 

    def who_won_gestures(self, gesture_one, gesture_two):
        if gesture_one == gesture_two:
            return "It's a DRAW! Let's PLAY AGAIN!"
        

        

    def display_winner(self, player_one_scoresheet, player_two_scoresheet):
        if player_one_scoresheet > player_two_scoresheet:
            print('Player One has won the game of RPSLS!!!')
        else:
            print('Player Two has won the game of RPSLS!!!')