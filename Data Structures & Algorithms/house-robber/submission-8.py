class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 , prev2 = 0 , 0

        for house in nums:
            tmp = prev1
            curr = max(prev2 + house, prev1)
            prev1 = curr
            prev2 = tmp
        return prev1