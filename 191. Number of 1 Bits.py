class Solution:
    def hammingWeight(self, n: int) -> int:
        # idea use bit shift
        # check current bit & 1 == 1, inc counter
        # repeat until n > 0
        
        count = 0
        size = len(bin(n))-2
        for x in range(size):
            if (n&1 == 1):
                count+=1
            n = n >> 1
            
        return count
            
        