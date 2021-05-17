"""
Sodoku solver

using recursion and backtracking to solve the sodoku

"""

board = [
    [0, 1, 0, 0, 9, 6, 8, 3, 0],
    [9, 3, 0, 2, 0, 0, 0, 4, 0],
    [8, 2, 4, 7, 0, 3, 1, 0, 0],
    [0, 0, 5, 9, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 8, 5, 4, 2, 9],
    [2, 0, 8, 0, 0, 4, 0, 6, 1],
    [7, 0, 0, 0, 3, 0, 0, 8, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 3],
    [0, 0, 1, 0, 4, 9, 2, 0, 7]
]


# print the division line for the row and column
def print_board():
    # print 1st horizontal line boarder
    print("-------------------------")
    for i in range(1, len(board) + 1):

        for j in range(1, len(board[i - 1]) + 1):

            # print 1st vertical line boarder
            if j == 1:
                print("|", end=" ")

            print(board[i - 1][j - 1], end=" ")

            if j % 3 == 0 and j % 9 != 0:
                print("|", end=" ")
            elif j % 3 == 0:
                print("|")

        if i % 3 == 0:
            print("-------------------------")


# find the empty box with 0 value in the sudoku
def find_none(board):
    for x in range(len(board)):
        for y in range(len(board[x])):

            if board[x][y] == 0:
                return x, y  # row, column
    return None


# check if the number enter is valid
def chek_valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # check current box and check if num already exist in current box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    # if everything else is ok and return True
    return True


# main solve runs the recursion and back tracking algo
def solve(bo):

    # the base case
    find = find_none(bo)  # find next empty box (x, y)
    if not find:
        return True  # no more empty box in sudoku means game completed
    else:
        row, col = find  # (x,y)

    # check if the enter number is valid and add into the board
    for i in range(1, 10):

        if chek_valid(bo, i, (row, col)):

            # add the num to the board
            bo[row][col] = i

            # recursive call
            if solve(bo):
                return True

            # backtracking that set the value back to 0
            bo[row][col] = 0

    return False


print("Before solving the sudoku: ")
print_board()
print(" ")
solve(board)
print("After solving the sudoku: ")
print_board()
