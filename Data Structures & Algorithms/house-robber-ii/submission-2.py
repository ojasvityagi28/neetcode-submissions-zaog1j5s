class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = max(self.helper(nums[:-1]) , self.helper(nums[1:]) )
        return res

    def helper(self, nums):
        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):
            curr = max(nums[i] + prev2 , prev1)
            prev1 , prev2 = curr , prev1
        return prev1



        