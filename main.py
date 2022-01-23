import random

# Aid Variables
user_symbols = ["", ""]
switch_turn = [1, -1]


def check_if_valid(answer, valid_answers):
    """
    Check if the user type a valid input.
    param answer: User Choice.
    param valid_answers: All valid choices.
    return: True if valid, False if not valid.
    """
    if answer in valid_answers:
        return True
    else:
        print(f"Invalid input ({answer}). You can choose an input only from this list: {valid_answers}")
        return False


def create_board(difficulty):
    """
    Create the game board by the chosen difficulty.
    param: difficulty: User difficulty choice.
    return: The game board (as a list).
    """
    board = []
    if difficulty == 1:
        rows = 3
    else:
        rows = 4
    for row in range(rows):
        board.append([])
        for column in range(rows):
            board[row].append('_')

    return board


def print_board(board, difficulty):
    """
    Print the board to the screen.
    param board: The game board.
    return: None
    """
    if difficulty == 1:
        print("*   0    1    2")
    else:
        print("*   0    1    2    3")

    r = 0
    for row in board:
        print(f"{r} {row}")
        r += 1
    print("\n")


def create_player_list(mode):
    if mode == 0:
        player_list = ['P', 'P']
    elif mode == 1:
        player_list = ['P', 'C']
    else:
        player_list = ['C', 'C']
    return player_list


def choose_row_column(row_column, difficulty):
    """
    per row_column value, request a value per difficulty
    Check if the picked row is valid (by difficulty).
    param: difficulty: 1 - 3x3, 2 - 4x4
    return: The chosen row as an int.
    """
    choice_valid = False
    choice = ""
    while not choice_valid:
        choice = input(f"Pick a {row_column} to mark: ")
        if difficulty == 1:
            choice_valid = check_if_valid(choice, ['0', '1', '2'])
        else:
            choice_valid = check_if_valid(choice, ['0', '1', '2', '3'])
    row = int(choice)
    return row


def generate_location(symbol, board):
    """
    Generate random location to the computer player. And check if the location is empty.
    param symbol: The computer symbol
    param board: The game board
    return: The Updated gabe board
    """
    spot_clear = False
    c_row = 0
    c_column = 0
    while not spot_clear:
        if len(board) == 3:
            c_row = random.randint(0, 2)
            c_column = random.randint(0, 2)
            spot_clear = spot_is_clear(c_row, c_column, board)
        else:
            c_row = random.randint(0, 3)
            c_column = random.randint(0, 3)
            spot_clear = spot_is_clear(c_row, c_column, board)
    board[c_row][c_column] = symbol
    return board


def mark_board(row, column, symbol, board, player):
    """
    Mark the board in the select location.
    param row: chosen row.
    param column: chosen column.
    param symbol: symbol to mark with.
    param board: The current game board.
    param player: Get who is playing.
    return: The updated game board.
    """
    global players
    if players[player] == 'P':
        board[row][column] = symbol
        return board
    else:
        print("Computer play is: ")
        return generate_location(symbol, board)


def spot_is_clear(row, column, board):
    """
    Check is the selected spot is empty.
    param row: chosen row.
    param column: chosen column.
    param board: current game board.
    return: True if the spot is empty and False if the spot is taken.
    """
    if board[row][column] == '_':
        return True
    else:
        return False


