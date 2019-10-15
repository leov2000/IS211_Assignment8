class Player:
    
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.tally = []
        self.rolling = False

    def reset_score(self):
        """
        A function responsible for resetting the score.

        Returns: a tuple with the reset score
        """
        self.score = 0    
        self.tally = []

        return (self.score, self.tally)
        
    def empty_score_tally(self):
        """
        A function responsible for resetting the tally.
        """
        self.tally = []
    
    def sum_tally(self):
        """
        A function responsible for summing the tally.
        
        Returns: the sum of the tally.
        """
        return sum(self.tally)

    def append_score_tally(self, num):
        """
        A function responsible for appending the score to a tally list.
        """
        self.tally.append(num)
    
    def add_to_score(self, score_num):
        """
        A function responsible for adding the score to the scorea attr.

        Parameters:
            score_num(int)
        """
        self.score = self.score + score_num

    def get_player_name(self):
        """
        A function responsible for returning the current player's name.
        """
        return self.name

    def get_player_rolling_state(self):
        """
        A function responsible for returning the current player's roll state.
        """
        return self.rolling

    def set_player_rolling_state(self, boolean):
        """
        A function responsible for setting the current player's roll state.
        """
        self.rolling = boolean

    def get_player_score(self):
        """
        A function responsible for returning the current player's score.
        """
        return self.score 