class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        dir = [(1, 0) , (-1 , 0), (0 , 1), (0 , -1)]

        def dfs(i , j , prev):
            if i < 0 or i == m or j < 0 or j ==n or matrix[i][j] <= prev:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]

            for dx, dy in dir:
                dp[i][j] = max(dp[i][j] ,1 + dfs(i + dx, j + dy , matrix[i][j]))
            return dp[i][j]
        res = 0
        for r in range(m):
            for c in range(n):
                length = dfs(r , c, float("-inf"))
                res = max(res , length )
        return res




            
            
        