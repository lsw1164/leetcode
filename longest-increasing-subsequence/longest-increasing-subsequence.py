import bisect 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        st = []
        for num in nums:
            if len(st) == 0 or num > st[-1]:
                st.append(num)
                continue
            idx = bisect.bisect_left(st, num)
            st[idx] = num
        return len(st)