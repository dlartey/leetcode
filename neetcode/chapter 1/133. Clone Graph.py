"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        table = collections.defaultdict()

        if not node:
            return None

        # use a queue to do BFS and store in a hashmap a list of the currentNode -> newNode
        q = deque()
        temp = None
        if node:
            q.append(node)
        
        while q:
            current = q.popleft()

            if current in table:
                continue
            
            table[current] = Node(current.val, None)
            # adds the neighbours to the BFS queue
            for n in current.neighbors:
                if not n in table:
                    q.append(n)
        
        for key in table.keys():
            for n in key.neighbors:
                table[key].neighbors.append(table[n])
 
        return table[node]

        
        