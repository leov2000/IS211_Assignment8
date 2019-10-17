from player import Player
from computer_player import ComputerPlayer

class PlayerFactory:
     def get_player_type(self, factory_type, name):
         name = f'{factory_type} name'

         if factory_type == 'human':
            return Player(name)
         if factory_type == 'computer':
             return ComputerPlayer(name)

