class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        visit.add((0,0))
        minheap = [(grid[0][0] , 0 , 0)]
        directions = [( 0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
        
        while minheap:
            t , r , c = heapq.heappop(minheap)
            if r == N - 1 and c == N - 1:
                return t
                break
            for dr , dc in directions:
                nr , nc = r + dr , c + dc
                if ((nr , nc) in visit or nr < 0 or nc < 0 or nr == N or nc == N):
                    continue
                visit.add((nr , nc))
                heapq.heappush(minheap , (max(t , grid[nr][nc]) , nr , nc))
        return t


        