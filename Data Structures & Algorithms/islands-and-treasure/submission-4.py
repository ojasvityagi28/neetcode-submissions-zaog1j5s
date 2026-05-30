class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        dist = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        def addcell(i , j):
            if (i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j]!= 2147483647):
                return
            grid[i][j] = -2
            q.append((i,j))

        while q:
            length = len(q)
            for k in range(length):
                i , j = q.popleft()
                grid[i][j] = dist
                addcell(i + 1, j)
                addcell(i - 1, j)
                addcell(i , j + 1)
                addcell(i , j - 1)
            dist += 1
        