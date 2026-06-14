class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        candidates.sort()
        def dfs(i , total):
            nonlocal res
            if total == target:
                res.append(sol[:])
                return
            elif i == len(candidates):
                return

            a = candidates[i]
            if total + a > target:
                return

            sol.append(candidates[i])
            dfs(i + 1 , total + a)
            sol.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i = i + 1
            dfs(i + 1 , total)

        dfs(0,0)
        return res




        