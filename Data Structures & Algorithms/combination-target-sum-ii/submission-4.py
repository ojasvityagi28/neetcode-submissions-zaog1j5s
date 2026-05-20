class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        candidates.sort()
        def dfs(i , total):
            if total == target:
                res.append(sol[:])
                return
            if i == len(candidates) or total > target:
                return

            sol.append(candidates[i]) #take ith candidate
            total += candidates[i]
            dfs(i + 1, total )

            #undo the changes
            a= sol.pop()
            total -= a

            j = i
            while j + 1 < len(candidates) and candidates[j + 1]== candidates[i]:
                j+= 1 # check the next number is not a duplicate
            #dont take candidate i
            dfs(j + 1 , total)
        dfs(0 , 0)
        return res

        