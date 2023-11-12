class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for x in nums: # O(n)
            heapq.heappush(self.heap,x) # O(logn)
            if len(self.heap) > k: # O(1)
                heapq.heappop(self.heap) # O(logn)
        # O(nlogn)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val) # O(logn)
        
        if len(self.heap) > self.k: # O(1)
            heapq.heappop(self.heap) # O(logn)

        return self.heap[0] # O(1)
        # O(logn)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)