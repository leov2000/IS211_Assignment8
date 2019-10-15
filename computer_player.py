from player import Player

class ComputerPlayer(Player):

    def execute_strategy(self, tally_count):
        min_amt = (tally_count < 25) and (tally_count < (100 - tally_count))
        
        return 'h' if min_amt else 'r'
