class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        col = len(matrix)
        lp = 0
        rp = (row*col)-1
        
        while (lp <= rp):
            mid = lp + (rp-lp)//2
            tempRow = mid//row
            tempCol = mid%row
            
            tempVal = matrix[tempRow][tempCol]
            
            if (tempVal == target):
                return True
            elif (tempVal > target):
                rp = mid-1
            else:
                lp = mid+1
        return False
        