class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i , buy):
            if i>= len(prices):
                return 0 #no profit no loss

            if (i , buy) in dp:
                return dp[(i , buy)]

            if buy:
                buying = dfs(i + 1 , not buy) - prices[i]
                cooldown = dfs(i + 1 , buy) 
                dp[(i , buy)] = max(buying , cooldown)
            else:
                selling = dfs(i + 2 ,not buy) + prices[i]
                cooldown = dfs(i + 1 , buy) 
                dp[(i , buy)] = max(selling, cooldown)
            return dp[(i , buy)]
        
        return dfs(0 , True)



        