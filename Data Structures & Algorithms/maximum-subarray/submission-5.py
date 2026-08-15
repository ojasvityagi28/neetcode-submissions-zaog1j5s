class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        res = float('-inf')

        for n in nums:
            if cursum + n >= n:
                cursum += n
            else:
                cursum = n
            res = max(cursum , res)
        return res
        

        