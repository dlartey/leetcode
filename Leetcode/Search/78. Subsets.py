class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # either append current element or choose nothing

        def dfs(curr, i):
            if i == n:
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()

            dfs(curr, i+1)
            
            return

        
        dfs([],0)
        return res
        