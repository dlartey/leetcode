class Solution:
    def missingNumber(self,array,n):
        # code here
        current = n
        for x in range(0,n-1):
            current=current^array[x]^(x+1)
        
        return current
