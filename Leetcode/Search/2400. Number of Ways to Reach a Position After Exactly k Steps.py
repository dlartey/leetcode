class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        directions = [-1,1]

        def dfs(pos,rem):
            if (pos,rem) in memo:
                return memo[(pos,rem)]
            
            if rem == 0:
                return 1 if pos == endPos else 0
            
            # check if it's feasible to reach end from here
            if (pos + rem < endPos or pos - rem > endPos):
                return 0
            
            count = 0
            
            for d in directions:
                temp = pos+d
                count+= dfs(temp, rem-1)
            
            memo[(pos,rem)] = count
            return count
        
        return dfs(startPos,k) % MOD

        