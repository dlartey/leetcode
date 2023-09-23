class UndergroundSystem:

    def __init__(self):
        self.journey = collections.defaultdict()
        self.average = collections.defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.journey[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # check if the id is in the map
        source, startTime = self.journey[id]
        del self.journey[id]
        self.average[(source,stationName)].append(t-startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.average[(startStation,endStation)]
        return sum(times)/len(times)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)