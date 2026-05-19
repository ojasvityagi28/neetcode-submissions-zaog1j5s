class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        dp = {}
        def dfs(i , maximum):
            nonlocal res
            if i>= len(nums):
                return res
            if (i , maximum) in dp:
                return dp[(i , maximum)]
            maximum += nums[i]
            res = max(res , maximum)
            dp[(i + 2 , maximum)] = dfs(i + 2 , maximum)
            maximum -= nums[i]
            res = max(res , maximum)
            dp[(i + 1 , maximum)]= dfs(i + 1 , maximum)
            return res
        return dfs(0 , 0)