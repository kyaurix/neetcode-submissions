class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dupe = set()
            for value in row:
                if value == ".":
                    continue
                elif value in dupe:
                    return False
                else:
                    dupe.add(value)
        for column in range(9):
            dupe = set()
            for row in range(9):
                if board[row][column] == ".":
                    continue
                elif board[row][column] in dupe:
                    return False
                else:
                    dupe.add(board[row][column])
        for boxRow in [0, 3, 6]:
            for boxCol in [0, 3, 6]:
                dupe = set()
                for row in range(boxRow, boxRow + 3):
                    for col in range(boxCol, boxCol + 3):
                        if board[row][col] == ".":
                            continue
                        elif board[row][col] in dupe:
                            return False
                        else:
                            dupe.add(board[row][col])
        return True