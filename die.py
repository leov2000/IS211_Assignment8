from random import randint

class Die:
    
    def __init__(self): 
        self.side = 0
        self.roll_count = 0

    def reset_die_side(self):
        """
        A function delegated to reseting the side state
        
        Parameters: None
        """
        self.side = 0
    
    def reset_roll_count(self):
        """
        A function delegated to reseting the count state
        
        Parameters: None
        """
        self.roll_count = 0
    
    def roll_the_die(self):
        """
        A function delegated to setting the roll and count state
        
        Parameters: None

        Returns: a random int from 1-6.
        """
        random_num = randint(1,6)

        self.side = random_num
        self.roll_count = self.roll_count + 1

        return self.side
    
    def get_die_state(self):
        """
        A function deleted to retrieving the side and count state of the die.

        Parameters: None
        """
        return (self.side, self.roll_count)