class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax = nums[0]
        curmin = nums[0]
        res = nums[0]
        for i,n in enumerate(nums):
            if i== 0:
                continue
            tmp = curmax
            curmax = max(n*curmax , n*curmin , n)
            curmin = min(n*tmp , n*curmin , n)  
            res = max(curmax , res) 
        return res    