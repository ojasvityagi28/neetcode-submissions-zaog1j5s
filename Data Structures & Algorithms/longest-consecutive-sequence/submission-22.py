class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res=0 

        for n in nums:
            if (n-1) not in hashset :
                curr_streak =1
                curr_no = n
                while (curr_no+1) in hashset:
                    curr_no +=1
                    curr_streak+=1
                    if curr_streak == len(nums):
                        return curr_streak
                res = max(res, curr_streak)
        return res

        