ROWS = 6
COLS = 7

# 初始化棋盘
board = []
for i in range(ROWS):
    row = []
    for j in range(COLS):
        row.append("-")
    board.append(row)

current_player = "X"


def print_board():
    for row in board:
        print(*row)
    print("0 1 2 3 4 5 6")


def drop_piece(col, player):
    # 从最底下一行开始向上查找空位
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = player
            return True
    return False


def check_win(player):
    # 1. 检查水平方向 (Horizontal win)
    # 列只需要循环到 COLS - 3，防止向右检查时越界
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # 2. 检查垂直方向 (Vertical win)
    # 行只需要循环到 ROWS - 3，防止向下检查时越界
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # 3. 检查正对角线 (Diagonal win \ 方向)
    # 从左上到右下，行和列都在增加
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # 4. 检查反对角线 (Diagonal win / 方向)
    # 从左下到右上，行在减少，列在增加。因此行从索引 3 开始向上检查
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

    return False


running = True

while running:
    print_board()
    print("Player", current_player, "turn")

    # 增加异常处理，防止用户输入非数字导致程序崩溃
    try:
        col = int(input("Choose a column 0-6: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if col < 0 or col >= COLS:
        print("Invalid column!")
        continue

    success = drop_piece(col, current_player)

    if not success:
        print("That column is full!")
        continue

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"