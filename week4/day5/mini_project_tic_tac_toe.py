#   -----------------------Tic Tac Toe Game

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# ------ Global variables
game_on = True
winner = None
current_player = 'x'


def play_game():
    display_board()

    # while the game is on, loop  till it stop (winner or tie)
    while game_on:
        player_input(current_player)

        # check if the game is over
        check_if_game_over()

        # change to another player
        switch_player()

    # while game is over, print the winner or tie
    if winner == "x" or winner == "o":
        print(winner, " won.")
    elif winner is None:
        print("It's a tie!")


def display_board():
    ''' Info: display the game board '''
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + '')
    print(board[3] + " | " + board[4] + " | " + board[5] + '')
    print(board[6] + " | " + board[7] + " | " + board[8] + '')
    print("\n")


def player_input(player):

    ''' info: handle turns and get valid position from player'''
    print(f'{player} now your turn.')
    position = input("Choose a position on the board between 1-9:")
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Choose a position on the board between 1-9:")

        # get the correct index for the board
        position = int(position) - 1

        # check if the cell is empty
        if board[position] == "-":
            valid = True
        else:
            print("You can't choose a taken spot on the board. Go again.")
        # print the player choice on board
        board[position] = player
        display_board()


def check_if_game_over():
    '''Info: check 2 conditions if the game is over, conditions references from other functions'''
    check_if_winner()
    check_if_tie()


def check_if_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonals()
    # get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_row():
    global game_on
    # check for 3 spots in a row are the same (but not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any of the rows have a match , there  is winner, and get True value below
    if row_1 or row_2 or row_3:
        game_on = False
    # return the winner player
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # return none if there is no row winner
    else:
        return None


def check_column():
    global game_on
    # check for 3 spots in a column are the same (but not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any of the columns have a match , there  is winner, and get True value below
    if column_1 or column_2 or column_3:
        game_on = False
    # return the winner player
    if column_1:
        return board[0]  # return any value put in the spot
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # return none if there is no coulmn winner
    else:
        return None


def check_diagonals():
    global game_on
    # check for 3 spots in a diagonal are the same (but not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any of the diagonl's have a match , there  is winner, and get True value below
    if diagonal_1 or diagonal_2:
        game_on = False
        # return the winner player
    if diagonal_1:
        return board[0]  # return any value put in the spot
    elif diagonal_2:
        return board[2]
    # return none if there is no row winner
    else:
        return None


def check_if_tie():
    global game_on
    # board is full
    if "-" not in board:
        game_on = False
        return True
    else:
        return False


def switch_player():
    global current_player
    if current_player == "x":
        current_player = "o"

    elif current_player == "o":
        current_player = "x"


play_game()
