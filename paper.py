class Paper:
    def __init__(self):
        self.paper = "Paper covers Rock!"

class PaperSpock(Paper):
    def __init__(self):
        super().__init__(self)
        self.paperspock = "Paper disproves Spock!"
                