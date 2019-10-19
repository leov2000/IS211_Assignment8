
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
    
    logging.basicConfig(filename='errors_log/errors.log', level=logging.ERROR, format='%(message)s')
    logging.getLogger('assignment8')

    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', default="human", help='choose human or computer')
    parser.add_argument('--player2', default="human", help='choose human or computer')
    parser.add_argument('--timed', default=0, const=60, nargs='?', help='pass the --timed flag to play for 1 min.')
    
    args = parser.parse_args()

    player1 = args.player1 
    player2 = args.player2
    timed = args.timed 

    print(player1, 'PLAYER1')
    print(player2, "PLAYER2")
    print_graphics('artwork/PIG-ART.txt')

    play = Play([player1, player2], timed)
    play.start()

    print_graphics('artwork/END.txt')
    print("\nThank you for playing PIG. Please run the script to play again!\n")

if __name__ == '__main__':
    main()
