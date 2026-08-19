class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    self.prefix[r][c] = matrix[r][c]
                elif r == 0:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r][c - 1]
                elif c == 0:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r-1][c]
                else:
                    self.prefix[r][c] = matrix[r][c] + self.prefix[r - 1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        else:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2] - self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)