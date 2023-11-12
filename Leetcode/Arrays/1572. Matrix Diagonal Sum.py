class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        total = 0
        if length % 2 == 1:
            total -= mat[length//2][length//2]

        r, c  =0, 0

        while r < length:
            total+=mat[r][c]
            r+=1
            c+=1
        
        r = 0 
        c = length-1
        while r < length:
            total+=mat[r][c]
            r+=1
            c-=1

        return total
        