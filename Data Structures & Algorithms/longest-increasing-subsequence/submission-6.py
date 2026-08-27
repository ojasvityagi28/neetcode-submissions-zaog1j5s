from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = 1
        dp = [nums[0]]

        for i in range(1 , len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                LIS +=1 
                continue
            index = bisect_left(dp , nums[i]) #finds the first index where the value is greater than or equal to nums[i]
            dp[index] = nums[i]
        return LIS
        