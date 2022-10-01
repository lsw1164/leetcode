class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])
        
        remove_cnt = 0
        prev_end = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            cur_start = sorted_intervals[i][0]
            if prev_end > cur_start:
                remove_cnt += 1
            else:    
                prev_end = sorted_intervals[i][1]
                
        return remove_cnt
    