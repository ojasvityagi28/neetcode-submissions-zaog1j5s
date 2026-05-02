class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = nums[0]
        res = nums[0]
        for i in range(1 ,len(nums)):
            if nums[i] + cursum >= nums[i]:
                cursum += nums[i]
            else:
                cursum = nums[i]
            res = max(cursum , res)
        return res
        