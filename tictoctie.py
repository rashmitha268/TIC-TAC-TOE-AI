# CODSOFT AI Internship - Task 2
# Tic-Tac-Toe AI using Minimax Algorithm

import math

# Display the board
def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether there is a winner
def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c]:
            return board[a]

    return None


# Check if the board is full
def is_full(board):
    return " " not in board


# Minimax algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == "O":
        return 1

    if winner == "X":
        return -1

    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# Find the best move for AI
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main game
def play_game():
    board = [" "] * 9

    print("===== TIC-TAC-TOE AI =====")
    print("You are X")
    print("AI is O")

    print("\nBoard positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    while True:
        print_board(board)

        # Human move
        while True:
            try:
                position = int(input("Enter your position (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Please enter a number from 1 to 9.")
                elif board[position] != " ":
                    print("That position is already occupied.")
                else:
                    board[position] = "X"
                    break

            except ValueError:
                print("Please enter a valid number.")

        # Check human winner
        winner = check_winner(board)

        if winner == "X":
            print_board(board)
            print("🎉 Congratulations! You won!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")

        move = best_move(board)
        board[move] = "O"

        # Check AI winner
        winner = check_winner(board)

        if winner == "O":
            print_board(board)
            print("🤖 AI wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break


# Start the game
play_game()