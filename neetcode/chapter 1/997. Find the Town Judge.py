class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree= [0]*n
        trustMatrix = collections.defaultdict()
        for x in trust:
            indegree[x[1]-1]+=1
            if not x[0] in trustMatrix:
                trustMatrix[x[0]] = []
            trustMatrix[x[0]].append(x[1])
        
        if (len(trustMatrix)==n):
            return -1
        
        for x in range(1,n+1):
            if x not in trustMatrix and indegree[x-1]==n-1:
                return x
        return -1
