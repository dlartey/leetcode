class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        if len(stones) == 1:
            return stones[0]

        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) > 1:
            f,s = abs(heapq.heappop(heap)), abs(heapq.heappop(heap))

            if (f != s):
                heapq.heappush(heap,-1*abs(f-s))
        
        return -1*heap[0] if heap else 0

        