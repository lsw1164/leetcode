class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)
        C = len(matrix[0])
        cache = [[0 for _ in range(C)] for __ in range(R)]
        cache[0][0] = matrix[0][0]
        for r in range(1, R):
            cache[r][0] = cache[r-1][0] + matrix[r][0]
        for c in range(1, C):
            cache[0][c] = cache[0][c-1] + matrix[0][c]
        for r in range(1, R):
            for c in range(1, C):
                cache[r][c] = matrix[r][c] + cache[r][c-1] + cache[r-1][c] - cache[r-1][c-1]
        self.cache = cache

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region = self.cache[row2][col2]
        if col1 > 0: region -= self.cache[row2][col1-1]
        if row1 > 0: region -= self.cache[row1-1][col2]
        if col1 > 0 and row1 > 0: region += self.cache[row1-1][col1-1]
        return region
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)