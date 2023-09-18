# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,counter):
            if root == None:
                return counter
            
            return max(dfs(root.left,counter+1),dfs(root.right,counter+1))

        return dfs(root,0)
        