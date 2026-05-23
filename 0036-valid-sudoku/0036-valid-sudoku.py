class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        gridSet = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                gridNo = (i // 3) * 3 + (j // 3)

                if (board[i][j] != '.'):
                    isPresentInRow = board[i][j] in rowSet[i]
                    isPresentInCol = board[i][j] in colSet[j]
                    isPresentInGrid = board[i][j] in gridSet[gridNo]
                
                    if (isPresentInRow or isPresentInCol or isPresentInGrid):
                        return False

                    rowSet[i].add(board[i][j])
                    colSet[j].add(board[i][j])
                    gridSet[gridNo].add(board[i][j])
            
        return True
        