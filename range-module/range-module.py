import bisect

class RangeModule:

    def __init__(self):
        self.ranges = []
        

    def addRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.ranges, left)
        r = bisect.bisect_right(self.ranges, right)
        intervals = []
        if l % 2 == 0: intervals.append(left)
        if r % 2 == 0: intervals.append(right)
        self.ranges[l:r] = intervals

        
    def queryRange(self, left: int, right: int) -> bool:
        l = bisect.bisect_right(self.ranges, left)
        r = bisect.bisect_left(self.ranges, right)
        return l == r and l % 2 == 1
    

    def removeRange(self, left: int, right: int) -> None:
        l = bisect.bisect_left(self.ranges, left)
        r = bisect.bisect_right(self.ranges, right)
        intervals = []
        if l % 2 == 1: intervals.append(left)
        if r % 2 == 1: intervals.append(right)
        self.ranges[l:r] = intervals


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)