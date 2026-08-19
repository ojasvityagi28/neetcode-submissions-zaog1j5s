from _heapq import heapify
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        l = 0
        for i in range(l , k):
            max_heap.append((-nums[i], i))

        heapq.heapify(max_heap)
        res.append(-max_heap[0][0])

        for r in range(k , len(nums)):
            l += 1
            heapq.heappush(max_heap , (-nums[r], r))
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
        return res


        