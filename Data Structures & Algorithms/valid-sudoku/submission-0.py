class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                boxIndex = (r // 3) * 3 + (c // 3)
                if (board[r][c] in rowSet[r]) or (board[r][c] in colSet[c]) or (board[r][c] in boxSet[boxIndex]):
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boxSet[boxIndex].add(board[r][c])
        return True
                
