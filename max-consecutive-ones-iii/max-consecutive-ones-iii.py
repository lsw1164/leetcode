class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] is 0: k -= 1
            
            if k < 0:
                if nums[slow] is 0: k += 1
                slow += 1
        return fast - slow + 1
            
                
                
            
                