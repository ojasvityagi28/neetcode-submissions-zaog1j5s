class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1]*n for _ in range(n)]

        def dfs(l , r):
            if l > r:
                return 0
            if l == r:
                return 1
            if dp[l][r] != -1:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = max(dp[l][r], 2 + dfs(l + 1 , r - 1))
            else:
                dp[l][r] = max(dfs(l + 1 , r), dfs(l , r - 1))

            return dp[l][r]

        return dfs(0, n - 1)