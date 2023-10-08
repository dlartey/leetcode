# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        temp = root
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.q.append(root)
            dfs(root.right)
            return
        dfs(temp)
        

    def next(self) -> int:
        return self.q.popleft().val

    def hasNext(self) -> bool:
        return len(self.q) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()