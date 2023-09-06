class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        hashSet = set()
        for lp in range(len(nums)):
            # calculate the missing number to find
            rp = len(nums)-1
            mid = lp+1
            while (lp < rp and mid < rp):
                missing = 0 - (nums[lp]+nums[rp])
                if (nums[mid] == missing):
                    tempAns = (nums[lp],nums[mid],nums[rp])
                    if (tempAns not in hashSet):
                        ans.append([nums[lp],nums[mid],nums[rp]])
                        hashSet.add(tempAns)
                    mid+=1
                if (nums[mid] > missing):
                    rp-=1
                    # calculate
                if (nums[mid] < missing):
                    mid+=1
        return ans
        