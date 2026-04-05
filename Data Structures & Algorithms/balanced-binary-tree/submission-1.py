# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        self.diff = 0
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.diff = abs((1+left) - (1+right))

            if self.diff > 1:
                res = False
    
            return 1+ max(left,right)
        dfs(root)
        return res

        