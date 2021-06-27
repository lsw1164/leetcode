class UndergroundSystem:

    def __init__(self):
        self.info_by_id = {}
        self.avg_by_name = {}
        
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.info_by_id[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_name, in_t = self.info_by_id[id]
        if in_name not in self.avg_by_name:
            self.avg_by_name[in_name] = {}
            
        if stationName not in self.avg_by_name[in_name]:
            self.avg_by_name[in_name][stationName] = (0, 0)
        
        total, cnt = self.avg_by_name[in_name][stationName]
        total += t - in_t
        cnt += 1
        self.avg_by_name[in_name][stationName] = (total, cnt)

        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.avg_by_name[startStation][endStation]
        return total / cnt

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)