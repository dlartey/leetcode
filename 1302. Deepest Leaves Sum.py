# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        table = collections.defaultdict(int)
        self.maxi = -math.inf
        
        def dfs(root,level):
            if not root:
                return
            self.maxi = max(self.maxi,level)
            table[level]+=root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
            return
        
        dfs(root,0)
        return table[self.maxi]
        