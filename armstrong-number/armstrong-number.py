class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(f"{n}")
        cur = n
        while cur > 0:
            d = cur % 10
            cur //= 10
            n -= d**k
        return n is 0