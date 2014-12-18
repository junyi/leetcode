# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled
# with the character '.'.


# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable.
# Only the filled cells need to be validated.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

    def isValidSudoku(self, board):
        entries = dict()
        entries['row'] = list(range(9))
        entries['col'] = list(range(9))
        entries['grid'] = list(range(9))
        all_types = entries.keys()

        for i in range(9):
            for j in range(9):
                if board[i][j] is not '.':
                    # print 'rowcol', i, j
                    for typ in all_types:
                        index = self.getIndex(typ, i, j)
                        if index in entries[typ]:
                            inpt = self.getInput(typ, index, board)
                            if self.check(inpt, board):
                                entries[typ].remove(index)
                            else:
                                return False

        return True

    def getInput(self, typ, index, board):
        if typ == 'row':
            res = board[index]
        elif typ == 'col':
            res = [board[row][index] for row in range(9)]
        else:
            start_row, start_col = self.getRowCol(index)
            res = []
            for i in range(9):
                offset_row = i / 3
                offset_col = i % 3
                num = board[start_row + offset_row][start_col + offset_col]
                res.append(num)

        return [int(i) for i in res if i != '.']

    def check(self, inpt, board):
        numbers = list(range(1, 10))
        for i in inpt:
            if i != '.' and i in numbers:
                numbers.remove(i)
            else:
                return False
        return True

    def getRowCol(self, index):
        return (index / 3) * 3, (index % 3) * 3

    def getIndex(self, typ, row, col):
        row = int(row)
        col = int(col)
        if typ == 'row':
            return row
        elif typ == 'col':
            return col
        else:
            return (row / 3) * 3 + col / 3
sudoku = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']

]
sol = Solution()
print sol.isValidSudoku(sudoku)
