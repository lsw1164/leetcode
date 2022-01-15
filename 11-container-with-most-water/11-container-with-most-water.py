class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        def get_area(l, r):
            return min(height[l], height[r]) * (r - l)
            
        while left < right:
            cur_area = get_area(left, right)
            max_area = max(max_area, cur_area)
            if height[left] < height[right]: left += 1 
            else: right -= 1
                
        return max_area
    