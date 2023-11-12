class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == ".":
                    continue
                if (current in rows[r] or 
                   current in cols[c] or
                   current in square[(r//3,c//3)]):
                    return False
                rows[r].add(current)
                cols[c].add(current)
                square[(r//3,c//3)].add(current)
        return True
                
     
            