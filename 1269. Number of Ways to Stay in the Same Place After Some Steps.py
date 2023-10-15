class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        directions = [-1,0,1]
        MOD = 10**9 + 7
        memo = {}

        # use DFS to compute all the possible movements
        def dfs(pos, rem):
            
            # if we've seen this combination before, then just return
            if (pos,rem) in memo:
                return memo[(pos,rem)]

            # no remaining moves
            if (rem == 0):
                return 1 if pos == 0 else 0

            # we can't get back to the start position from here
            if pos > rem:
                return 0
            
            count = 0

            for d in directions:
                temp = pos+d
                if 0 <= temp < arrLen:
                    count += dfs(temp, rem-1)

            memo[(pos,rem)] = count

            return count
        
        return dfs(0, steps) % MOD
        