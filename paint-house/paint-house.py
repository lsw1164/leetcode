class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 1: return min(costs[0])
        
        dp = [[0 for __ in range(3)] for _ in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(dp)):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i-1][j-1], dp[i-1][j-2])
        return min(dp[i])