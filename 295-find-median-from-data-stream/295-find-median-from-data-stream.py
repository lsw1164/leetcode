import heapq

class MedianFinder:

    def __init__(self):
        self.smalls = []
        self.bigs = []
        
    def addNum(self, num: int) -> None:
        if self.get_size() < 2:
            heapq.heappush(self.smalls, (-num, num))
            self.update()
            return
        
        min_of_bigs = self.peek(self.bigs)
        if num > min_of_bigs:
            heapq.heappush(self.bigs, (num, num))
        else:
            heapq.heappush(self.smalls, (-num, num))
        self.update()
        
    def get_size(self):
        return len(self.smalls) + len(self.bigs)
        
    def peek(self, heap):
        key, val = heapq.heappop(heap)
        heapq.heappush(heap, (key, val))
        return val
    
    def update(self):
        if len(self.smalls) == len(self.bigs): return
        if len(self.smalls) == len(self.bigs)+1: return
        
        if len(self.smalls) < len(self.bigs)+1:
            _, val = heapq.heappop(self.bigs)
            heapq.heappush(self.smalls, (-val, val))
        else:
            _, val = heapq.heappop(self.smalls)
            heapq.heappush(self.bigs, (val, val))
        
    def findMedian(self) -> float:
        if self.get_size() % 2 == 0:
            max_of_smalls = self.peek(self.smalls)
            min_of_bigs = self.peek(self.bigs)
            return (max_of_smalls + min_of_bigs) * 0.5
        
        max_of_smalls = self.peek(self.smalls)
        return max_of_smalls    
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()