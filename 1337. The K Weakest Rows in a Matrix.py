class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for x in range(len(mat)):
            total = sum(mat[x][::])
            heapq.heappush(heap,(total,x))
        
        ans = heapq.nsmallest(k,heap)
        return [a[1] for a in ans]
        