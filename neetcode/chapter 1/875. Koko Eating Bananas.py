class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def satisfyMin(speed):
            count = 0
            for number in piles:
                if (number <= speed):
                    count+=1
                else:
                    count+= math.ceil(number/speed)
                if (count > h):
                    return False
            return True
        
        lp = 1
        rp = max(piles)
        currentMin = rp
        while (lp <= rp):
            mid = lp + (rp-lp)//2
            
            if (satisfyMin(mid)):
                currentMin = min(currentMin,mid)
                rp = mid-1
            else:
                lp = mid+1
            
        return currentMin
            
         