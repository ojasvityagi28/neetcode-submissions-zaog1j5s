class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        atlantic , pacific = [], []

        for r in range(rows):
            pacific.append((r , 0))
            atlantic.append((r , columns - 1))

        for c in range(columns):
            pacific.append((0 , c))
            atlantic.append((rows - 1 , c)) 

        atl = [[False] * columns for n in range(rows)] 
        pac = [[False] * columns for n in range(rows)]  

        def addcell(i , j , prevheight, ocean , q):
            if (i < 0 or i == rows or j < 0 or j == columns or ocean[i][j] == True or heights[i][j] < prevheight ):
                return
            q.append((i , j))

        def bfs(source , ocean):
            q = deque(source)
            while q:
                length = len(q)
                for a in range(length):
                    i , j = q.popleft()
                    ocean[i][j] = True
                    prevheight = heights[i][j]
                    addcell(i + 1 , j , prevheight , ocean , q )
                    addcell(i - 1 , j , prevheight , ocean , q )
                    addcell(i , j - 1 , prevheight , ocean , q )
                    addcell(i , j + 1 , prevheight , ocean , q )


        bfs(pacific , pac)
        bfs(atlantic , atl)
        res = []
        for r in range(rows):
            for c in range(columns):
                if atl[r][c] and pac[r][c]:
                    res.append([r , c])
        return res
            