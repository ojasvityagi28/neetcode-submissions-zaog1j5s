class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        res = 0
        area = 0

        def dfs(i , j):
            nonlocal area
            if (i < 0 or i >= rows or j < 0 or j>= columns) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            area = ( 1 + dfs(i + 1 , j) +
            dfs(i - 1 , j) +
            dfs(i , j + 1) +
            dfs(i , j - 1) )
            return area
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area =dfs(i , j)
                    res = max( area , res)
        return res
              