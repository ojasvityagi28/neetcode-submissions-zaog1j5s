class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1

        for c in coins:
            nextDP = [0]*(amount + 1)
            nextDP[0] = 1

            for a in range(1 , len(dp)):
                nextDP[a] = dp[a]
                if  a >= c:
                    nextDP[a] += nextDP[a - c]
            dp = nextDP
        return dp[amount]

        