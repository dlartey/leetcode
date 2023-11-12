class TimeMap:

    def __init__(self):
        self.map1 = {} # stores a key -> [(timestamp,val),(ts2,val2)] pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map1:
            self.map1[key].append((timestamp,value))
        else:
            self.map1[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map1:
            return ""
        
        res = ""
        candidates = self.map1[key]
        lp, rp = 0, len(candidates)-1
        while (lp <= rp):
            mid = lp + (rp-lp)//2
            
            if (candidates[mid][0] <= timestamp):
                res = candidates[mid][1]
                lp = mid+1
            else:
                rp = mid-1

        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)