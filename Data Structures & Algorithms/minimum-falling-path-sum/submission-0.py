class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        #base case 
        # if row == len(matrix): return 0
        dp = [[None]*len(matrix[0]) for _ in range(len(matrix))]
        def dfs(r , c):
            if r == len(matrix):
                return 0

            if c == len(matrix[0]) or c < 0:
                return float('inf')

            if dp[r][c] != None:
                return dp[r][c]

            dp[r][c] = matrix[r][c] + min(dfs(r+1, c-1), dfs(r+1, c), dfs(r+1, c+1))
            
            return dp[r][c]
        
        res = float('inf')
        
        for c in range(len(matrix[0])):
            res = min(res , dfs(0 , c))
        
        return res

