# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root,maxi):
            if not root:
                return
            
            if root.val >= maxi:
                self.res+=1
                maxi = root.val    
            
            dfs(root.left,maxi)
            dfs(root.right,maxi)
            return
        
        dfs(root,-math.inf)
        return self.res
        