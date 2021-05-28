from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counter = Counter(nums)
        nums.sort()
        
        for num in nums:
            if not num in counter or counter[num] == 0: continue
            for i in range(k):
                next_num = num + i
                if not next_num in counter or counter[next_num] == 0: return False
                counter[next_num] -= 1
        return True
            
                
            
            
                
        
        
        