import heapq

class Solution:
    
    def peek(self, pq):
        peek = heapq.heappop(pq)
        heapq.heappush(pq, peek)
        return peek
    
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        
        for [start, end] in intervals:
            if len(pq) > 0 and self.peek(pq) <= start:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
            
        return len(pq)