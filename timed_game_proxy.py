from game import Game
from timed_proxy import TimedProxy

class TimedGameProxy(TimedProxy):
    def get_time(self):
        return self._subject.time

    def set_time(self, new_time):
        self._time = new_time 