class Solution:
    def sortColors(self, nums: List[int]) -> None:
        CNT_MEMO_LEN = 3
        cnt_memo = [0]*CNT_MEMO_LEN
        for num in nums:
            cnt_memo[num] += 1
        
        color = 0
        for i in range(len(nums)):
            while color < CNT_MEMO_LEN and cnt_memo[color] == 0:
                color += 1
            nums[i] = color
            cnt_memo[color] -= 1