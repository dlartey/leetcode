class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap,n)
        temp = heap
        return heapq.nlargest(k,heap)[-1]
        