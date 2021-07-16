class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i;
        
        output = []
        for i in range(len(nums)):
            key = target - nums[i];
            if not key in hash_map: 
                continue
            j = hash_map[key]
            if i != j: return [i, j]
                