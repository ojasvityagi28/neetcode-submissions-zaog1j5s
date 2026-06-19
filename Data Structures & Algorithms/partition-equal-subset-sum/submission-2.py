class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [[None for i in range(target + 1)] for y in range(len(nums))]

        def dfs(i , target):
            if target == 0:
                return True
            if i>= len(nums) or target < 0:
                return False

            if dp[i][target] is not None:
                return dp[i][target]

            dp[i][target] = dfs(i + 1 , target) or dfs(i +1 , target - nums[i]) 

            return dp[i][target]
        return dfs(0 , target) 

        