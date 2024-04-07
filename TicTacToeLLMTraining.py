import random
import os

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)
    game_number = 1

    game_moves = []

    while game_number <= 2000:
        game_moves.append(f"game{game_number} = [\n")
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = random.choice(players)
        game_moves.append({"role": "computer", "content": f"Game {game_number}"})

        for _ in range(9):
            available_moves = get_available_moves(board)

            if not available_moves:
                game_moves.append({"role": "computer", "content": "It's a tie!"})
                break

            if current_player == "X":
                row, col = random.choice(available_moves)
                board[row][col] = "X"
                game_moves.append({"role": "user", "content": f"Player X placed at ({row}, {col})"})
            else:
                row, col = random.choice(available_moves)
                board[row][col] = "O"
                game_moves.append({"role": "assistant", "content": f"Player O placed at ({row}, {col})"})

            if check_winner(board, current_player):
                game_moves.append({"role": "computer", "content": f"Player {current_player} wins!"})
                break

            current_player = "O" if current_player == "X" else "X"
        
        game_moves.append("]\n\n")
        game_number += 1

    # Save game history to a file
    file_path = os.path.join(os.path.expanduser("~"), "Downloads", "TicTacToeTraining.txt")
    with open(file_path, "w") as f:
        for move in game_moves:
            if isinstance(move, dict):
                f.write(f"    {str(move)},\n")
            else:
                f.write(move)

if __name__ == "__main__":
    play_tic_tac_toe()
