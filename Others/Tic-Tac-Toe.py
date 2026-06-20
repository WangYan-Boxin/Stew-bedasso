board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "X"


def print_board():
    for row in board:
        print(*row)


def check_win(player):
    # 检查所有行
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # 检查所有列
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # 检查两条对角线
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_tie():
    for row in board:
        if "-" in row:
            return False
    return True


running = True

while running:
    print_board()
    print(f"Player {current_player}'s turn")

    while True:
        try:
            row = int(input("Enter row 0, 1, or 2: "))
            col = int(input("Enter column 0, 1, or 2: "))


            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Please enter 0, 1, or 2.")
                continue

            if board[row][col] != "-":
                print("That cell is already taken! Try another one.")
                continue

            break

        except ValueError:

            print("Invalid input! Please enter valid numbers.")


    board[row][col] = current_player


    if check_win(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        running = False
        break


    if check_tie():
        print_board()
        print("It's a tie!")
        running = False
        break


    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"