"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        table = collections.defaultdict()
        dummy1 = head
        # add nodes to the hashmap
        while dummy1:
            temp = Node(dummy1.val)
            table[dummy1] = temp
            dummy1=dummy1.next
        
        dummy2 = head
        ans = Node(-1)
        res = ans
        while dummy2:
            node = table[dummy2]
            node.random = table.get(dummy2.random,None)
            ans.next = node
            ans = ans.next
            node = node.next
            dummy2 = dummy2.next
            
        return res.next
        