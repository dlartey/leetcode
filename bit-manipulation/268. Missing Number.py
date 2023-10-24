class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for x in range(nums):
            res = res ^ nums[x] ^ x

        return res
        # O(n) time complexity
        # O(1) space complexity