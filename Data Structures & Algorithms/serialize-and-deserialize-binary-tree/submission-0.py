# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        q = deque([root])
        string = []
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node == "N":
                    string.append("N")
                    continue
                string.append(str(node.val))
                q.append(node.left) if node.left else q.append("N")
                q.append(node.right) if node.right else q.append("N")
        return ",".join(string)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        if values[0] == "N":
            return None
        root = TreeNode(int(values[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()

            if i < len(values):
                node.left = TreeNode(int(values[i])) if values[i]!= "N" else None
                if node.left:
                    q.append(node.left)
                i += 1
            if i < len(values):
                node.right = TreeNode(int(values[i])) if values[i]!= "N" else None
                if node.right:
                    q.append(node.right)
                i += 1
        return root

                
                





