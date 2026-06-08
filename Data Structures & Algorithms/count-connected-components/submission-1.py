class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()

        adjlist = {i : [] for i in range(n)}
        for node1, node2 in edges:
            adjlist[node1].append(node2)
            adjlist[node2].append(node1)

        def dfs(node , prev):
            if node in visited:
                return
            visited.add(node)

            for n in adjlist[node]:
                if n == prev:
                    continue
                dfs(n , node)
        
        for c in range(n):
            if c not in visited:
                components += 1
                dfs(c , -1)
        return components
        