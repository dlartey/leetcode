class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []

        # O(n)
        for n in arr:
            count = 0
            number = n
            while number: # O(32) = O(1)
                count += number & 1
                number = number >> 1
            res.append((count,n))
        
        res.sort(key=lambda x: (x[0],x[1])) # O(nlogn)
        return [x[1] for x in res]