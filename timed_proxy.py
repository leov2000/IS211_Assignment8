from game import Game

class TimedProxy(Game):
    def __init__(self, subject):
        self._subject = subject
        self._time = None 
