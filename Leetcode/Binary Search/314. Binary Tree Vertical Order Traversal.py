# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = collections.defaultdict(list)

        def dfs(node, level, pos):
            if not node:
                return
            
            table[pos].append((level, node.val))
            dfs(node.left, level+1, pos-1)
            dfs(node.right, level+1, pos+1)
            return
        
        dfs(root, 0, 0)
        res = []
        
        for k in sorted(table.keys()):
            table[k].sort(key=lambda x:x[0])
            res.append([x[1] for x in table[k]])
        
        return res

        