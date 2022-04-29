class Spock:
    def __init__(self):
        self.spock = "Spock smashes Scissors!"
    

class SpockRock(Spock):
    def __init__(self):
        super().__init__(self)
        self.spockrock = "Spock vaporizes Rock!"