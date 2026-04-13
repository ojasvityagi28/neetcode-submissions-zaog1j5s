class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r , c))

        def addcell( i , j):
            nonlocal fresh
            if ( i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j]!= 1):
                return
            q.append((i , j))
            fresh -= 1
            grid[i][j] = 2

        minutes = 0

        while q:
            length = len(q)
            for a in range(length):
                i , j = q.popleft()
                addcell(i + 1 , j)
                addcell(i - 1 , j)
                addcell(i , j - 1)
                addcell(i , j + 1)
            if q:
                minutes+=1
        return minutes if fresh == 0 else -1
                


        