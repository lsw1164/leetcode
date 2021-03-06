class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: continue
            if nums[i] > 0: break
                
            visit = set()
            for j in range(i+1, len(nums)):
                third = -(nums[i]+nums[j])
                if third in visit: 
                    triplet = tuple(sorted((nums[i], nums[j], third)))
                    triplets.add(triplet)
                visit.add(nums[j])
                
        return triplets