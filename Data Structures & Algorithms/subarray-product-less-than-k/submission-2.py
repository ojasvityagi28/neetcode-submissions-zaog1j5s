class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        product = 1
        res = 0
        if k <= 1:
            return 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                if l <= r:
                    product = product/nums[l]
                    l += 1
            res += (r - l + 1)
        return res


        