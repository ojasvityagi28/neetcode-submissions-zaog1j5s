class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        res = []
        def dfs(start ,total):
            nonlocal res
            if total == target:
                res.append(comb[:])  
                return
            for i in range(start,len(nums)):
                a= nums[i]
                if total + a > target:
                    continue
                total += a
                comb.append(a)
                dfs(i , total)
                total -= a
                comb.pop()
        dfs(0, 0)
        return res


                  