import random
import os

# Function to check if a player has won
def check_win(board, player):
    # Check horizontal and vertical
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j <= len(board[0]) - 4 and all(board[i][j+k] == player for k in range(4)):  # Check horizontal
                return True
            if i <= len(board) - 4 and all(board[i+k][j] == player for k in range(4)):  # Check vertical
                return True

    # Check diagonals
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if all(board[i+k][j+k] == player for k in range(4)) or \
                    all(board[i+k][j+3-k] == player for k in range(4)):
                return True

    return False

# Function to check if the board is full (tie)
def check_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to make a move for the given player
def make_move(board, col, player):
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return row + 1, col + 1, len(board) - row  # Adjust indices and add Z coordinate
    return None

# Function to simulate AI moves
def ai_move(board, player):
    while True:
        col = random.randint(0, len(board[0]) - 1)
        move = make_move(board, col, player)
        if move:
            return move

# Function to play the game and write moves to a text file
def play_game():
    wins = 0
    ties = 0

    # Set the file path to save in Downloads directory
    file_path = os.path.join(os.path.expanduser('~'), 'Documents', 'DimensionalDominationTraining.txt')

    with open(file_path, 'w') as file:
        game_number = 1
        move_number = 1
        while wins < 2000:
            # Randomize board dimensions and winning requirement
            rows = random.randint(6, 12)
            cols = random.randint(6, 12)
            win_count = random.randint(4, 8)

            file.write(f"game{game_number} = [\n")
            move_number = 1
            game_number += 1
            file.write(f"    {{'role': 'computer', 'content': 'Board dimensions: {rows}x{cols}x{rows} (XYZ)'}},\n")
            move_number += 1
            file.write(f"    {{'role': 'computer', 'content': 'Number needed to win: {win_count}'}},\n")

            # Initialize the board
            board = [[" " for _ in range(cols)] for _ in range(rows)]
            while True:
                # AI 1's turn
                row, col, z = ai_move(board, "User")
                file.write(f"    {{'role': 'user', 'content': 'Player X placed at ({row}, {col}, {z})'}},\n")
                move_number += 1
                if check_win(board, "User"):
                    wins += 1
                    file.write(f"    {{'role': 'computer', 'content': 'Player X wins!'}}\n")
                    move_number += 1
                    file.write("]\n\n")
                    file.write("\n\n")
                    break

                # AI 2's turn
                row, col, z = ai_move(board, "Assistant")
                file.write(f"    {{'role': 'assistant', 'content': 'Player O placed at ({row}, {col}, {z})'}},\n")
                move_number += 1
                if check_win(board, "Assistant"):
                    wins += 1
                    file.write(f"    {{'role': 'computer', 'content': 'Player O wins!'}}\n")
                    move_number += 1
                    file.write("]\n\n")
                    file.write("\n\n")
                    break

                if check_full(board):
                    ties += 1
                    file.write(f"    {{'role': 'computer', 'content': 'It's a tie!'}}\n")
                    move_number += 1
                    file.write("]\n\n")
                    file.write("\n\n")
                    break

# Start the game
play_game()
