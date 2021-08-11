from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.que = deque()

    def next(self, val: int) -> float:
        self.que.append(val)
        self.sum += val
        
        if len(self.que) > self.size:
            self.sum -= self.que.popleft()
        
        return self.sum / len(self.que)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)