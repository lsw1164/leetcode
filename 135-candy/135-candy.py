class Solution:
    
    def candy(self, ratings: List[int]) -> int:
        memo = [None] * len(ratings)
        
        def get_rating(idx):
            if idx < 0 or idx >= len(ratings): return 0 
            return ratings[idx]
            
        def get_candy_cnt(idx):
            if idx < 0 or idx >= len(ratings): return 0
            if memo[idx] != None: return memo[idx]
            
            l, r, cur = get_rating(idx - 1), get_rating(idx + 1), get_rating(idx)
            
            #print(f"idx: {idx},  l: {l},  cur: {cur},  r: {r}, memo: {memo}")
            
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
            #print(canty_cnt)
            
            
        #print(memo)
        return total_canty_cnt
            
        
