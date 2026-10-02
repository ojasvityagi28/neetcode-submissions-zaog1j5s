# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {value : i for i, value in enumerate(inorder)}

        def dfs(preorder_start, preorder_end , inorder_start, inorder_end):
            if preorder_start > preorder_end:
                return None

            root_value = preorder[preorder_start]
            root = TreeNode(root_value)

            root_inorder_index = inorder_map[root_value]
            length_left_subtree = root_inorder_index - inorder_start


            root.left = dfs(preorder_start + 1, preorder_start + length_left_subtree, inorder_start ,root_inorder_index -1 )
     
            root.right = dfs(preorder_start +length_left_subtree + 1, preorder_end ,root_inorder_index + 1 , inorder_end)

            return root
        
        return dfs(0 , len(preorder) - 1, 0 , len(inorder) - 1)




