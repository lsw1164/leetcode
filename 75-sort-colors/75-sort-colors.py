class Solution:
    def sortColors(self, nums: List[int]) -> None:
        CNT_MEMO_LEN = 3
        cnt_memo = [0]*CNT_MEMO_LEN
        for num in nums:
            cnt_memo[num] += 1
        
        cnt_idx = 0
        for i in range(len(nums)):
            while cnt_idx < CNT_MEMO_LEN and cnt_memo[cnt_idx] == 0:
                cnt_idx += 1
            nums[i] = cnt_idx
            cnt_memo[cnt_idx] -= 1