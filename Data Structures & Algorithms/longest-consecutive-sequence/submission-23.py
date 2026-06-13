class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        res = 0
        for i in range(len(nums)):
            length = 1
            num = nums[i]
            while num - 1 in hashset:
                num = num-1
                length +=1
            num = nums[i]
            while num + 1 in hashset:
                num = num + 1
                length +=1
            res = max(res , length)
            hashset.add(nums[i])
        return res
            

        