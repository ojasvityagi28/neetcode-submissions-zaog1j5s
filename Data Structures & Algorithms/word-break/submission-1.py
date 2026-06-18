class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(start):
            if start == len(s):
                return True
            if start in dp:
                return dp[start]
            dp[start] = False
            for i in range(start, len(s)):
                if s[start : i + 1] in wordDict:
                    if dfs(i + 1):
                        dp[start] = True
            return dp[start]
        return dfs(0)

        