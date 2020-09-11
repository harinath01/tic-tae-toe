# tic tac toe board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# to print the winner at the end
winner = None

# To know the current player
current_player = "X"

game_still_going = True


# To display a board
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# for handle the turn between X and O
def handle_turn(player):
    print(player+"'s turn")
    position = input('choose the position between 1 to 9 :')

    valid = False
    while not valid:
        # checking a input position is valid or not
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('enter the correct position')
            position = input('choose the position between 1 to 9 :')
        position = int(position)-1
        # check a given position empty or not
        # If empty current player will be store on that position
        # else print the message 'you can't go there'
        if board[position] == '-':
            valid = True
            board[position] = player
        else:
            print('you cant go there')
    # displaying a board after given position changed with symbols
    display_board()


# To check anyone won the match by checking rows, columns, diagonal
def check_for_winner():
    row_winner = check_rows()

    column_winner = check_column()

    diagonal_winner = check_diagonal()
    global winner

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

#checking rows
def check_rows():
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 | row2 | row3:
        global game_still_going
        game_still_going = False
        if row1:
            return board[0]
        elif row2:
            return board[3]
        elif row3:
            return board[6]

# checking a columns for the anyone wins
def check_column():
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'

    if col1 | col2 | col3:
        global game_still_going
        game_still_going = False
        if col1:
            return board[0]
        elif col2:
            return board[1]
        elif col3:
            return board[2]

# checking a diagonal, Is anyone wins
def check_diagonal():
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        global game_still_going
        game_still_going = False
        if diagonal1:
            return board[0]
        elif diagonal2:
            return board[2]


# for checking match is tie or not
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

# To flip the current player between X and O
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# check game still going or not
def check_if_game_over():
    check_for_winner()

    check_if_tie()


def playgame():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

#to print winner if anyone won
    if winner =='X' or winner == 'O':
        print(winner+' won the match')
    else:
        print('tie')

# to play a game
playgame()
