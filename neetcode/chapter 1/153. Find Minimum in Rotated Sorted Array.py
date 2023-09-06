class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums)-1
        res = nums[0]
        
        while (lp <= rp):
            
            if (nums[lp] < nums[rp]):
                res = min(res,nums[lp])
                break
                
            mid = lp + (rp-lp)//2
            res = min(res,nums[mid])
            if (nums[mid] >= nums[lp]):
                lp= mid+1
            else:
                rp = mid-1
        
        return res