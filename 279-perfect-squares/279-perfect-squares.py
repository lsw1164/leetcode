class Solution:
    
    
    def numSquares(self, n: int) -> int:
        MAX_NUM = 10001
        memo = [None] * MAX_NUM
        memo[0] = 0
        cur = 1
        while cur*cur <= MAX_NUM:
            memo[cur*cur] = 1
            cur += 1
        
        def get_num_squares(num):
            if memo[num] != None: 
                return memo[num]
            
            min_num_squares = float('inf')
            cur = 1
            while cur*cur <= num:
                diff = num - cur * cur
                cur_num_squares = get_num_squares(diff) + 1
                min_num_squares = min(min_num_squares, cur_num_squares)
                cur += 1
            memo[num] = min_num_squares
            return min_num_squares
        
        return get_num_squares(n)
        