class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        return [num for num in set(nums2) if num in num1_set]
            
        
        