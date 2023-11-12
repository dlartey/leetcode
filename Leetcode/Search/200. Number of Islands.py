class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for i in range(colLen)] for x in range(rowLen)]
        
        def dfs(x,y):

            for d in directions:
                tempX = x+d[0]
                tempY = y+d[1]
                # checking if in bounds
                if 0 <= tempX < rowLen and 0 <= tempY < colLen and grid[tempX][tempY] == "1" and not visited[tempX][tempY]:
                    visited[tempX][tempY] = True
                    dfs(tempX,tempY)
            return

        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == '1' and not visited[r][c]:
                    res+=1
                    visited[r][c] = True
                    dfs(r,c)
        
        return res


        