class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            # if the end is greater than the start, then update with the maximum
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res
        