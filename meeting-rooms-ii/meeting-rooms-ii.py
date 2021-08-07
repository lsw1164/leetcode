import heapq

class Solution:
    
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        
        def peek():
            peek = heapq.heappop(pq)
            heapq.heappush(pq, peek)
            return peek
        
        for [start, end] in intervals:
            if len(pq) > 0 and peek() <= start:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
            
        return len(pq)