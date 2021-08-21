class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1) 
        
        N = len(nums1) + len(nums2)
        left, right = 0, len(nums1)
        INF = float('inf')
        
        while left <= right:
            mid1 = (left + right) >> 1
            mid2 = (N + 1) // 2 - mid1
            l_max1 = nums1[mid1-1] if mid1 > 0 else -INF
            r_min1 = nums1[mid1] if mid1 < len(nums1) else INF
            l_max2 = nums2[mid2-1] if mid2 > 0 else -INF
            r_min2 = nums2[mid2] if mid2 < len(nums2) else INF
            if l_max1 <= r_min2 and l_max2 <= r_min1:
                l_max = max(l_max1, l_max2)
                r_min = min(r_min1, r_min2)
                return (l_max + r_min) * 0.5 if N % 2 == 0 else l_max
            elif l_max1 > r_min2:
                right = mid1 - 1
            else:
                left = mid1 + 1
                
        return 0