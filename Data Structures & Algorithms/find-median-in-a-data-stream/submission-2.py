class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.small_heap or num < -1*self.small_heap[0]:
            heapq.heappush(self.small_heap , -num)
        else:
            heapq.heappush(self.large_heap , num)

        if len(self.small_heap) - len(self.large_heap) > 1:
            element = heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap , -element)

        if len(self.large_heap) - len(self.small_heap) > 1:
            element = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap , -element)
        
    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]
        elif len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]

        return ((-self.small_heap[0]) + self.large_heap[0])/2

        
        