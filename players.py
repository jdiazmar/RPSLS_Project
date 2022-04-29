from asyncio import selector_events
from select import select


class Players:
    def __init__(self):
        self.players = []
        self.select_player()

    def view_player(self):
        pass 

    def select_player(self, name):
        self.name = name 

class SelectPlayers(Players):
    def __init__(self):
        super().__init__()
        pass 