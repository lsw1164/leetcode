class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while st[-1] != -1 and heights[st[-1]] >= heights[i]:
                cur_h = heights[st.pop()]
                cur_w = i - st[-1] - 1
                max_area = max(max_area, cur_h * cur_w)
            st.append(i)
        
        while st[-1] != -1:
            cur_h = heights[st.pop()]
            cur_w = len(heights) - st[-1] - 1
            max_area = max(max_area, cur_h * cur_w)
            
        return max_area
        