class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        hash_map = {}
        for num in nums:
            hash_map[num] = None
            
        longest = 0
        while len(nums) > 0:
            top = nums.pop()
            if hash_map[top] != None: continue
            
            cnt = 1
            cur = top-1
            while cur in hash_map:
                if hash_map[cur] != None:
                    cnt += hash_map[cur]
                    break
                cnt += 1
                cur -= 1
            hash_map[top] = cnt
            longest = max(longest, cnt)
        return longest