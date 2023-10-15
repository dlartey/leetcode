class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use dfs to iterate and calculate the max area
        row = len(grid)
        col = len(grid[0])
        visited = [[False for x in range(col)] for y in range(row)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.maxi = 0

        def dfs(x, y, count):

            visited[x][y] = True

            for dir in directions:
                tempX = dir[0] + x
                tempY = dir[1] + y

                if 0 <= tempX < row and 0 <= tempY < col and not visited[tempX][tempY] and grid[tempX][tempY] == 1:
                    count+= dfs(tempX, tempY, 1)
            
            return count

        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    res = dfs(r, c, 1)
                    self.maxi = max(self.maxi,res)

        return self.maxi
        