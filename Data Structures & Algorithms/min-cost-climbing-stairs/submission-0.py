class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two = 0
        one = cost[n - 1]

        for i in range(n - 2 ,-1 , -1):
            tmp = one
            one = min((cost[i] + one) , (cost[i] + two))
            two = tmp
        return min(one , two)

        