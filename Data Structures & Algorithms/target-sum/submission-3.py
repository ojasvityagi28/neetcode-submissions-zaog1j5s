class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for total, ways in dp.items():
                next_dp[total + nums[i]] += ways
                next_dp[total - nums[i]] += ways
            dp = next_dp
        return dp[target]