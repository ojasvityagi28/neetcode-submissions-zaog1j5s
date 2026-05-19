class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        helper = [(0 ,1), (0, -1), (1, 0), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i , j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        while q:
            length = len(q)
            for n in range(length):
                i , j = q.popleft()
                for ni, nj in helper:
                    if 0 <= (i + ni) < rows and 0 <= (j + nj) < cols:
                        if grid[i + ni][j + nj] == 1:
                            q.append((i + ni ,j + nj))
                            fresh -=1
                            grid[i + ni][j + nj] = 2
            if q:
                minutes +=1
        return minutes if fresh == 0 else -1
            
            
        