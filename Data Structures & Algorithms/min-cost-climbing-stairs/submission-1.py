class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        one = cost[n - 1]
        two = 0
        res = 0
        for i in range(n - 2 , -1 , -1):
            res = min(cost[i] + one , cost[i] + two)
            one , two = res , one
        return min(one , two)
        