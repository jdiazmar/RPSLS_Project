from asyncio import selector_events
from select import select


class Players:
    def __init__(self, name):
        self.name = name

    def view_player(self):
        print(f"You chose {self.name}!")

    def player_selection(self, name):
        self.player_selection = name
        self.view_player()
        

player_one = Players("Rock")
player_one.view_player()
player_two =Players("Paper")
player_two.view_player()
player_three = Players("Scissors")
player_three.view_player()
player_four = Players("Lizard")
player_four.view_player()
player_five = Players("Spock")
player_five.view_player()




    
