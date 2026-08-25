class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = []
        for char in count:
            maxheap.append(-count[char])
        heapq.heapify(maxheap)
        q = deque()
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                freq = heapq.heappop(maxheap)
                if -(freq + 1) > 0:
                    q.append((freq + 1, time + n))
                
            if q and q[0][1] == time:
                heapq.heappush(maxheap , q.popleft()[0]) 

        return time
                
