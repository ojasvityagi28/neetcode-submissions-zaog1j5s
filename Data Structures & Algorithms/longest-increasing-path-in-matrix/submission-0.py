class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows = len(matrix)
        cols = len(matrix[0])
        res = -1

        def dfs(r , c , prevval):
            if (r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prevval):
                return 0
            if (r ,c) in dp:
                return dp[(r , c)]

            res = 1 + dfs(r + 1 , c , matrix[r][c])
            res = max(res , 1 + dfs(r - 1 , c , matrix[r][c]))
            res = max(res , 1 + dfs(r , c + 1, matrix[r][c]))
            res = max(res , 1 + dfs(r , c - 1 , matrix[r][c]))
            dp[(r,c)] = res
            return dp[(r , c)]

        for r in range(rows):
            for c in range(cols):
                length = dfs(r , c , -1)
                if length > res:
                    res = length
        return res
            
        