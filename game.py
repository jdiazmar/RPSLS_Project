from human import Human


class Game:
    def __init__(self) -> None:
        self.player_one = Human()
        self.player_two = Human()

    def run_game(self) -> None:
        pass

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

    def display_winner(self):
        pass 