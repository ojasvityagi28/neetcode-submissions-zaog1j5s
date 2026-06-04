class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = { i:[] for i in range(numCourses)}
        visiting = set()

        for crs, pre in prerequisites:
            adjlist[crs].append(pre)

        visited = set()
        res = []
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True #visited and already added

            visiting.add(crs)

            for pre in adjlist[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res


        