class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height)-1
        maxArea = -math.inf
        while (lp < rp):
            maxi = min(height[lp],height[rp])
            maxArea=max(maxArea,(rp-lp)*maxi)
            
            if (height[lp] <= height[rp]):
                lp+=1
            else:
                rp-=1
                
        return maxArea
            
        