class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res
        