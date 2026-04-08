class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:k]
        heapq.heapify(minheap) #o(k)
        for a in nums[k:]:
            if a > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap , a)
        return minheap[0]        