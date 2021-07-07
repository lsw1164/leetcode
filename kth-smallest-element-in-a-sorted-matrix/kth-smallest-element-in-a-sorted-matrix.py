class Solution:
    def count_less_equal(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        r, c = n-1, 0
        while r >= 0 and c < n:
            if matrix[r][c] > mid:
                larger = min(larger, matrix[r][c])
                r -= 1
                continue
            smaller = max(smaller, matrix[r][c])
            count += r+1
            c += 1
        return count, smaller, larger
            
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1] 
        while left < right:
            mid = left + (right-left)*0.5 # hypothetical mid
            smaller, larger = matrix[0][0], matrix[n-1][n-1]
            count, smaller, larger = self.count_less_equal(matrix, mid, smaller, larger)
            
            if count == k: 
                return smaller
            if count < k: 
                left = larger
            else:
                right = smaller
        return left
    