class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr_n = len(nums)
        xorr_nums = 0
        for i in range(len(nums)):
            xorr_n ^= i
            xorr_nums ^= nums[i]
        return xorr_n^xorr_nums
        