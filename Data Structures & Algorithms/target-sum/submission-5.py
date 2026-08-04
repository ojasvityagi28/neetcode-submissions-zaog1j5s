class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        total = 0

        def dfs(index , total):
            if index == len(nums) and target == total:
                return 1
            if index == len(nums):
                return 0
            if (index , total) in dp:
                return dp[(index , total)]

            dp[(index, total)] = dfs(index + 1,total + nums[index]) + dfs(index + 1, total - nums[index])

            return dp[(index , total)]
        return dfs(0 , 0)
