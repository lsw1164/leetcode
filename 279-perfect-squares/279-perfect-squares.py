class Solution:
    
    
    def numSquares(self, n: int) -> int:
        memo = [0] + [float('inf')] * n
        
        for i in range(1, n+1):
            min_num_squares = float('inf')
            for j in range(1, int(i**0.5) + 1):
                square = j*j
                memo[i] = min(memo[i], memo[i - square] + 1)
                
        return memo[n]
