class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 2: return k**n
        ways = [0] * (n+1)
        ways[1], ways[2] = k, k*k
        
        for i in range(3, n+1):
            ways[i] = (k-1) * (ways[i-1] + ways[i-2])
            
        return ways[n]