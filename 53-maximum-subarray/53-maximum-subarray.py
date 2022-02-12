class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_contiguous = -float('inf')
        contiguous = -float('inf')
        for num in nums:
            contiguous = max(contiguous + num, num)
            max_contiguous = max(max_contiguous, contiguous)
        return max_contiguous
        