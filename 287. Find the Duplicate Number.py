class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        elems = set()

        for x in nums:
            if x in elems:
                return x
            else:
                elems.add(x)

        