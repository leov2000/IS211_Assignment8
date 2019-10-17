from game import Game
from timed_proxy import TimedProxy

class TimedGateProxy(TimedProxy):
    def get_time(self):
        return self.time

    def set_time(self, new_time):
        self.time = new_time 