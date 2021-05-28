from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0: return False
        counter = Counter(nums)
        nums.sort()
        
        for num in nums:
            if not num in counter: continue
            for next_num in range(num, num + k):
                if not next_num in counter: return False
                counter[next_num] -= 1
                if counter[next_num] == 0:
                    counter.pop(next_num)
        return True
            
                
            
            
                
        
        
        