class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        minHeap = [-cnt for cnt in count.values()]
        heapq.heapify(minHeap)

        time = 0
        q = deque()

        while minHeap or q:
            time += 1

            if minHeap:
                a = heapq.heappop(minHeap)
                if a + 1 != 0:
                    q.append((a + 1, time + n))

            if q and q[0][1] == time:
                heapq.heappush(minHeap , q.popleft()[0])
        
        return time



        