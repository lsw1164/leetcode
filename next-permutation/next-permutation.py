class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums) - 2
        while l >= 0 and nums[l+1] <= nums[l]:
            l -= 1
            
        if l >= 0:
            r = len(nums) - 1
            while nums[r] <= nums[l]:
                r -= 1
            nums[r], nums[l] = nums[l], nums[r]
        self.reverse(nums, l + 1)   
        
    def reverse(self, nums, start):
        l, r = start, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1
        