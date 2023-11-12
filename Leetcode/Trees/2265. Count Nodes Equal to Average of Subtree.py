# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if node.left == None and node.right == None:
                self.res+=1
                return (node.val, 1)
            
            leftSum, rightSum = 0,0
            count, count2 = 0,0

            if node.left:
                leftSum, count = dfs(node.left)
            
            if node.right:
                rightSum, count2 = dfs(node.right)
            
            if (leftSum+rightSum+node.val)//(count+count2+1) == node.val:
                self.res+=1
            
            return (leftSum+rightSum+node.val, count+count2+1)

        dfs(root)

        return self.res
        