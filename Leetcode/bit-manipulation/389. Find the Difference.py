class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0

        for x in range(len(s)):
            ans = ans ^ ord(s[x]) ^ ord(t[x])

        ans = ans ^ ord(t[-1])
        
        return chr(ans)
        