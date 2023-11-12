class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        n = len(candidates)

        if sum(candidates) < target:
            return []
            
        def dfs(i, current, total):
            if total == target:
                self.res.append(current.copy())
            
            if i >= n or total > target:
                return

            prev = -1

            for x in range(i,n):
                if candidates[x] == prev:
                    continue
                current.append(candidates[x])
                dfs(x+1,current,total+candidates[x])
                current.pop()
                prev = candidates[x]
            return


        dfs(0,[],0)
        return self.res
        