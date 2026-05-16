"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        orgTocopy = {}
        def dfs(node):
            if node in orgTocopy:
                return
            copy = Node(node.val)
            orgTocopy[node] = copy
            
            for n in node.neighbors:
                dfs(n)      
        dfs(node)

        for org in orgTocopy:
            copy = orgTocopy[org]
            if org.neighbors:
                copy.neighbors = []
                for nei in org.neighbors:
                    neicopy = orgTocopy[nei]
                    copy.neighbors.append(neicopy)
        return orgTocopy[node]






        