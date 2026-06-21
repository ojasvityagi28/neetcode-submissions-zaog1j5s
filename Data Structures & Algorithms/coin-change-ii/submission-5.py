class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(index, target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if (index, target) in dp:
                return dp[(index, target)]

            dp[(index, target)] = 0

            for i in range(index, len(coins)):
                if target >= coins[i]:
                    dp[(index, target)] += dfs(i,  target - coins[i])

            return dp[(index, target)]

        return dfs(0, amount)