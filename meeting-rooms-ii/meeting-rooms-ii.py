import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        pq = []
        for [start, end] in intervals:
            if len(pq) == 0:
                heapq.heappush(pq, end)
                continue
            available_time = heapq.heappop(pq)
            heapq.heappush(pq, available_time)
            
            if available_time <= start:
                heapq.heappop(pq)
                
            heapq.heappush(pq, end)
            
        return len(pq)