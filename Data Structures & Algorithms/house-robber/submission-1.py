class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            prev = nums[0]
            return prev
        if n == 2:
            curr = max(nums[0], nums[1])
            return curr
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2 , n):
            tmp = curr
            curr = max(prev + nums[i], curr)
            prev = tmp

        return curr

        