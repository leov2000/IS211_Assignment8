def safe_int_checker(int_str):
    """
    A function that checks if the string is actually an int. used for the CLI.

    Parameters:
        int_str(str): A string representing an int.

    Returns:
        A tuple with a boolean as the first item and a value if its successfuly cast or None if it isnt.
    """

    try:
        num = int(int_str)
        return (True, num)
    except ValueError:
        return (False, None)

def print_graphics(file_name):
    """
    A print utility function that prints out the PIG and END logo

    Parameters:
        file_name(<text_file>): A text file
    """

    text_header = "$" * 51

    ascii_file = open(file_name, 'r')
    ascii_text = ascii_file.read()

    print(text_header)
    print(ascii_text)
    print(text_header)

def print_unintended_keystroke():
    """
    A print utility function that prints out an error message 

    Parameters:None
    """

    print("Hmm.. not sure what that was, please click on 'r' or 'h' ")

def print_current_score(score_list, game_num, current_player = None):
    """
    A print utility function that prints out the curent score

    Parameters:
        score_list(list[dict[str, int]])
        game_num(int)
        current_player(<Player>)
    """

    (player_name, player_tally) = (current_player.get_player_name(), current_player.sum_tally())
    text_header = '$' * 17 
    text_footer = '$' * 51

    print(f'{text_header}[-GAME-{game_num}-SCORE-]{text_header}')
    print('\n')

    for player_score_details in score_list:
        append_string = f'TALLY: {player_tally}' if player_score_details['player_name'] == player_name and current_player.get_player_rolling_state() else ''
        print(f'PLAYER {player_score_details["player_name"]} SCORE: {player_score_details["player_score"]} {append_string}')
        print('\n')

    print(text_footer)

def print_die_roll_message(num, player_name):
    """
    A print utility function that prints out the player's current roll

    Parameters:
        num(int)
        player_name(str)
    """
    
    roll_message = f'Player {player_name} rolled a {num} You lost a turn...\n' if num == 1 else f'Player {player_name} rolled a {num}! Adding it to the tally...\n'
    print(roll_message)

def get_winner(player_list):
    """
    A utility function that retrieves the winner of the game when the game ends.
    
    Parameters:
        player_list(list[dict[str, int]])
    """

    highest_score = sorted(player_list, key= lambda k: k['player_score'])
    highest_score.reverse()
    
    return highest_score[0]

def print_game_winner(score_dict, game_num):
    """
    A utility function that prints the game winner

    Parameters:
        score_dict(dict[str,int])
        game_num(int)
    """

    name = score_dict.get('player_name')
    score = score_dict.get('player_score')
    print('\n')
    print('*' * 51)
    print(f'\nPlayer {name} won GAME:{game_num} with a SCORE OF: {score} !!!!\n')
    print('*' * 51)
    print('\n')
