class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []

        for c in s:
            if c != '#':
                s1.append(c)
            else:
                if s1:
                    s1.pop()
        
        for a in t:
            if a != '#':
                s2.append(a)
            else:
                if s2:
                    s2.pop()
        
        return s1 == s2
        