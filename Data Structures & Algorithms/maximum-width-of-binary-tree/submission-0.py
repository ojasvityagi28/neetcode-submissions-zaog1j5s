# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q = deque([(root , 1)])
        res = float('-inf')
        last_length = 1
        
        while q:
            length = len(q)

            first_position = 0

            for i in range(length):
                node, pos = q.popleft()
                if i == 0:
                    first_position = pos

                if node.left:
                    q.append((node.left, 2*pos))

                if node.right:
                    q.append((node.right, 2*pos + 1))

            res = max(pos - first_position + 1, res)
        
        return res