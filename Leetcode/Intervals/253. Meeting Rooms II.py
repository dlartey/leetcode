class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        heap = []
        intervals.sort()
        for i in intervals:
            if not heap:
                heapq.heappush(heap,(i[1]))
                res+=1
                continue
            
            if i[0] >= heap[0]:
                temp = heapq.heappop(heap)
                heapq.heappush(heap,i[1])
            else:
                heapq.heappush(heap,i[1])
                res+=1

        return res
        