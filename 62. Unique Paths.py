class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]
        memo = {}

        def dfs(x, y):
            if (x,y) in memo:
                return memo[(x,y)]
                
            if x == m-1 and y == n-1:
                return 1
            
            count = 0
            
            for d in directions:
                tempX = d[0]+x
                tempY = y+d[1]

                if 0 <= tempX < m and 0 <= tempY < n:
                    count+= dfs(tempX, tempY)
            
            memo[(x,y)] = count
            return count
        
        return dfs(0,0)
        