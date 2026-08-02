class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for c, p in prerequisites:
            if c not in pre:
                pre[c] = []
            pre[c].append(p)
        visiting = set()
        visited = set()
        def dfs(crs):
            if crs not in pre:
                return True
            if crs in visited:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)

            for pres in pre[crs]:
                if not dfs(pres):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
        