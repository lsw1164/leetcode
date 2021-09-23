from copy import deepcopy 

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        comb = []
        combinations = []
        
        def update_combinations(pivot):
            if k == len(comb):
                combinations.append(deepcopy(comb))
                return
            
            for i in range(pivot, n): 
                if len(comb) > 0 and comb[-1] >= nums[i]: 
                    continue
                comb.append(nums[i])
                update_combinations(i+1)
                comb.pop()
                
        update_combinations(0) 
        
        return combinations