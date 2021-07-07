class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COL = len(matrix), len(matrix[0])
        
        def idx_2_pt(idx):
            return [idx // COL, idx % COL]
        
        left, right = 0, ROW*COL-1
        
        while left <= right:
            mid = (left+right) >> 1
            r, c = idx_2_pt(mid)
            if target == matrix[r][c]:
                return True
            if matrix[r][c] < target:
                left = mid + 1
                continue
            right = mid - 1
        return False
            
            