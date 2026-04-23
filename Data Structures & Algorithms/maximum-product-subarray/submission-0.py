class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin , curmax = 1, 1
        
        for a in nums:
            tmp = curmax
            curmax = max(a*curmax , a*curmin , a)
            curmin = min(a*tmp , a*curmin , a)
            res = max(curmax , res)
        return res

        