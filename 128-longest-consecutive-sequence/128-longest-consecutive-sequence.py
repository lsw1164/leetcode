class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        hash_map = {}
        for num in nums:
            hash_map[num] = 0
            
        longest = 0
        for num in nums:
            if hash_map[num] != 0: continue
            
            cnt = 1
            cur = num-1
            
            while cur in hash_map:
                
                consecutive = hash_map[cur]
                if consecutive != 0:
                    cnt += consecutive
                    break
                    
                cnt += 1
                cur -= 1
                
            hash_map[num] = cnt
            longest = max(longest, cnt)
            
        return longest