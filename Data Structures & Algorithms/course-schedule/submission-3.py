class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for c, p in prerequisites:
            if not c in pre:
                pre[c] = []
            pre[c].append(p)
        seen = set()
        seeing = set()

        def dfs(c):
            if c in seeing:
                return False
            if c in seen:
                return True
            seeing.add(c)
            if c in pre:
                for p in pre[c]:
                    if not dfs(p):
                        return False
            seeing.remove(c)
            seen.add(c)
            return True
        for c in range(numCourses):
            if c not in seen:
                if not dfs(c):
                    return False
        return True

            

        