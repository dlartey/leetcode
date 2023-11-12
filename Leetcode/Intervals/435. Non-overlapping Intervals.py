class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        temp = []
        # Uses Timsort best case O(n)
        intervals.sort(key = lambda x: (x[1])) # O(nlogn)

        for x in intervals: # O(n)
            if not temp:
                temp.append(x) # O(1)
                continue
            
            if temp[-1][1] > x[0]: # O(1)
                res+=1 # O(1)
            else:
                temp.append(x) # O(1)
        
        return res
        # Time complexity = O(nlogn)
        