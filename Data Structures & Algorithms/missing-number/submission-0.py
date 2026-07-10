class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_n = 0
        sum_nums = 0
        for i,n in enumerate(nums):
            sum_nums += n
            sum_n += i
        sum_n += len(nums)
        return sum_n - sum_nums

        