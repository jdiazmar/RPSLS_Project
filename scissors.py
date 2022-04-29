class Scissors:
    def __init__(self):
        self.scissors = "Scissors cut Paper!"
        

class ScissorsLizard(Scissors):
    def __init__(self):
        super().__init__(self)
        self.scissorslizard = "Scissors decapitates Lizard!"