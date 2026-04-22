class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(index):
            if index == len(s):
                return 1

            if index in memo:
                return memo[index]

            if s[index] == "0":
                return 0

            res = dfs(index + 1)

            if (index + 1) < len(s) and int(s[index : index + 2]) <= 26:
                res += dfs(index + 2)

            memo[index] = res
            return res
            

        return dfs(0)
        
        