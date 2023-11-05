"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        self.q = deque()

        def findMinLeft(node):
            self.q.append(node.right)

            while self.q:
                current = self.q.popleft()
                
                if current.left:
                    self.q.append(current.left)
                else:
                    return current

        def findMinParent(node):
            if node.parent:
                self.q.append(node.parent)
            
            while self.q:
                current = self.q.popleft()
                if current.val > node.val:
                    return current
                
                if current.parent:
                    self.q.append(current.parent)
            
            return None

        if node.right:
           return findMinLeft(node)
        else:
            return findMinParent(node)
            
        