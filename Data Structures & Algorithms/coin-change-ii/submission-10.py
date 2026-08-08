class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(index, target):
            if target == 0:
                return 1
            if (index , target) in memo:
                return memo[(index , target)]

            memo[(index , target)] = 0

            for i in range(index, len(coins)):
                if target >= coins[i]:
                    memo[(index , target)] += dfs(i , target - coins[i])
            return memo[(index , target)]
            
        return dfs(0 , amount)