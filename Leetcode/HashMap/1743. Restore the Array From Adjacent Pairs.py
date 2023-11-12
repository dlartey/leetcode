class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacencyList = collections.defaultdict(list)
        start = 0
        res  = []
        visited = set()

        for pair in adjacentPairs:
            adjacencyList[pair[0]].append(pair[1])
            adjacencyList[pair[1]].append(pair[0])
        
        for k,v in adjacencyList.items():
            if len(v) == 1:
                start = k
                break
        
        def dfs(current):
            res.append(current)
            visited.add(current)

            for n in adjacencyList[current]:
                if not n in visited:
                    dfs(n)
            return
        
        dfs(start)
        return res
    # O(n)

        