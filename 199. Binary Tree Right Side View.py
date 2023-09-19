# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        table = collections.defaultdict()

        def rsv(root,level):
            if root == None:
                return

            if not level in table:
                table[level] = root.val
                
            rsv(root.right,level+1)
            rsv(root.left,level+1)
        
        rsv(root,0)
        count = 0

        while count in table:
            ans.append(table[count])
            count+=1
        return ans
        