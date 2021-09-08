class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set, num2_set = set(nums1), set(nums2)
        return [num for num in num2_set if num in num1_set]
            
        
        