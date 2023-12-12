import random
def print_board(board):
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n")
def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
def get_player_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Try again.")
        elif board[row][col] != " ":
            print("That position is already filled. Try again.")
        else:
            return row, col
def get_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        # Player 1's turn
        row, col = get_player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board, "X"):
            print("you won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        # Player 2's turn
        if mode == "2P":
            row, col = get_player_move(board)
        else:
            row, col = get_computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board, "O"):
            if mode == "2P":
                print("oponent won!")
            else:
                print("Computer won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
mode = input("Choose game mode (1P for against computer, 2P for two players): ")
play_game()
