class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {i : [] for i in range(n)}

        for node , edge in edges:
            adjlist[node].append(edge)
            adjlist[edge].append(node)
        seeing = set()
        edge_count = 0
        def dfs(n , prev):
            nonlocal edge_count
            if n in seeing:
                return False
            seeing.add(n)

            for e in adjlist[n]:
                if e == prev:
                    continue
                edge_count += 1
                if not dfs(e , n):
                    return False

            seeing.remove(n)
            adjlist[n] = []
            return True

        
        if not dfs(0 , -1):
            return False
        return n - 1 == edge_count



        

        