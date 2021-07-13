class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        def get_prev(idx):
            return nums[idx-1] if idx-1 >= 0 else float('-inf')
        
        def get_next(idx):
            return nums[idx+1] if idx+1 < len(nums) else float('-inf')
        
        while left < right:
            mid = (left+right)>>1
            if nums[mid] < get_next(mid):
                left = mid + 1
            else:
                right = mid
        return right
        