class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        running = 0

        start = 0
        for i in range(len(gas)):
            if running + (gas[i] - cost[i]) >= 0:
                running += gas[i] - cost[i]
            else:
                running = 0
                start = i + 1
        return start
        
        
        