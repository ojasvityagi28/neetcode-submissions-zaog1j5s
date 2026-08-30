# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            a = dfs(root.left)
            b = dfs(root.right)
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            path_sum = root.val + a + b

            res = max(res , path_sum)

            return root.val + max(a , b)

        dfs(root)
        return res