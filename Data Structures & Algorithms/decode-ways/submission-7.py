class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(index):
            if index >= len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in dp:
                return dp[index]
            
 
            res = dfs(index + 1)
        
            if index + 1 < len(s) and (s[index] == "1" or s[index] == "2" and s[index + 1] in "0123456"):
                res += dfs(index + 2)

            dp[index] = res
            return res

        return dfs(0)


        