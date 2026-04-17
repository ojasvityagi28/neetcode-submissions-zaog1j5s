class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjlist = {(i, j): [] for i, j in points}
        for i , j in points:
            for p ,q in points:
                if [i , j] == [p , q]:
                    continue
                dist = abs(i - p) + abs(j - q)
                adjlist[(i, j)].append((dist , (p , q)))

        visit = set()
        res = 0
        minheap = [(0 , tuple(points[0]))]

        while minheap:
            if len(visit) == len(points):
                return res
            w , (i , j) = heapq.heappop(minheap)
            if (i, j) in visit:
                continue
            res += w
            visit.add((i , j))
            for a, (b,c) in adjlist[(i , j)]:
                if (b , c) not in visit:
                    heapq.heappush(minheap , (a , (b, c)))
        return res
            


                   