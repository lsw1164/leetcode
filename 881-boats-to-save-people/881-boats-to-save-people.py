class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) <= 1: 
            return len(people)
        
        people.sort()
        l, r = 0, len(people) - 1
        boat_cnt = 0
        
        while l <= r:
            boat_cnt += 1
            
            if l == r: 
                break
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
                
        return boat_cnt