import random

# Initialize the Tic Tac Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full (tie)
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function for the computer's move (random placement)
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Main game loop
while True:
    player1 = input("Player 1, enter 'X' or 'O': ").upper()
    if player1 not in ["X", "O"]:
        print("Invalid choice. Please enter 'X' or 'O'.")
        continue

    player2 = "X" if player1 == "O" else "O"

    print("Tic Tac Toe Game Start!")
    print_board(board)

    current_player = player1

    while True:
        row, col = None, None

        if current_player == "X" or (current_player == "O" and player2 == "X"):
            while True:
                try:
                    row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
                    col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers for row and column.")

        elif current_player == "O":
            row, col = computer_move(board)

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        current_player = player1 if current_player == player2 else player2

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye.")
        break


