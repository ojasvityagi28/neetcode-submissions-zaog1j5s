class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n]+=1

        min_heap = []

        for key,value in count.items():
            heapq.heappush(min_heap , (value , key) )
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        while k > 0:
            a , b = heapq.heappop(min_heap)
            res.append(b)
            k-=1
        return res
        