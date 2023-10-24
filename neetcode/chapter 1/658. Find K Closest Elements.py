class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr: # O(n)
            diff = abs(x-num)
            if len(heap) < k:
                heapq.heappush(heap, (-diff,-num)) # O
            else:
                heapq.heappushpop(heap, (-diff, -num))

        res = [-1*y for x,y in heap]
        res.sort()
    
        return res
    
    #############
    class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key= lambda y: abs(x-y)) #O(nlogn)
        res = arr[:k]
        res.sort() # O(nlogn)
        return res
        
        