# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        table = collections.defaultdict(lambda: -math.inf) # Stored depth values

        def dfs(node, level):
            if node == None:
                return
            
            table[level] = max(node.val, table[level]) # O(1)
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)

            return

        dfs(root, 0) # O(n)
        return table.values()

        