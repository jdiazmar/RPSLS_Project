from asyncio import selector_events
from os import name
from select import select


class Players:
    def __init__(self, name):
        self.name = name

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()
        

class HumanPlayer:
    def __init__(self) -> None:
        super().__init__(name)

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()
        

class ComputerPlayer:
    def __init__(self) -> None:
        super().__init__(name)

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()





    
