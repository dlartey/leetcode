class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res = 0
        times = []
        n = len(dist)

        # gets the times to reach the goal
        for x in range(n):
            temp = dist[x]
            times.append((temp/speed[x],dist[x]))

        current = 0
        heapq.heapify(times)

        while times:
            temp = heapq.heappop(times)
            if current < temp[0]:
                res+=1
                current+=1
            else:
                break

        return res
        