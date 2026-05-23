class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rowSet(9);
        vector<unordered_set<char>> colSet(9);
        vector<unordered_set<char>> gridSet(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int gridNo = (i / 3) * 3 + (j / 3);

                if (board[i][j] != '.') {
                    bool isPresentInRow = rowSet[i].count(board[i][j]);
                    bool isPresentInCol = colSet[j].count(board[i][j]);
                    bool isPresentInGrid = gridSet[gridNo].count(board[i][j]);

                    if (isPresentInRow || isPresentInCol || isPresentInGrid) {
                        return false;
                    }

                    rowSet[i].insert(board[i][j]);
                    colSet[j].insert(board[i][j]);
                    gridSet[gridNo].insert(board[i][j]);
                }
            }
        }

        return true;
    }
};