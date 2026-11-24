class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        res = 0
        max_length = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if dp[i][0] < 1 + dp[j][0]:
                        dp[i][0] = 1 + dp[j][0]
                        dp[i][1] = dp[j][1]
                    elif dp[i][0] == 1 + dp[j][0]:
                        dp[i][1] += dp[j][1]


        max_length = max(x[0] for x in dp)

        for x in dp:
            if x[0] == max_length:
                res += x[1]
        return res            
            

        