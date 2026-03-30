class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset=set(nums)
        maxlength=0
        length=1
        for n in nums:
            if (n-1) not in hashset:
                length=1
                while (n+length) in hashset:
                    length+=1
                maxlength=max(length,maxlength)
        return maxlength

