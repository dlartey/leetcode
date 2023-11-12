class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjList = collections.defaultdict(list)
        self.nodes = set()

        for edge in edges:
            start, end, cost = edge
            self.adjList[start].append((end,cost))
            self.nodes.add(start)
            self.nodes.add(end)
        
    def addEdge(self, edge: List[int]) -> None:
            start, end, cost = edge
            self.adjList[start].append((end,cost))
            self.nodes.add(start)
            self.nodes.add(end)
        
    def shortestPath(self, node1: int, node2: int) -> int:
        unvisited = list(self.nodes)
        self.minCost = collections.defaultdict(lambda: math.inf)

        self.minCost[node1]=0
        while unvisited:
            currentMinNode = None
            for node in unvisited:
                if currentMinNode == None:
                    currentMinNode = node
                elif self.minCost[node] < self.minCost[currentMinNode]:
                    currentMinNode = node
            
            neighbours = self.adjList[currentMinNode]
            for n in neighbours:
                temp = self.minCost[currentMinNode]+ n[1]
                if temp < self.minCost[n[0]]:
                    self.minCost[n[0]] = temp
            
            unvisited.remove(currentMinNode)
           
        return -1 if self.minCost[node2] == math.inf else self.minCost[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)