class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        if not height:
            return 0
        
        lp, rp = 0, len(height)-1
        lMax, rMax = height[lp], height[rp]

        while lp < rp:
            if lMax < rMax:
                lp+=1
                lMax = max(lMax, height[lp])
                res+= lMax - height[lp]
            else:
                rp-=1
                rMax = max(rMax,height[rp])
                res+= rMax-height[rp]

        return res
        