class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ocean_views = []
        
        max_h = -float('inf')
        for i in reversed(range(len(heights))):
            h = heights[i]
            if h > max_h:
                ocean_views.append(i)
            max_h = max(max_h, h)
            
        return reversed(ocean_views)