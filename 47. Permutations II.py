class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        memo = set()
        res = []
        n = len(nums)
        def dfs(curr,indices):
            
            if len(indices) == n:
                temp = curr.copy()
                if tuple(temp) not in memo:
                    memo.add(tuple(temp))
                    res.append(curr.copy())
                return
            
            for x in range(n):
                if x in indices:
                    continue

                curr.append(nums[x])
                indices.append(x)
                dfs(curr,indices)
                curr.pop()
                indices.pop()
            return

        dfs([],[])
        return res
        
        