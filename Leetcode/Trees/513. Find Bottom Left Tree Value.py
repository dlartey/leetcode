# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        table = collections.defaultdict(list)
        self.maxLevel = 0
        def dfs(root,level):
            if root == None:
                return
            
            if level > self.maxLevel:
                self.maxLevel = level
            dfs(root.left,level+1)
            table[level].append(root.val)
            dfs(root.right,level+1)
            return

        dfs(root,0)
        return table[self.maxLevel][0]

            
        