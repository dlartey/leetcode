class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxD = 0
        count = 0
        for x in range(len(s)):
            if (s[x] == "("):
                stack.append("*")
                count+=1
                maxD = max(count,maxD)

            if (s[x] == ")"):
                stack.pop()
                count-=1
        return maxD
        