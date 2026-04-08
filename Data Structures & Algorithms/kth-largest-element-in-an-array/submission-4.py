class Solution:
    def quickselect(self, nums , k):
        l = 0
        r = len(nums)-1
        while True:
            if r <= l+1:
                if r==l+1 and nums[r] > nums[l]:
                    nums[l],nums[r] = nums[r] , nums[l]
                return nums[k]

            j = self.partition (nums , l , r)
            if j == k:
                return nums[k]
            if k < j:
                r = j - 1
            if k > j:
                l = j + 1

    def partition(self ,nums , l , r):
        mid = (l+r)//2
        nums[mid], nums[l+1] = nums[l+1], nums[mid]
        if nums[r] > nums[l]:
            nums[r], nums[l] = nums[l], nums[r]
        if nums[r] > nums[l+1]:
            nums[r], nums[l+1] = nums[l+1], nums[r]  
        if nums[l + 1] > nums[l]:
            nums[l+1], nums[l] = nums[l], nums[l+1] 
        pivot = nums[l+1]
        i = l+1
        j = r
        while True:
            while True:
                i+=1
                if not nums[i] > pivot:
                    break
            while True:
                j-=1
                if not nums[j] < pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j] , nums[i]
        nums[l+1], nums[j] = nums[j] , nums[l+1]
        return j
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums , k -1 )
    

        # minheap = nums[:k]
        # heapq.heapify(minheap) #o(k)
        # for a in nums[k:]:
        #     if a > minheap[0]:
        #         heapq.heappop(minheap)
        #         heapq.heappush(minheap , a)
        # return minheap[0]        
