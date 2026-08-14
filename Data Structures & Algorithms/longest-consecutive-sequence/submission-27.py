class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        res = 1

        for n in nums:
            if n - 1 not in numSet:
                seq = 1
                while n + 1 in numSet:
                    seq += 1
                    res = max(res , seq)
                    n += 1
        return res

        