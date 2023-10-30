class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1

        for x in range(1, n):
            new_a = e
            new_e = a + i
            new_i = a + o + e + u
            new_o = i + u
            new_u = a

            a, e, i, o, u  = new_a, new_e, new_i, new_o, new_u

        return (a+i+e+o+u) % (10**9 + 7)