# PLAY WITH "cmd" please.

# Importing "random" and "os" packages
import random
import os

# Defines the state variables.
player1_name = ''
player2_name = ''
player1_marker = ''
player2_marker = ''
players = []
player_turns = []
moves_list = []
game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Clears the "cmd" output:
def clear():
    os.system( 'cls' )

# Prints a game board with specified index objects from a list.
def display_board(board):
    print('          '+ '-------')
    print('          ' + '|' + board[7] + '|' + board[8] + '|' + board[9] + '|')
    print('          ' + '|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print('          ' + '|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print('          '+ '-------')

# Function that can take in a player input and assign their marker as 'X' or 'O'.
def player_register():
    marker1 = ''
    global player1_name
    player1_name_temp = input('      Hello Player 1! Please tell me your name:   ')
    player1_name = player1_name_temp[0].upper() + player1_name_temp[1:]
    print('      ')
    global player2_name
    player2_name_temp = input('      Hello Player 2! Please tell me your name:   ')
    player2_name = player2_name_temp[0].upper() + player2_name_temp[1:]
    print('      ')
    while marker1.lower() != 'x' or marker1.lower() != 'o':
        marker1 = input(f'      {player1_name}, please type x or o to select your marker.   ' )
        if marker1.lower() == 'x':
            marker2 = 'o'
            break
        elif marker1.lower() == 'o':
            marker2 = 'x'
            break
        else:
            continue
    global player1_marker
    player1_marker = marker1.upper()
    global player2_marker
    player2_marker = marker2.upper()

# Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, marker, player):
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


# Function that uses the random module to randomly decide which player goes first AND creates a list of strings of the player markers according to the order they will play.
def first_player():
    global players
    global player_turns
    global moves_list
    players = [player1_name, player2_name]
    first_one = players[random.randint(0,1)]

    if first_one == players[0]:
        moves_list = [player1_marker, player2_marker, player1_marker, player2_marker, player1_marker, player2_marker, player1_marker, player2_marker, player1_marker]

        player_turns = [player1_name, player2_name, player1_name, player2_name, player1_name, player2_name, player1_name, player2_name, player1_name]

    else:
        moves_list = [player2_marker, player1_marker, player2_marker, player1_marker, player2_marker, player1_marker, player2_marker, player1_marker, player2_marker]

        player_turns =[player2_name, player1_name, player2_name, player1_name, player2_name, player1_name, player2_name, player1_name, player2_name]


    print(f"   {first_one} will play first")

# Returns TRUE if a space is freely AVAILABLE on board, returns FALSE if a space is NOT AVAILABLE.
def position_available(position, game_board):
    #
    available_positions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if game_board[position] in available_positions:
        return True
    else:
        return False

# Asks player for their move. If they give a response outside the board indexes, asks again. If the position is not available (see function above), returns a string that informs this and asks again for a valid move.
def next_move(player, marker):
    temp_move = input(f"   {player}, please select a position for your move. (1-9)")
    available_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while temp_move not in available_moves:
        temp_move = input(f"   {player}, please enter a number to mark a position for your move. (1-9)")
    next_move = int(temp_move)
    while position_available(next_move, game_board) != True:
        #When position is occupied
        temp_move = input(f"   {player}, this position is occupied already. Please select another position. (1-9)")
        while temp_move not in available_moves:
            temp_move = input(f"   {player}, please enter a number to mark a position for your move. (1-9)")
        next_move = int(temp_move)
        if position_available(next_move, game_board) == True:
            game_board[next_move] = marker
            break
        else:
            continue

    while position_available(next_move, game_board) == True:
        while temp_move not in available_moves:
            temp_move = input(f"   {player}, please enter a number to mark a position for your move. (1-9)")
        next_move = int(temp_move)
        game_board[next_move] = marker
        break


# Asks the player if they want to play again and returns a boolean True if they do want to play again.
def play_again():
    yes_responses = ["yes", "'yes'", "y", "yep", "yey", "yay", "yea", "yeah", "yess", "yeap"]
    print('     ')
    response = input("   Would you like to play again? Type 'Yes' to play again.  ")
    if response.lower() in yes_responses:
        return True
    else:
        return False

# In-game architecture.
def play_game():
    global game_board
    game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('       ')
    switch = 0
    while switch < 9:
        player_register()
        first_player()
        print('       ')
        switch2 = 0
        while switch2 < 9:
            clear()
            print('       ')
            print("   Tic Tac Toe, by Rodi Şiyar Arserim")
            print('       ')
            print(f"   {player1_name}, playing as {player1_marker}    -    {player2_name}, playing as {player2_marker}")
            print('       ')
            display_board(game_board)
            print('       ')
            print('       ')
            next_move(player_turns[switch], moves_list[switch])
            print('       ')
            print('       ')
            if win_check(game_board, player1_marker, player1_name) == True:
                print(f"      {player1_name} has won.")
                break
            elif win_check(game_board, player2_marker, player2_name) == True:
                print(f"      {player2_name} has won.")
                break
            switch += 1
            switch2 += 1
            clear()
        else:
            print('     ')
            print('     ')
            print('      This game is a tie.')
            break
        break

# Gameplay
def tic_tac_toe():
    play_game()
    while play_again() == True:
        clear()
        play_game()
    else:
        print('      ')
        print('      ')
        bye = input("    Thank you for playing. Press 'enter' to exit.")

# Starts the game
tic_tac_toe()
