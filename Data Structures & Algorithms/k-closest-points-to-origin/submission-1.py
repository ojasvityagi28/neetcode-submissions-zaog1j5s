class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minheap =[]
        for x, y in points:
            dist = x**2 + y**2
            minheap.append((dist , (x,y)))
        heapq.heapify(minheap)

        while k > 0:
            a = heapq.heappop(minheap)
            res.append(a[1])
            k-=1
        return res
            

        