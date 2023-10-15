class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # initialise the min distance we've seen so far at each step to infinity
        dp = [math.inf]*(n+1)
        # set min distance for 1st and 2nd step to 0 (since we can reach these and can't get smaller value)
        dp[0], dp[1] = cost[0], cost[1]

        # iterate from 2 to n+1, since we can be at pos before last and jump 2 steps
        for x in range(2,n+1):
            # get the current cost, else 0 if we are out of bounds
            current = cost[x] if x < n else 0

            # calculate the minimum at position x using pre-computed values
            dp[x] = min(dp[x-1] + current, dp[x-2] + current)

        return min(dp[n],dp[n-1])
        