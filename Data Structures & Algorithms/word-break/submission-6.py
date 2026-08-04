class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]

            dp[i] = False

            for word in wordDict:
                length = len(word)
                if i + length <= len(s) and s[i : i+ length] == word:
                    if dfs(i + length):
                        dp[i] = True
            return dp[i]
        return dfs(0)

        