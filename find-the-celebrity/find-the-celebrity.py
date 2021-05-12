# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
        
    def findCelebrity(self, n: int) -> int:
        
        knows_cache = [[None for _ in range(n)] for __ in range(n)]
        def get_know(a, b):
            if knows_cache[a][b] != None: return knows_cache[a][b]
            knows_cache[a][b] = knows(a, b)
            return knows_cache[a][b]
        
        can_be_celebrity = [True] * n
        
        for i in range(n):
            if not can_be_celebrity[i]: continue
            for j in range(i+1, n):
                i2j, j2i = get_know(i, j), get_know(j, i)
                if i2j == j2i:
                    can_be_celebrity[i] = can_be_celebrity[j] = False
                    break
                if i2j:
                    can_be_celebrity[i] = False
                    break
                else:
                    can_be_celebrity[j] = False
                    
        if not True in can_be_celebrity: return -1
        celebrity = can_be_celebrity.index(True)
        
        for i in range(n):
            if i == celebrity: continue
            if get_know(celebrity, i): return -1
            if not get_know(i, celebrity): return -1
            
        return celebrity
            