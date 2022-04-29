class Lizard:
    def __init__(self):
        self.lizard = "Lizard poisons Spock!"

class LizardPaper(Lizard):
    def __init__(self):
        super().__init__(self)
        self.lizardpaper = "Lizard eats Paper!"