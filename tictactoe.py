#!/usr/bin/env python3

""" This program designed to play TIC TAC TOE Game """

from IPython.display import clear_output

# Globals
board = [' '] * 10
game_on = True
result = ' '

def banner():
    print("#" * 60)
    print(" TIC TAC TOE ")
    print("#" * 60,"\n\n")

def reset_board():
    """ reset_board: Initializes the board to blanks """
    global board, game_on
    board = [' '] * 10
    game_on = True

def display_board():
    # Not using 0 index
    """ display_board: Displays the board """
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-' * 12)
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-' * 12)
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')

def winner(board,player):
    """winner: Checks whether a player is winner based on alignment of mark """    
    if ((board[7] == board[8] == board[9] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[1] == board[2] == board[3] == player) or \
        (board[7] == board[4] == board[1] == player) or \
        (board[8] == board[5] == board[2] == player) or \
        (board[9] == board[6] == board[3] == player) or \
        (board[7] == board[5] == board[3] == player) or \
        (board[9] == board[5] == board[1] == player)):
        return True
    else:
        return False

def full_board(board):
    """ full_board: Check whether the board is full """
    if ' ' in board[1:]:
        return False
    else:
        return True 

class player(object):
    """ player: Player class that lets the player to choose the mark """
    def __init__(self,mark):
        self.mark = str(mark).upper()    # X or O

def validate_mark():

    """validate_mark: Check for valid input, either X or O """

    while True:
        try:
            mark = input('Enter the mark X or O:').upper()
    
        except ValueError as err:
            print("Invalid mark, please enter 'X' or 'O' {0}".format(err))

        if mark == 'X' or mark == 'O':
            print('Valid mark')
            break
        else:
            print("Invalid mark, please enter 'X' or 'O' ")
            continue

    return mark

def ask_player(mark):

    """ ask_player: Function asks the player as to where to place the mark, if the 
                    space is empty, it places his mark there
   
        Argument:
            mark: Player's mark is passed as the argument, it's either X or O """

    print('Choose a position to place your mark', mark)
    while True:
        try:
            choice = int(input("Where do you want to place your mark? valid option [1-9]"))

        except ValueError as err:
            print('You entered an invalid number, please try again. Enter a between number 1-9 {0}'.format(err))
            continue

        if choice not in range(1,10):
            print('Invalid number, please enter a number between 1-9')
            continue

        if board[choice] == ' ':
            board[choice] = mark
            break
        else:
            print('The place is taken. Please try another number between 1-9')
            continue

def player_choice(mark):

    global board,game_on,result

    result = ' '
    ask_player(mark)

    # Check for win
    if winner(board,mark):
        clear_output()
#        display_board()
        result = mark + 'Congratulations! you won the game'
        game_on = False

    # Display the board
    clear_output()
    display_board()

    if full_board(board):
        result = "It's a TIE!"
        game_on = False

    clear_output()

    return game_on,result

def game():

    reset_board()
    global result

    banner()
    p1 = player(validate_mark())
    if p1.mark == 'X':
        p2 = player('o')
    elif p1.mark == 'O':
        p2 = player('x')

    while True:
    
        clear_output()
        display_board()

        game_on,result = player_choice(p1.mark)
        print(result)
        if game_on == False:
            break

        game_on,result = player_choice(p2.mark)
        print(result)
        if game_on == False:
            break

    # Ask whether they want to replay the game
    cont = input('Do you want to play Tic Tac Toe again?').lower()
    if cont == 'y': 
        game()
    else:
        print('Thanks for playing. Wrapping up')
        reset_board()

def main():
    game()

if __name__ == '__main__':
    main()
