class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i : [] for i in range(numCourses)}

        for crs,pre in prerequisites:
            adjlist[crs].append(pre)
        
        visiting = set()
        visited = set()
        res = []

        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting.add(c)

            for pre in adjlist[c]:
                if not dfs(pre):
                    return False


            visiting.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            

        