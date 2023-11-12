class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(curr,indices):
            if len(indices) == n:
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
        