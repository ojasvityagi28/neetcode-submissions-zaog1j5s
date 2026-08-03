class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxE = nums[0]
        res = []
        seen_index = 0
        for i in range(k):
            if nums[i] >= maxE:
                maxE = nums[i]
                seen_index = i
        res.append(maxE)

        l = 0
        for r in range(k,len(nums)):
            if l != seen_index:
                if nums[r] >= maxE:
                    maxE = nums[r]
                    seen_index = r
                res.append(maxE)
            else:
                maxE = nums[l + 1]
                seen_index = l + 1
                for j in range(l + 1,r + 1):
                    if nums[j] >= maxE:
                        seen_index = j
                        maxE = nums[j]
                res.append(maxE)
            l += 1
        return res


        

        