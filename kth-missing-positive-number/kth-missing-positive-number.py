class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        num = 0
        while k > 0:
            num += 1
            if num in s: continue
            k -= 1
        return num
        