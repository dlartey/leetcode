class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        prev = prices[0]
        n = len(prices)

        for x in range(1,n):
            if prices[x] - prev > 0:
                res += prices[x] - prev
            
            prev = prices[x]
            
        return res
            
        