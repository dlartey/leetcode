class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cm = 1
        self.taken = set()

    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap) # O(logn)
            self.taken.add(res) # O(1)
            return res
        else:
            current = self.cm
            self.cm+=1 
            self.taken.add(current) # O(1)
            return current # O(1)
        

    def addBack(self, num: int) -> None:
        if num in self.taken: # O(1)
            heapq.heappush(self.heap,num) # O(logn)
            self.taken.remove(num) # O(1)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)