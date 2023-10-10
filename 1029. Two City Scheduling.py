class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        costs.sort(key = lambda i:i[0]-i[1])
        res = 0
        for x in range(n):
            res+= costs[x][0] + costs[x+n][1]
        
        return res


