# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        table = collections.defaultdict(int)
        if root:
            q.append(root)

        while q:
            current = q.popleft()

            table[current.val]+=1
            if current.left:
                q.append(current.left)
            
            if current.right:
                q.append(current.right)
        res = []
        maxFreq = max(table.values())

        for k,v in table.items():
            if v == maxFreq:
                res.append(k)
        
        return res