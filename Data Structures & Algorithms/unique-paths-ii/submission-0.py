class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[-1]*cols for _ in range(rows)]

        def dfs(i , j):
            if i == rows or j == cols or obstacleGrid[i][j] == 1:
                return 0
            if i == rows - 1 and j == cols - 1 and obstacleGrid[i][j] == 0:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs( i + 1 , j) + dfs(i , j + 1)

            return dp[i][j]
      
        return dfs(0 , 0)

        