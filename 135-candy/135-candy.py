class Solution:
    
    def candy(self, ratings: List[int]) -> int:
        memo = [None] * len(ratings)
            
        def get_candy_cnt(idx):
            if idx < 0 or idx >= len(ratings): return 0
            if memo[idx] != None: return memo[idx]
            
            l = ratings[idx - 1] if idx > 0 else 0
            r = ratings[idx + 1] if idx < len(ratings) - 1 else 0
            cur = ratings[idx]
            
            if cur <= l and cur <= r:
                memo[idx] = 1
                return 1
            
            candy_cnt = 1
            
            if cur > l:
                l_candy_cnt = get_candy_cnt(idx - 1)
                candy_cnt = max(candy_cnt, l_candy_cnt + 1)
            
            if cur > r:
                r_candy_cnt = get_candy_cnt(idx + 1)
                candy_cnt = max(candy_cnt, r_candy_cnt + 1)
                
            memo[idx] = candy_cnt 
            return memo[idx]
        
        
        total_canty_cnt = 0
        for i in range(len(ratings)):
            canty_cnt = get_candy_cnt(i)
            total_canty_cnt += canty_cnt
            
            
        return total_canty_cnt
            
        
