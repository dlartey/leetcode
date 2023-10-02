class Solution:
    def longestDupSubstring(self, s: str) -> str:
                # Use Rabin-Karp to calculate the substrings
        # Use binary search to find the string length which repeats
        b = 26
        n = len(s)
        modulus = 10**9 + 7
        self.ans = [-1,-1]
        # this is used to calculate the exponent for the numbers
        nums = [ord(s[i]) - ord('a') for i in range(n)]
        
        lp, rp = 0, n-1
        start = -1
        while lp <=rp:
            # this is the length of the substring we want to find duplicates for
            mid = lp + (rp-lp)//2
            startOfDup = self.search(mid,b,modulus,n,nums)
            
            if startOfDup != -1:
                lp = mid+1
                start = startOfDup
            else:
                rp = mid-1

        return s[start:start+lp-1]
    
    def search(self,mid,b,modulus,n,nums):
        # takes the substring size, modulus, base
        # formula for hash = (h*b + nums[i])%mod
        h = 0
        for x in range(mid):
            h = (h*b + nums[x])% modulus

        seen = collections.defaultdict(list)
        seen[h].append(0)
        expon = pow(b,mid,modulus)
        for i in range(1,n-mid+1):
            h = (h*b - nums[i-1]*expon + nums[mid+i-1]) % modulus

            if h in seen:
                current = nums[i:i+mid]
                if any(current == nums[index:index+mid] for index in seen[h]):
                    return i
            seen[h].append(i)
        return -1
        