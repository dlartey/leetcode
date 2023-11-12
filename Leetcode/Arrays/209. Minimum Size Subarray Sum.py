class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp = 0
        minLen = math.inf
        currentSum = 0
        for rp in range(len(nums)):
            currentSum+=nums[rp]
            while (currentSum >= target):
                minLen = min(minLen,(rp-lp+1))
                currentSum-=nums[lp]
                lp+=1

        return 0 if minLen > len(nums) else minLen
        