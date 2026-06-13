class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                length = 1
                num = nums[i]
                while num + 1 in hashset:
                    num = num + 1
                    length +=1
                res = max(res , length)

        return res
            

        