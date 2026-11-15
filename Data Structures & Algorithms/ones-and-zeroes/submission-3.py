class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [[0, 0] for i in range(len(strs))]
        dp = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]

        for i,s in enumerate(strs):
            for char in s:
                if char == "1":
                    count[i][1] += 1
                else:
                    count[i][0] += 1
        sol = []
        
        def dfs(index, zero_count, one_count):
            if index == len(strs):
                return 0
            
            if dp[index][zero_count][one_count] != -1:
                return dp[index][zero_count][one_count]
            
            res = dfs(index + 1, zero_count, one_count)

            if zero_count + count[index][0] <= m and one_count + count[index][1] <= n:
                res = max(res, 1 + dfs(index + 1, zero_count + count[index][0], one_count + count[index][1]) )

            dp[index][zero_count][one_count] = res

            return res
        
        return dfs(0 , 0 , 0)

        