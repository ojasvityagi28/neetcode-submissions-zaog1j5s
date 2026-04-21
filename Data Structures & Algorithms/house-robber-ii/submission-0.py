class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper( nums):
            n = len(nums)
            prev = 0
            curr = 0
            for i in range(n):
                tmp = curr
                curr = max(nums[i] + prev , curr)
                prev = tmp #value of rob1 without adding the nums[i]
            return curr

        a = helper(nums[1:])
        b = helper(nums[:-1])
        return max(nums[0], a  , b)


        

        
        