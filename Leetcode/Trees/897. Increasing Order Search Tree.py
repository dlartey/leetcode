# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        #in order -> left, current, right
        q = deque()
        temp = root

        def inOrder(root):
            if root == None:
                return

            inOrder(root.left)
            q.append(root)
            inOrder(root.right)
            root.left, root.right = None, None
            return
        # now inOrder traversal is in the queue

        inOrder(temp)
        temp2 = TreeNode()
        temp3 = temp2
        while q:
            temp2.right, temp2.left = q.popleft(), None
            temp2 = temp2.right
        
        return temp3.right