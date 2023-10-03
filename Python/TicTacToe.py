import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))
bbhbhbh
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    if all(board[i][i] == player for i in range(len(board))) or all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board, player):
    while True:
        try:
            row = int(input(f"{player}, choose row (0-{len(board) - 1}): "))
            col = int(input(f"{player}, choose column (0-{len(board) - 1}): "))

            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def play_game():
    print("Welcome to Tic Tac Toe!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    while True:
        board_size = int(input("Enter board size (e.g., 3 for a 3x3 board): "))
        if board_size >= 3:
            break
        else:
            print("Board size must be at least 3x3.")

    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    current_player = player1
    players = [player1, player2]

    while True:
        print_board(board)
        row, col = get_player_move(board, current_player)
        board[row][col] = "X" if current_player == player1 else "O"

        if check_win(board, "X" if current_player == player1 else "O"):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
