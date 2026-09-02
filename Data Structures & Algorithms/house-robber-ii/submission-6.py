class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.rob1(nums[:n - 1]), self.rob1(nums[1:]))
    
    def rob1(self, nums):
        prev1 = 0
        prev2 = 0

        for n in nums:
            tmp = prev1
            prev1 = max(prev2 + n, prev1)
            prev2 = tmp
        return prev1



        