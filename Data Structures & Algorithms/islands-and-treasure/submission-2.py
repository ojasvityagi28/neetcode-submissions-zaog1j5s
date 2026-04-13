class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        columns = len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    q.append((i , j))
                    
        def addcell(i , j):
            if (i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j]!= 2147483647):
                return
            grid[i][j] = -2
            q.append((i , j))

        dist = 0
        while q:
            length = len(q)
            for a in range(length): 
                i , j = q.popleft()
                grid[i][j] = dist
                addcell(i + 1 , j ) #added rooms that are one cell away
                addcell(i - 1 , j ) # then incremented dist by 1
                addcell(i , j - 1 ) 
                addcell(i , j + 1 ) 
            dist += 1
  


        


        