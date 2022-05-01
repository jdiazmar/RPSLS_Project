from players import Players
import random

class AI(Players):
    def __init__(self):
        super().__init__()
        

    def choose_gesture(self, player):
        random_number = random.randint(0, 4)
        ai_choice = self.gestures[random_number]
        print(f"The AI chose {ai_choice}! ")
        return ai_choice