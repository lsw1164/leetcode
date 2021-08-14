class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_map: return ""
        i = self.uppder_bound(self.time_map[key], timestamp)
        return self.time_map[key][i-1][1] if i > 0 else ""

    def uppder_bound(self, entries, target):
        l, r = 0, len(entries)
        while l < r:
            mid = (l+r)>>1
            t, _ = entries[mid]
            if t <= target:
                l = mid + 1
            else:
                r = mid
        return l
                
            
            
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)