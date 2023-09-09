class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        res = [0]*26
        tempRes = [0]*26
        lp = 0
        rp = 0
        
        for i,x in enumerate(s1):
            res[ord(x)-ord("a")]+=1
            tempRes[ord(s2[i])-ord("a")]+=1
            
        
        if tempRes == res:
            return True
        
        
        for i in range(len(s1),len(s2)):
            tempRes[ord(s2[lp]) - ord("a")]-=1
            tempRes[ord(s2[i]) - ord("a")]+=1
            
            if (tempRes == res):
                return True
            lp+=1
            
        return False
            
            
        