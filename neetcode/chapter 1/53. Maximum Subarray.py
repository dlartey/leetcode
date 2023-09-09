class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csf = 0
        maxi = -math.inf
        
        for num in nums:
            csf += num
            maxi = max(maxi,csf)
            
            if (csf < 0):
                csf = 0
        
        return maxi
        