class Solution:
    def secondHighest(self, s: str) -> int:
        dicti = {}
        for x in range(len(s)):
            if ord(s[x]) >= ord("0") and ord(s[x]) <= ord("9"):
                # then it's a number add it to the map
                val = int(s[x])
                if not val in dicti:
                    dicti[val] = 0
                dicti[val]+=1
        
        if (len(dicti) < 2):
            return -1
        
        heap = [key for key in dicti.keys()]
        return heap[1]

                
        