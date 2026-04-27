class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(index, target):
            if target == 0:
                return 1
            if (index, target) in dp:
                return dp[(index, target)]

            dp[(index, target)] = 0

            for i in range(index, len(coins)):
                new_target = target - coins[i]   # ✅ move inside loop

                if new_target == 0:
                    dp[(index, target)] += 1
                elif new_target > 0:
                    dp[(index, target)] += dfs(i, new_target)

            return dp[(index, target)]

        return dfs(0, amount)