class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0 , 1) , (0 , - 1) , (1 , 0), (-1 , 0)]
        pac_res = set()
        atl_res = set()
        pac_ocean = deque()
        atl_ocean = deque()
        rows = len(heights)
        cols = len(heights[0])

        for i in range(cols):
            pac_ocean.append((0 , i))
            pac_res.add((0 , i))
            atl_ocean.append((rows - 1 ,i))
            atl_res.add((rows - 1 ,i))

        for i in range(rows):
            pac_ocean.append((i , 0))
            pac_res.add((i , 0))
            atl_ocean.append((i , cols - 1))
            atl_res.add((i , cols - 1))

        def bfs(ocean_set ,q):
            while q:
                length = len(q)
                for i in range(length):
                    r , c = q.popleft()
                    for i, j in directions:
                        nr , nc = r + i , c + j
                        if nr < 0 or nr == rows or nc < 0 or nc == cols or (nr, nc) in ocean_set or heights[nr][nc] < heights[r][c]:
                            continue
                        ocean_set.add((nr , nc))
                        q.append((nr , nc))
        bfs(pac_res , pac_ocean)
        bfs(atl_res , atl_ocean)
        return list(pac_res & atl_res)


        


        