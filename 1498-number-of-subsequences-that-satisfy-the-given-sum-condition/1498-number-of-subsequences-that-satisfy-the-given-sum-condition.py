class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        nums.sort()
        
        for min_idx, n in enumerate(nums):
            if 2 * n > target: break
            max_idx = bisect.bisect(nums, target - n, lo=min_idx)
            ans += pow(2, max_idx - min_idx - 1, MOD)
            
        return ans % MOD