def check_game_over(board, difficulty):
    """
    Check if there is a winner or not.
    param board: The game board.
    param difficulty: The board size.
    return: The winner symbol or 'noWin' if there isn't a winner.
    """
    for symbol in ['X', 'O']:
        if difficulty == 1:
            if board[0].count(symbol) == 3 or board[1].count(symbol) == 3 or board[2].count(symbol) == 3 or \
                    (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol) or \
                    (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol) or \
                    (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol) or \
                    (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or \
                    (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
                return symbol
        elif board[0].count(symbol) == 4 or board[1].count(symbol) == 4 or board[2].count(symbol) == 4 or \
                board[3].count(symbol) == 4 or \
                (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol and
                 board[3][0] == symbol) or \
                (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol and
                 board[3][1] == symbol) or \
                (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol and
                 board[3][2] == symbol) or \
                (board[0][3] == symbol and board[1][3] == symbol and board[2][3] == symbol and
                 board[3][3] == symbol) or \
                (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol and
                 board[3][3] == symbol) or \
                (board[0][3] == symbol and board[1][2] == symbol and board[2][1] == symbol and
                 board[3][0] == symbol):
            return symbol
    return "noWin"


def board_is_full(board):
    """
    Check if the board is full.
    param board: The game board.
    return: True if full, False if not full.
    """
    for row in board:
        for column in row:
            if column == "_":
                return False
    return True


def choose_difficulty():
    """
    Let the player choose the board size.
    return: 1 - 3x3 or 2 - 4x4.
    """
    difficulty_valid = False
    difficulty = 0

    print("Welcome to TicTacToe !")
    while not difficulty_valid:
        difficulty = input("Please choose difficulty :\n1 - 3x3\n2 - 4x4\n")
        difficulty_valid = check_if_valid(difficulty, ['1', '2'])

    return int(difficulty)


def choose_mode():
    """
    Let the player choose a game mode.
    return: 0 - PvP, 1 - PvC, 2 - CvC.
    """
    mode = input("Please choose mode: \n0 - Player vs Player\n1 - Player vs Computer\n2 - "
                 "Computer vs Computer\n")
    if check_if_valid(mode, ['0', '1', '2']):
        return int(mode)
    else:
        return choose_mode()


def set_players_symbols():
    """
    Let the plater choose a symbol.
    return: None.
    """
    global user_mode, user_symbols
    symbol_valid = False
    if user_mode == 0 or user_mode == 1:
        while not symbol_valid:
            user_symbols[0] = input("Choose your player1 symbol: 'X' or 'O'. ").upper()
            symbol_valid = check_if_valid(user_symbols[0], ['X', 'O'])
        if user_symbols[0] == 'X':
            user_symbols[1] = 'O'
        else:
            user_symbols[1] = 'X'
    else:
        user_symbols[0] = 'X'
        user_symbols[1] = 'O'


def check_if_possible_win():
    """
    Check if you can win in the current move.
    return: None. (Print Message)
    """
    for row_ix in range(len(game_board)):
        for column_ix in range(len(game_board)):
            if spot_is_clear(row=row_ix, column=column_ix, board=game_board):
                game_board[row_ix][column_ix] = user_symbols[turn]
                if check_game_over(game_board, user_difficulty) != "noWin":
                    print(f"You can win Now !!")
                game_board[row_ix][column_ix] = "_"


def choose_a_spot():
    """
    Let the player choose a spot to mark.
    return: Dict of the row and the column.
    """
    check_if_possible_win()
    user_row = choose_row_column("row", user_difficulty)
    user_column = choose_row_column("column", user_difficulty)
    if spot_is_clear(user_row, user_column, game_board):
        return {"row": user_row, "column": user_column}
    else:
        print("This spot is not empty. try again.")
        return choose_a_spot()


players = []

main_game = True
# The Main Loop
while main_game:
    # Setting up The Game
    user_difficulty = choose_difficulty()
    user_mode = choose_mode()
    set_players_symbols()
    players = create_player_list(user_mode)
    game_board = create_board(user_difficulty)
    print_board(game_board, user_difficulty)

    game_is_on = True
    turn = 0
# The Game Loop
    while game_is_on:
        if players[turn] == 'P':
            user_spot = choose_a_spot()
            game_board = mark_board(user_spot["row"], user_spot["column"], user_symbols[turn], game_board, turn)
        else:
            game_board = mark_board(0, 0, user_symbols[turn], game_board, turn)
# Switch Turns
        turn += switch_turn[turn]

        print_board(game_board, user_difficulty)
        win_test = check_game_over(game_board, user_difficulty)
        if win_test != "noWin":
            print(f"The winner is the {win_test} player.")
            play_again = input("Do you want to play again? Type 'y' or 'n'. ").lower()
            game_is_on = False
            if play_again != 'y':
                main_game = False

        if board_is_full(game_board) and game_is_on:
            print("It's a draw.")
            play_again = input("Do you want to play again? Type 'y' or 'n'. ").lower()
            game_is_on = False
            if play_again != 'y':
                main_game = False
