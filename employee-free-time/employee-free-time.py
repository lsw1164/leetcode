"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    
    def merge_intervals(self, intervals):
        merged = []
        for start, end in sorted(intervals):
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
                continue
            merged[-1][1] = max(merged[-1][1], end)
        return merged
        
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        work_intervals = []
        for intervals in schedule:
            for i in intervals:
                work_intervals.append([i.start, i.end])
                
        merged_intervals = self.merge_intervals(work_intervals)       
        
        freetimes = []
        for i in range(1, len(merged_intervals)):
            prev_end, cur_start = merged_intervals[i-1][1], merged_intervals[i][0]
            freetimes.append(Interval(prev_end, cur_start))
        
        return freetimes   
        