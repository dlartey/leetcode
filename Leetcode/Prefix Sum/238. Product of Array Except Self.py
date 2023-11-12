class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rv = [1]*n
        lv = [1]*n

        for x in range(1,n):
            lv[x] = lv[x-1]*nums[x-1]
        
        for y in range(n-2,-1,-1):
            rv[y] = rv[y+1]*nums[y+1]

        for i in range(n):
            rv[i] = rv[i]*lv[i]
        
        return rv
            