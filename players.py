from asyncio import selector_events
from os import name
from select import select


class Players:
    def __init__(self):
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()
        

class HumanPlayer:
    def __init__(self) -> None:
        super().__init__(self)
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def choose_gesture(self):
        pass

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()
        

class ComputerPlayer:
    def __init__(self) -> None:
        super().__init__(name)
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()





    
