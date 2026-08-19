class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0] * (cols + 1) for _ in range(rows+1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefixSum[r][c+1]
                self.prefixSum[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixSum[r2][c2]
        top = self.prefixSum[r1-1][c2]
        left = self.prefixSum[r2][c1-1]
        topLeft = self.prefixSum[r1-1][c1-1]

        return bottomRight - top - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)