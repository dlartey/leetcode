import math
class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far = -math.inf
        max_here = 0
        
        for i in range(N):
            max_here+=arr[i]
            
            if (max_here > max_so_far):
                max_so_far = max_here
            if (max_here < 0):
                max_here = 0
        
        return max_so_far