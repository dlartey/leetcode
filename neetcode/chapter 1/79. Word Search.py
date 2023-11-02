class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        self.res = False
        visited = []

        def backtrack(x, y, rem):
            if rem == "":
                self.res = True
                return
            
            visited.append((x,y))

            for d in directions:
                tempX = x + d[0]
                tempY = y + d[1]

                if 0 <= tempX < row and 0 <= tempY < col and (tempX,tempY) not in visited and board[tempX][tempY] == rem[0]:
                    if len(rem) > 1:
                        backtrack(tempX, tempY, rem[1:])
                    else:
                        backtrack(tempX, tempY, "")

            visited.pop()
            return

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    backtrack(r, c, word[1:])
        
        return self.res