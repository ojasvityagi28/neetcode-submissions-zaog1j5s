class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res , sol =[], []
        candidates.sort()
        def dfs(i, targetsum):
            if targetsum == target:
                res.append(sol[:])
                return
            elif i== len(candidates) or targetsum > target:
                return
            
            j = i
            while j+1 < len(candidates) and candidates[j+1] == candidates[j]:
                j+=1
            dfs(j + 1 , targetsum)
                 
            if targetsum + candidates[i] > target:
                return
            
            sol.append(candidates[i])
            targetsum += candidates[i]
            dfs(i+1 , targetsum)

            a = sol.pop()
            targetsum -= a
        dfs(0, 0)
        return res

        