class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        self.res = 0
        row = len(grid)
        col = len(grid[0])
        visited = []

        def backtracking(x, y, total):
            
            visited.append((x,y))

            for d in directions:
                tempX = x+d[0]
                tempY = y+d[1]

                if 0 <= tempX < row and 0 <= tempY < col and grid[tempX][tempY] != 0 and not (tempX, tempY) in visited:
                    visited.append((tempX, tempY))
                    self.res = max(self.res, total + grid[tempX][tempY])
                    backtracking(tempX, tempY, total+grid[tempX][tempY])
                    visited.pop()
            
            self.res = max(self.res, total)
            visited.pop()

            return
        # each time choose greedily the best available option and mark it as visited, then unvisit it after

        # O(m*n * backtraking)
        for r in range(row):
            for c in range(col):
                if grid[r][c] != 0:
                    backtracking(r, c, grid[r][c])
        
        return self.res