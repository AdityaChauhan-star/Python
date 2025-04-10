#Task 2 : Tic Tac Toe Game

# Create a simple Tic Tac Toe game that can beplayed between two players or against
# thecomputer.

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def get_free_positions(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def get_random_move(board):
    return random.choice(get_free_positions(board))

def player_move(board, player):
    while True:
        try:
            row = int(input(f"{player}'s turn. Enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"{player}'s turn. Enter the column (1, 2, or 3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)

    while True:
        for player in players:
            print_board(board)

            if player == "X":
                row, col = player_move(board, player)
            else:
                row, col = get_random_move(board)

            board[row][col] = player

            if is_winner(board, player):
                print_board(board)
                print(f"{player} wins!")
                return

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                return

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
