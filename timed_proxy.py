from game import Game

class TimedProxy(Game):
    def __init__(self, subject):
        self._subject = subject
        self.time = None
        self.players = subject.players
        self.turn = subject.turn
        self.end = subject.end
        self.die = subject.die
