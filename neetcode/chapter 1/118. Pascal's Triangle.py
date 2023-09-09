class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        currRow = 1
        
        while (currRow < numRows):
            prevRow = rows[-1]
            newRow = [1]
            for x in range(len(prevRow)-1):
                newRow.append(prevRow[x]+prevRow[x+1])
            newRow.append(1)
            rows.append(newRow)
            currRow+=1
            
        return rows
            
        
        