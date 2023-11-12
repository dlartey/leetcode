class Solution:
    def countBits(self, n: int) -> List[int]:
        # idea loop from 1 to n+1 O(n)
        # then get the number of 1 bits
        res = []
        for x in range(0,n+1):
            res.append(self.calculate1bits(x))
        return res
    
    def calculate1bits(self,n):
        res = 0
        while n:
            n&=n-1
            res+=1
        return res
        