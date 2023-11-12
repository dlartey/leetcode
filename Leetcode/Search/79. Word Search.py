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
        # For this problem, I attempted to use backtracking if the index of the word we are searching for matches the current row & column for the grid
        
        # Then, I check that the tempX & tempY variable I create by exploring the 4-direction is inbound, that the next index of the word matches and we haven't already visited.
        
        # If these conditions are matched, then we recursively call the backtrack function and return True if we can find the word in the board
        
        # Time complexity: O(N * 3^L)
        return self.res