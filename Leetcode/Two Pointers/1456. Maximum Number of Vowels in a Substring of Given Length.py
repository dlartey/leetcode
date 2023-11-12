class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a":1, "e":1, "i":1, "o":1, "u":1}

        n = len(s)

        count = 0
        for x in range(0,k):
            count += vowel.get(s[x],0)

        maxi = count
        
        for lp in range(0,n-k):
            count-= vowel.get(s[lp],0)
            count+= vowel.get(s[lp+k],0)
            
            if count > maxi:
                maxi = count

        return maxi



        