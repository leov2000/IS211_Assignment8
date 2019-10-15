
import argparse
import logging
from utilities import safe_int_checker, print_graphics
from play import Play

def main():
    """
    The primary function of this application that runs the game.

    Parameters:
        None

    Logs:
        An error if the string url is entered incorrectly.
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPlayers', default=2)
    args = parser.parse_args()

    logging.basicConfig(filename='errors_log/errors.log', level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment7')

    players = args.numPlayers
    (player_is_int, player_num) = safe_int_checker(players)

    print_graphics('artwork/PIG-ART.txt')
    keyed = input('\nHow many games would you like to play?\n')
    (game_is_int, game_num) = safe_int_checker(keyed)

    if game_is_int and player_is_int:
        play = Play(player_num, game_num)
        play.start()
    else:
        print(f'Something went wrong, you entered in games: "{keyed}" & players: "{players}"')
        logging.error(f'Error processing games key: "{keyed}" & players key: "{players}"')
        return SystemExit
    
    print_graphics('artwork/END.txt')
    print("\nThank you for playing PIG. Please run the script to play again!\n")

if __name__ == '__main__':
    main()
