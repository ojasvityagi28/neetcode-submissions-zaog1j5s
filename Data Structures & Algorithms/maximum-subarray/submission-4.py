class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        maxsum = cursum

        for i,n in enumerate(nums):
            if i == 0:
                continue
            if n + cursum >= n:
                cursum += n
            else:
                cursum = n
            maxsum = max(maxsum , cursum)
        return maxsum
        