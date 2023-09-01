class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        lp = 2
        mid = 0
        rp = x//2
        
        while (lp<=rp):            
            mid = lp + (rp-lp)//2
            
            if (mid*mid > x):
                rp=mid-1
            elif (mid*mid < x):
                lp=mid+1
            else:
                return mid
        
        return rp