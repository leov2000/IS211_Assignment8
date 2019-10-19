from player import Player

class ComputerPlayer(Player):

    def execute_strategy(self, tally_count, cpu_score):

        if tally_count + cpu_score == 100:
            return 'h'
        elif tally_count >= 25:
            return 'h'
        else:
            return 'r'
