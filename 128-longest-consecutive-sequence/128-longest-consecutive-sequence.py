class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        hash_set = set(nums)
            
        longest = 1
        for num in nums:
            if num - 1 in hash_set: continue
            
            consecutive = 1
            while num + 1 in hash_set:
                num += 1
                consecutive += 1
                
            longest = max(longest, consecutive)
            
        return longest