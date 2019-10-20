import os
import sys
import unittest
import random
from functools import reduce

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from game import Game 
from player import Player 
from die import Die 

class TestGame(unittest.TestCase):
    
    def setUp(self):
        player_list = [Player(player_name, 'human') for player_name in range(0,2)]
        self.game = Game(player_list, Die())
    
    def simulate_game_attempts(self, tries):
        i = 0 

        while i <= tries:
            random_index = random.choice([0,1])
            player = self.game.get_players()[random_index]
            die_roll_num = self.game.roll_die(player)
            player.add_to_score(die_roll_num)

            i = i + 1

    def sum_game_score(self):
        score_list = self.game.get_score_list()
        score_comp = [[v for k,v in player_dict.items() if k == 'player_score' ] for player_dict in score_list ]
        score_sum = reduce(lambda x,y: x[0] + y[0], score_comp)

        return score_sum

    def test_game_has_players(self):
        player_list = self.game.get_players()

        self.assertEqual(isinstance(len(player_list), int), True)

    def test_game_player_roll(self):
        player_one = self.game.get_players()[0]

        die_roll_num = self.game.roll_die(player_one)

        self.assertEqual(isinstance(die_roll_num, int), True)

    def test_game_high_score(self):
        high_score = self.game.check_highest_score()

        self.assertEqual(isinstance(high_score, int), True)

    def test_game_functionality(self):
        self.simulate_game_attempts(1000)

        score_sum = self.sum_game_score()
        
        self.assertEqual(score_sum > 0, True)

    def test_game_reset_functionality(self):
        self.simulate_game_attempts(100)
        self.game.reset_game()
        score_sum = self.sum_game_score()

        self.assertEqual(score_sum, 0)
