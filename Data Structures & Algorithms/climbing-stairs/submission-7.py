class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[n] = 1
        dp[n - 1] = 1

        for a in range(n - 2, -1 , -1):
            dp[a] = dp[a + 1] + dp[a + 2]
        return dp[0]