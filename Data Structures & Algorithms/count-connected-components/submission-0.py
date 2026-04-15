class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visit = set()

        adjlist = {i: [] for i in range(n)}

        for node, edge in edges:
            adjlist[node].append(edge)
            adjlist[edge].append(node)

        def dfs(node , prev):
            if node in visit:
                return

            visit.add(node)

            for nei in adjlist[node]:
                if nei == prev:
                    continue
                else:
                    dfs(nei , node)
            


        for c in range(n):
            if c not in visit:
                components+= 1
                dfs(c , -1)
        return components
