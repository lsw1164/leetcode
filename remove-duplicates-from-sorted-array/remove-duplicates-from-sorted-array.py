class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        INF = (1<<30)
        duplicate_cnt = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = INF
                duplicate_cnt += 1
        nums.sort()
        return len(nums) - duplicate_cnt
        
                
        