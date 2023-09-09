class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums)-1
        #if nums[lp] < nums[rp] init, then normal bin search, else other search

        while (lp <= rp):
            mid = lp + (rp-lp)//2

            if (nums[mid] == target):
                return mid
            
            if nums[lp] <= nums[mid]:
                if target > nums[mid] or target < nums[lp]:
                    lp = mid+1
                else:
                    rp = mid -1
            else:
                if target < nums[mid] or target > nums[rp]:
                    rp = mid-1
                else:
                    lp = mid+1
        return -1
        