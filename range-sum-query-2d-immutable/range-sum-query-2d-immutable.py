class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)
        C = len(matrix[0])
        
        self.h_cumul = [[0 for _ in range(C)] for __ in range(R)]
        self.v_cumul = [[0 for _ in range(C)] for __ in range(R)]
        
        for r in range(R):
            cumul = 0
            for c in range(C):
                cumul += matrix[r][c]
                self.h_cumul[r][c] = cumul
                
        for c in range(C):
            cumul = 0
            for r in range(R):
                cumul += matrix[r][c]
                self.v_cumul[r][c] = cumul

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dr, dc = row2 - row1, col2 - col1
        sum_region = 0
        if dr > dc:
            for c in range(col1, col2+1):
                sum_region += self.v_cumul[row2][c]
                if row1 > 0: sum_region -= self.v_cumul[row1-1][c]
        else:
            for r in range(row1, row2+1):
                sum_region += self.h_cumul[r][col2]
                if col1 > 0: sum_region -= self.h_cumul[r][col1-1]
                    
        return sum_region
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)