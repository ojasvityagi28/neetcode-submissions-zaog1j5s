class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        res = 1
        n = len(nums)

        for i in range(n - 1, -1, -1):
                for j in range(i + 1, n):
                    if nums[j] > nums[i]:
                        dp[i] = max(dp[i], 1 + dp[j])
                res = max( res , dp[i] )

        return res