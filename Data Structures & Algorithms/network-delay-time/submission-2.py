class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = {i+1 : [] for i in range(n)}
        for u , v , t in times:
            adjlist[u].append((t,v))

        minheap = [(0,k)]
        visit = set()
        t = 0

        while minheap:
            w1 , n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)

            for w2,n2 in adjlist[n1]:
                heapq.heappush(minheap, (w2 + w1 , n2))

        return t if len(visit) == n else -1



        