class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        n = len(pref)

        for x in range(1,n):
            # store calculated val by doing current prefix so far XOR current element
            temp = pref[x-1] ^ pref[x]
            res.append(temp)
            # update the prefix

        return res
        