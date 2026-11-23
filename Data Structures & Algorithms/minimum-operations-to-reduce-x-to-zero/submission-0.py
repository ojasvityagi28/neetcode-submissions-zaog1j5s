class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x > sum(nums):
            return -1

        target = sum(nums) - x

        l = 0
        total = 0
        length = -1
        for r in range(len(nums)):
            total += nums[r]
            while total > target:
                total -= nums[l]
                l += 1
            if total == target:
                length = max(length, r - l + 1)
        
        if length == -1:
            return -1
        else:
            return len(nums) - length