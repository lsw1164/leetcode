class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            prev_end, start = intervals[i-1][1], intervals[i][0]
            if prev_end > start: return False
        return True