class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n-1

        for x in range(n-1,-1,-1):
            if x+nums[x] >=goal:
                goal = x
                
        return True if goal == 0 else False

        