class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax , curmin = nums[0] , nums[0]
        res = nums[0]

        for i,n in enumerate(nums):
            if i == 0:
                continue
            tmp = curmax
            curmax = max(curmax*n , curmin*n , n)
            curmin = min(curmin*n , tmp*n , n)

            res = max(curmax , res)
        return res
        