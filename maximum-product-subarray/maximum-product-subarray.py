class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_val = max_val = nums[0]
        prev_min = prev_max = nums[0]
        
        for i in range(1, len(nums)):
            cur_min = min(prev_min * nums[i], prev_max * nums[i], nums[i])
            cur_max = max(prev_min * nums[i], prev_max * nums[i], nums[i])
            max_product = max(max_product, cur_max)
            prev_min, prev_max = cur_min, cur_max
        return max_product
            
        
            
            
            