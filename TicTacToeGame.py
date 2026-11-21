import random

board = [" " for i in range(9)]

def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False

def check_draw():
    return " " not in board

def computer_move():

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    if board[4] == " ":
        board[4] = "O"
        return

    empty_positions = [i for i in range(9) if board[i] == " "]
    if empty_positions:
        position = random.choice(empty_positions)
        board[position] = "O"

def play_game():

    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O.")

    while True:

        display_board()

        try:
            move = int(input("Enter your position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid position! Try again.")
            continue

        board[move] = "X"

        if check_winner("X"):
            display_board()
            print("Congratulations! You won!")
            break

        if check_draw():
            display_board()
            print("The game is a draw!")
            break

        computer_move()
        print("Computer played:")

        if check_winner("O"):
            display_board()
            print("Computer wins! Better luck next time.")
            break

        if check_draw():
            display_board()
            print("The game is a draw!")
            break

play_game()
