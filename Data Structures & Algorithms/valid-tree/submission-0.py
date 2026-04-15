class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visiting = set()
        adjlist = {i: [] for i in range(n)}

        res = []

        for node, edge in edges:
            adjlist[node].append(edge)
            adjlist[edge].append(node)

        def dfs(node , prev):
            if node in visiting:
                return False

            visiting.add(node)
            
            for nei in adjlist[node]:
                if nei == prev:
                    continue
                if not dfs(nei , node):
                    return False

            visiting.remove(node)
            res.append(node)
            return res
        
        if not dfs(0 , -1):
            return False
        return len(res) == n
            
        






        