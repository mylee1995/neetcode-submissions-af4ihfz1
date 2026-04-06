class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.validateRows(board) == False:
            return False
        if self.validateCols(board) == False:
            return False
        for i in range (1, 9, 3):
            for j in range (1, 9, 3):
                validBox = self.validateBox(board, i, j)
                print(i, j, validBox)
                if validBox == False:
                    return False
        return True
            

    def validateRows(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 1):
            rowMap = {}
            for j in range(0, 9, 1):
                cell = board[i][j]
                if cell == ".": 
                    continue
                elif rowMap.get(cell, False):
                    return False
                else:
                    rowMap[cell] = True
        return True

    def validateCols(self, board: List[List[str]]) -> bool:
        for i in range (0, 9, 1):
            colMap = {}
            for j in range(0, 9, 1):
                cell = board[j][i]
                if cell == ".": 
                    continue
                elif colMap.get(cell, False):
                    return False
                else:
                    colMap[cell] = True
        return True
        
    def validateBox(self, board: List[List[str]], x: int, y: int) -> bool:
        # create box from given x and y coordinate and validate if given box is valid sudoku
        boxMap = {}
        for i in range (x-1, x+2, 1):
            for j in range (y-1, y+2, 1):
                cell = board[i][j]
                if cell == ".":
                    continue
                elif boxMap.get(cell, False):
                    return False
                else:
                    boxMap[cell] = True
        return True