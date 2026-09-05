class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two = 0
        one = 0
        curr = 0
        for i in range(2 , n + 1):
            curr =min(one + cost[i - 1] , two + cost[i - 2])
            two , one = one, curr
        return curr
            
        