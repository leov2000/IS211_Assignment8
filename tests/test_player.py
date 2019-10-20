import os
import sys
import unittest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, 'human')

    def test_player_has_name_value(self):
        player_name = self.player.get_player_name()

        self.assertEqual(player_name, 1)

    def test_player_tally_has_values(self):
        self.player.append_score_tally(5)
        self.player.append_score_tally(3)
    
        self.assertEqual(self.player.sum_tally(), 8)
    
    def test_player_rolling_state(self):
        self.player.set_player_rolling_state(True)
        rolling_state = self.player.get_player_rolling_state()

        self.assertEqual(rolling_state, True)

    def test_player_score_value(self):
        self.player.add_to_score(5)
        self.player.add_to_score(18)

        current_score = self.player.get_player_score()

        self.assertEqual(current_score, 23)
    
    def test_player_score_state_after_reset(self):
        (score, _) = self.player.reset_score()
        
        self.assertEqual(score, 0)

    def test_player_tally_state_after_reset(self):
        (_, tally) = self.player.reset_score()

        self.assertEqual(tally, [])
    
