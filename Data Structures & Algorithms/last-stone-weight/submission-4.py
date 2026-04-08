class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxheap = [-n for n in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            diff = -(abs(x-y))
            if diff != 0:
                heapq.heappush(maxheap , diff)
        return -maxheap[0] if maxheap else 0
        
        