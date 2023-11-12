class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if (len(t) > len(s)):
            return ""
        tFreq = [0]*(ord("z")-ord("A")+1)
        lp = 0
        res = math.inf
        ans = ""
        currFreq = [0]*(ord("z")-ord("A")+1)
        uniqueChars = set(t)

        for char in t:
            tFreq[ord(char) - ord("A")]+=1

        def atLeastEqual():
            for char in uniqueChars:
                if (currFreq[ord(char)-ord("A")] < tFreq[ord(char)-ord("A")]):
                    return False
            return True

        for rp in range(len(s)):
            currFreq[ord(s[rp]) - ord("A")]+=1

            while atLeastEqual():
                if ((rp-lp+1) < res):
                    res = rp-lp+1
                    ans = s[lp:rp+1]
                currFreq[ord(s[lp]) - ord("A")]-=1
                lp+=1

        return ans
        
        