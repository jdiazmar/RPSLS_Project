from asyncio import selector_events
from os import name
from select import select
import random


class Players:
    def __init__(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.score = 0

    def choose_gesture(self):
        pass
        

class Human(Players):
    def __init__(self) -> None:
        super().__init__(self)
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def choose_gesture(self):
        print('')
        for index in range(len(self.gestures)):
            print(f'{index} for {self.gestures[index]}')
        players_choice = input(f"{Human(Players)} Choose your gesture! ")
        while players_choice != "0" and players_choice != "1" and players_choice != "2" and players_choice != "3" and players_choice != "4":
            input(f"Please choose from 0-4 to select your gesture: ")
        players_choice = int(players_choice)
        if players_choice <= 4:
            players_choice = self.gestures[players_choice]
        print(f"Player 1 chose {players_choice}! ")
        return players_choice


class AI(Players):
    def __init__(self) -> None:
        super().__init__()
        

    def choose_gesture(self, player):
        random_number = random.randit(0, 4)
        ai_choice = self.gestures[random_number]
        print(f"The AI chose {ai_choice}! ")
        return ai_choice




    
