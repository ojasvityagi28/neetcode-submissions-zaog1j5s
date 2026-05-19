class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        rob2 = nums[0]
        rob1 = max(nums[0], nums[1])
        for i in range(2,n):
            curr = max(nums[i] + rob2, rob1)
            tmp = rob1
            rob1 = curr # curr value will be 1 steps back
            rob2 = tmp #2 steps back will be 1 step back value

        return rob1
        