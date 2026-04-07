# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        res = 0
        def inorder(root):
            nonlocal res
            if not root:
                return
            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                res = root.val
            inorder(root.right)
            return res

        return inorder(root)

            
            
            
        