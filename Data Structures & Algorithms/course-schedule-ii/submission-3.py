class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i : [] for i in range(numCourses)}
        res = []
        for crs,pre in prerequisites:
            adjlist[crs].append(pre)
        seeing = set()
        seen = set()
        def dfs(i):
            if i in seen:
                return True
            if i in seeing:
                return False
            seeing.add(i)
            for crs in adjlist[i]:
                if not dfs(crs):
                    return False
            seeing.remove(i)
            seen.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


        