def is_valid_sudoku(board):

    for row in range(9):
        seen = set()
        for value in board[row]:
            if value == ".":
                continue
            if value in seen:
                return False

            seen.add(value)

    for col in range(9):

        seen = set()
        for r in range(9):
            value = board[r][col]
            if value == ".":
                continue
            if value in seen:
                return False
            seen.add(value)
    for corner_r in [0, 3, 6]:
        for corner_c in [0, 3, 6]:
            seen = set()
            for r in range(corner_r, corner_r + 3):
                for c in range(corner_c, corner_c + 3):
                    value = board[r][c]
                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(value)
    return True




print(is_valid_sudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))


print(is_valid_sudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))


# Time: O(1) | Space: O(1)

# approach
# check every row for duplicate numbers using a set
# check every column for duplicate numbers using a set
# check every 3x3 box for duplicate numbers using a set
# ignore "." because it represents an empty cell
# if any number is already seen in the same row, column, or box return False
# if no duplicates are found return True
