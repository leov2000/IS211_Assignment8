
import logging
import time
from game import Game
from timed_proxy import TimedProxy
from timed_game_proxy import TimedGameProxy
from die import Die
from player_factory import PlayerFactory
from utilities import print_current_score, print_die_roll_message, get_winner, print_game_winner, print_unintended_keystroke

class Play:
    
    def __init__(self, player_list, timed):
        self.factory = PlayerFactory()
        self.players = [self.factory.get_player_type(player, index+1) for index, player in enumerate(player_list) ]
        self.game = TimedGameProxy(TimedProxy(Game(self.players, Die())))
        self.game.set_time(timed)
        self.CLI = True 
        self.game_num = 0
        self.timed = timed 

    def timed_game(self, current_game, game_players):
        start_time = time.time()
        time_elapsed = 0

        while self.CLI:

            while current_game.check_highest_score() < 100 or time_elapsed > self.game.get_time():
                time_elapsed = time.time() - start_time

                for player in game_players:
                    player.set_player_rolling_state(True)

                    while player.get_player_rolling_state() and current_game.check_highest_score() < 100 and time_elapsed < self.game.get_time():
                        time_elapsed = time.time() - start_time

                        if time_elapsed > self.game.get_time():
                            self.end_game(current_game)
                            return
                        else:
                            self.check_player_input(player, current_game)
                        

            if current_game.check_highest_score() >= 100 or time_elapsed > self.game.get_time():
                self.end_game(current_game)
                
    
    def play_reg_game(self, current_game, game_players):
        while self.CLI:

            while current_game.check_highest_score() < 100:

                for player in game_players:
                    player.set_player_rolling_state(True)
            
                    while player.get_player_rolling_state() and current_game.check_highest_score() < 100:
                        self.check_player_input(player, current_game)

            if current_game.check_highest_score() >= 100:
                self.end_game(current_game)

    def start(self):
        """
        The start function of the play class that encapsulates the rules of the game.

        Parameters: None
        """
        current_game = self.game
        game_players = current_game.get_players()

        self.play_reg_game(current_game, game_players) if self.timed == 0 else self.timed_game(current_game, game_players)
    
    def check_player_input(self, player, current_game):
        """
        A function that checks the key input entered by a player on their turn.

        Parameters:
            player(<Player>)
            current_game(<Game>)
        
        Logs: An error if a key is entered that isn't an 'h' or 'r'
        """
        if player.factory_type == 'computer':
            tally = current_game.sum_tally(player)
            cpu_score = player.get_player_score()
            cpu_input = player.execute_strategy(tally, cpu_score)

            self.hold_action(player, current_game) if cpu_input == 'h' else self.roll_action(player, current_game)

            return 

        player_input = input(f'Player {player.get_player_name()} would you like to ("r") roll or ("h") hold?\n')
        
        if player_input.lower() == 'h':
            self.hold_action(player, current_game)
        elif player_input.lower() == 'r':
            self.roll_action(player, current_game)
        else:
            print_unintended_keystroke()
            logging.error(f'unintended_keystroke for Player: {player.get_player_name()} typed in: {player_input}')

    def hold_action(self, player, current_game):
        current_game.hold(player)
        score_list = current_game.get_score_list()
        print_current_score(score_list, self.game_num+1, player)


    def roll_action(self, player, current_game):
        num_rolled = current_game.roll_die(player)
        score_list = current_game.get_score_list()
        print_die_roll_message(num_rolled, player.get_player_name(), player.factory_type)
        print_current_score(score_list, self.game_num+1, player)

    def retreive_winner(self, current_game):
        """
        A function that retrieves the winner of a game and prints it.

        Parameters:
            current_game(<Game>)
        """

        high_scorer = get_winner(current_game.get_score_list())
        print_game_winner(high_scorer, self.game_num+1)

    def end_game(self, current_game):
        """
        A function that resets a game ends it and moves onto the next game if present.

        Parameters:
            current_game(<Game>)
        """
        self.retreive_winner(current_game)
        self.game_num  = self.game_num  + 1
        current_game.reset_game()
        self.CLI = False