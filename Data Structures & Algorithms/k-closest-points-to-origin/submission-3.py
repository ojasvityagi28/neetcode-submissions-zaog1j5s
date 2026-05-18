class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = math.sqrt(x**2 + y**2)
            minheap.append((distance , x , y))
        heapq.heapify(minheap)
        res= []
        while k > 0:
            d , x , y = heapq.heappop(minheap)
            res. append([x, y])
            k-=1
        return res


        